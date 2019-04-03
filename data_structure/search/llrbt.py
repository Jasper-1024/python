#!/usr/bin/python3

from ST import ST, BtNode

red = 'red'
black = 'black'


class llrbt(ST):
    def __init__(self):
        self.root = None

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, root):
        if not (isinstance(root, BtNode) or (root is None)):
            raise ValueError('root must be BtNode')
        self._root = root

    # 查找
    def search(self, key):
        return self.get(key, self.root)

    # 插入
    def insert(self, key, value):
        self.root = self.put(key, value, self.root)
        self.root.color = black

    # 删除
    def delete(self, key):
        if (not self.isred(self.root.lchild)) and (not self.isred(
                self.root.rchild)):
            self.root.color = red
        self.root = self.delete_node(key, self.root)
        if self.root:
            self.root.color = black

    # 选择 返回排名k的key
    def select(self, k):
        return self.select_node(k, self.root).key

    # 排名 返回key的排名
    def rank(self, key):
        return self.rank_node(key, self.root)

    # 范围查找
    def kesys(self, min, max):
        arr = []
        self.keys_node(arr, min, max, self.root)
        return arr

    def get(self, key, node=None):
        # 找到以node为根节点的子树,返回key对应的值,不存在返回null
        if node is None:
            return None
        cmp = self.key_compare(key, node.key)
        if cmp < 0:
            return self.get(key, node.lchild)
        elif cmp > 0:
            return self.get(key, node.rchild)
        else:
            return node.value

    def put(self, key, value, node=None):
        # 空位置,插入新的红色节点
        if node is None:
            return BtNode(key, value, color=red, N=1)
        cmp = self.key_compare(key, node.key)
        # 插入/递归
        if cmp < 0:
            node.lchild = self.put(key, value, node.lchild)
        elif cmp > 0:
            node.rchild = self.put(key, value, node.rchild)
        else:
            node.value = value
        # 右链接为红,左链接为黑,左旋转
        if self.isred(node.rchild) and (not self.isred(node.lchild)):
            node = self.rotateLeft(node)
        # 左链接为红,左左链接为红,右旋转
        if self.isred(node.lchild) and self.isred(node.lchild.lchild):
            node = self.rotateRight(node)
        # 左链接为红,右链接为红,反转
        if self.isred(node.rchild) and self.isred(node.lchild):
            self.flipColors(node)
        # 节点计数器
        node.N = self.size(node.lchild) + 1 + self.size(node.rchild)
        return node

    def delete_node(self, key, node=None):
        # 左子树
        if self.key_compare(key, node.key) < 0:
            # 左链接,左左链接为黑
            if (not self.isred(node.lchild)
                    and not self.isred(node.lchild.lchild)):
                # 左子树处理
                node = self.moveRedLeft(node)
            # 递归进入左子树
            node.lchild = self.delete_node(key, node.lchild)
        # node/右子树
        else:
            # 左链接为红,右旋转
            if self.isred(node.lchild):
                node = self.rotateRight(node)
            # 待删除为 node,且右子树为空 删除
            if self.key_compare(key, node.key) == 0 and node.rchild is None:
                return None
            # 右链接为黑 右左链接为黑 右子树处理
            if not self.isred(node.rchild) and not self.isred(
                    node.rchild.lchild):
                node = self.moveRedRight(node)
            # 待删除为 node ,右子树不为空 寻找后继
            if self.key_compare(key, node.key) == 0:
                # 右子树最小
                node.key = self.min(node.rchild)
                node.value = self.search(node.rchild, node.key)
                # 递归删除后继节点
                node.rchild = self.deleteMin(node.rchild)
            else:
                # 递归进入右子树
                node.rchild = self.delete_node(key, node.rchild)
        return self.balance(node)

    def select_node(self, k, node=None):
        # 返回排名k的节点
        if node is None:
            return None
        n = self.size(node.lchild)
        if n > k:
            return self.select_node(k, node.lchild)
        elif n < k:
            return self.select_node(k - n - 1, node.rchild)
        else:
            return node

    def rank_node(self, key, node=None):
        # 返回node为根节点的子树中小于key的数量.
        if node is None:
            return 0
        cmp = self.key_compare(key, node.key)
        if cmp < 0:
            return self.rank_node(key, node.lchild)
        elif cmp > 0:
            return self.size(node.lchild) + 1 + self.rank_node(
                key, node.rchild)
        else:
            return self.size(node.lchild)

    def keys_node(self, arr, min, max, node=None):
        if node is None:
            return
        cmpmin = self.key_compare(min, node.key)
        cmpmax = self.key_compare(max, node.key)
        if cmpmin < 0:
            self.keys_node(arr, min, max, node.lchild)
        if (cmpmin <= 0) and (cmpmax >= 0):
            arr.append(node)
        if cmpmax > 0:
            self.keys_node(arr, min, max, node.rchild)

    def deleteMin(self, node=None):
        # 不存在右链接为红,so只考虑左链接即可
        if node.lchild is None:
            return None
        # 左链接,左左链接为黑
        if (not self.isred(node.lchild)) and (not self.isred(
                node.lchild.lchild)):
            node = self.moveRedLeft(node)
        # 递归
        node.lchild = self.deleteMin(node.lchild)
        # 返回平衡
        return self.balance(node)

    def deleteMax(self, node=None):
        # 左链接为红,右旋转
        if self.isred(node.lchild):
            node = self.rotateRight(node)
        # 右链接为空
        if node.rchild is None:
            return None
        # 右链接 右右链接为红
        if (not self.isred(node.rchild)
                and (not self.isred(node.rchild.rchild))):
            node = self.moveRedRight(node)
        # 递归
        node.rchild = self.deleteMax(node.rchild)
        # 返回平衡
        return self.balance(node)

    # 左旋转
    def rotateLeft(self, node):
        r_node = node.rchild
        node.rchild = r_node.lchild
        r_node.lchild = node
        # 原node的颜色
        r_node.color = node.color
        node.color = 'red'
        # 更新节点计数器
        r_node.N = node.N
        node.N = self.size(node.lchild) + 1 + self.size(node.rchild)
        return r_node

    # 右旋转
    def rotateRight(self, node):
        l_node = node.lchild
        node.lchild = l_node.rchild
        l_node.rchild = node
        # 原node的颜色#
        l_node.color = node.color
        node.color = 'red'
        # 更新节点计数器
        l_node.N = node.N
        node.N = self.size(node.lchild) + 1 + self.size(node.rchild)
        return l_node

    # 一个节点两条红链接/黑链接(删除用),反转
    def flipColors(self, node):
        # node.color = red
        # node.lchild.color = black
        # node.rchild.color = black
        def nor(node):
            if not (node is None):
                if node.color == red:
                    node.color = black
                else:
                    node.color = red

        # 反转
        nor(node)
        nor(node.lchild)
        nor(node.rchild)
        return node

    # 删除后,向上修复平衡
    def balance(self, node=None):
        # 右链接为红,左旋转
        if self.isred(node.rchild):
            node = self.rotateLeft(node)
        # 左链接为红,左左链接为红,右旋转
        if self.isred(node.lchild) and self.isred(node.lchild.lchild):
            node = self.rotateRight(node)
        # 左链接为红,右链接为红,反转
        if self.isred(node.rchild) and self.isred(node.lchild):
            self.flipColors(node)

        return node

    # 删除时右子树处理
    def moveRedRight(self, node=None):
        # node为红,右链接 右右链接 为黑
        # 反转node
        self.flipColors(node)
        # 右右链接为红 左旋转
        if self.isred(node.lchild.lchild):
            node = self.rotateRight(node)
        return node

    # 删除时左子树处理
    def moveRedLeft(self, node=None):
        # node为红,左链接 左左链接 为黑
        # 反转node
        self.flipColors(node)
        # 右左链接为红
        if self.isred(node.rchild.lchild):
            # 右子树 右旋转
            node.rchild = self.rotateRight(node.rchild)
            # node左旋转
            node = self.rotateLeft(node)
        return node

    # 节点是否为红色
    def isred(self, node=None):
        if node is None:
            return False
        elif node.color == 'red':
            return True
        else:
            return False

    # 查询某子树的最小节点
    def min(self, node=None):
        if node.lchild is None:
            return node.key
        else:
            return self.min(node.lchild)

    def size(self, node=None):
        if node is None:
            return 0
        else:
            return node.N

    def key_compare(self, key1, key2):
        if isinstance(key1, int) and isinstance(key2, int):
            return key1 - key2
        elif isinstance(key1, str) and isinstance(key2, str):
            if key1 > key2:
                return 1
            elif key1 == key2:
                return 0
            else:
                return -1
        else:
            raise ValueError('keys types not match!')

    def test_delemin(self):
        # root的左右链接均为黑
        if (not self.isred(self.root.lchild)) and (not self.isred(
                self.root.rchild)):
            self.root.color = red
        self.root = self.deleteMin(self.root)
        if self.root:
            self.root.color = black

    def test_delemax(self):
        # root的左右链接均为黑
        if (not self.isred(self.root.lchild)) and (not self.isred(
                self.root.rchild)):
            self.root.color = red
        self.root = self.deleteMax(self.root)
        if self.root:
            self.root.color = black


if __name__ == "__main__":
    pass
