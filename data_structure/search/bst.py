#!/usr/bin/python3

from ST import ST, BtNode


class bst(ST):
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
        # 有可能根节点更新
        self.root = self.put(key, value, self.root)

    # 删除
    def delete(self, key):
        self.root = self.delete_node(key, self.root)

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
        # 找到key,存在节点则更新值,否则插入新的节点.
        if node is None:
            return BtNode(key, value, N=1)
        cmp = self.key_compare(key, node.key)
        if cmp < 0:
            node.lchild = self.put(key, value, node.lchild)
        elif cmp > 0:
            node.rchild = self.put(key, value, node.rchild)
        else:
            node.value = value
        node.N = self.size(node.lchild) + self.size(node.rchild) + 1
        return node

    def min(self, node=None):
        # 以node为根节点的子树的最小值
        if node.lchild is None:
            return node
        else:
            return self.min(node.lchild)

    def max(self, node=None):
        # 以node为根节点的子树的最大值
        if node.rchild is None:
            return node
        else:
            return self.max(node.rchild)

    def deleteMin(self, node=None):
        # 递归删除最小节点
        if node.lchild is None:
            return node.rchild
        node.lchild = self.deleteMin(node.lchild)
        node.N = self.size(node.lchild) + self.size(node.rchild) + 1
        return node

    def deleteMax(self, node=None):
        # 递归删除最大节点
        if node.rchild is None:
            return node.lchild
        node.rchild = self.deleteMax(node.rchild)
        node.N = self.size(node.lchild) + self.size(node.rchild) + 1
        return node

    def delete_node(self, key, node=None):
        # 如果节点为空
        if node is None:
            return None
        cmp = self.key_compare(key, node.key)
        # 继续向下递归
        if cmp < 0:
            node.lchild = self.delete_node(key, node.lchild)
        elif cmp > 0:
            node.rchild = self.delete_node(key, node.rchild)
        else:
            # 如果只有一个节点/子节点均为空
            if node.lchild is None:
                return node.rchild
            if node.rchild is None:
                return node.lchild
            # 两个子节点均不为空
            tmp = node  # 备份node节点
            node = self.min(tmp.rchild)  # node位置被右子树最左边节点取代
            tmp.rchild = self.deleteMin(tmp.rchild)
            node.rchild = tmp.rchild  # 新node的右子树 = 删除最左边节点依旧大于新node的原node的右子树
            node.lchild = tmp.lchild  # 新node的左子树 = 原node的左子树
        # 更新节点计数器
        node.N = self.size(node.lchild) + self.size(node.rchild) + 1
        return node

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

    def contains(self, key):
        pass

    def isEmpty(self):
        if self.root is None:
            return False
        else:
            return True

    def size(self, node=None):
        if node is None:
            return 0
        else:
            return node.N
