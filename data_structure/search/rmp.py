class Node(object):
    def __init__(self, k, v, c=RED, l=None, r=None):
        self.lchild = l
        self.rchild = r
        self.key = k
        self.color = c
        self.value = v


class Red_black_tree(object):
    def __init__(self):
        self.root = None
        self.node_size = 0

    def is_red(self, node):
        if node:
            return node.color
        else:
            return False

    def put(self, k, v):
        node = self.root
        self.root = self.insert(node, k, v)
        self.root.color = BLACK

    def get(self, k):
        return self.search(self.root, k)

    def insert(self, node, k, v):
        if not node:
            return Node(k, v)
        if k == node.key:
            node.value = v
        elif k < node.key:
            node.lchild = self.insert(node.lchild, k, v)
        else:
            node.rchild = self.insert(node.rchild, k, v)

        if (self.is_red(node.rchild)):  #右红变左红
            node = self.rotateLeft(node)
        if (self.is_red(node.lchild)
                and self.is_red(node.lchild.lchild)):  #连续左红就要右转
            node = self.rotateRight(node)

        if (self.is_red(node.lchild)
                and self.is_red(node.rchild)):  #两孩子都红，需要翻转颜色
            self.colorFlip(node)
        return node

    def search(self, node, x):
        current_node = node
        while True:
            if not current_node:
                result = None
                break
            elif x < current_node.key:
                current_node = current_node.lchild
            elif x > current_node.key:
                current_node = current_node.rchild
            else:
                result = current_node
                break
        if result:
            return result.value
        else:
            return None

    def rotateLeft(self, h):
        node = h.rchild
        h.rchild = node.lchild
        node.lchild = h
        node.color = node.lchild.color
        node.lchild.color = RED
        return node

    def rotateRight(self, h):
        node = h.lchild
        h.lchild = node.rchild
        node.rchild = h
        node.color = node.rchild.color
        node.rchild.color = RED
        return node

    def colorFlip(self, h):  #翻转颜色函数
        h.color = not h.color
        h.lchild.color = not h.lchild.color
        h.rchild.color = not h.rchild.color
        return h

    def fixUp(self, h):  #删除时，用到的往上修复的函数
        if self.is_red(h.rchild):
            h = self.rotateLeft(h)
        if self.is_red(h.lchild) and self.is_red(h.lchild.lchild):
            h = self.rotateRight(h)
        if self.is_red(h.lchild) and self.is_red(h.rchild):
            h = self.colorFlip(h)

        return h

    def moveRedRight(self, h):  #删除时右路查询的情况
        self.colorFlip(h)
        if self.is_red(h.lchild.lchild):
            h = self.rotateRight(h)
            self.colorFlip(h)
        return h

    def moveRedLeft(self, h):  #删除时左路查询的情况
        self.colorFlip(h)
        if self.is_red(h.rchild.lchild):
            h.rchild = self.rotateRight(h.rchild)
            h = self.rotateLeft(h)
            self.colorFlip(h)
        return h

    def deleteMin(self, h):
        if not h.lchild:  ##为何，因为不可能出现黑节点在右而左节点为空的情况。而在LLRBT里，红节点一直在左
            return None
        if self.is_red(h.lchild) and self.is_red(h.lchild.lchild):
            h = self.moveRedLeft(h)
        h.lchild = self.deleteMin(h.lchild)
        return self.fixUp(h)

    def remove(self, k):
        self.root = self.delete(self.root, k)
        self.root.color = BLACK

    def delete(self, h, k):
        if k < h.key:
            if (not self.is_red(h.lchild)
                    and not self.is_red(h.lchild.lchild)):
                h = self.moveRedLeft(h)
            h.lchild = self.delete(h.lchild, k)
        else:
            if self.is_red(h.lchild):
                h = self.rotateRight(h)
            if k == h.key and h.rchild == None:
                return None
            if not self.is_red(h.rchild) and not self.is_red(h.rchild.lchild):
                h = self.moveRedRight(h)
            if k == h.key:
                h.key = self.min(h.rchild)
                h.value = self.search(h.rchild, h.key)
                h.rchild = self.deleteMin(h.rchild)
            else:
                h.rchild = self.delete(h.rchild, k)
        return self.fixUp(h)

    def min(self):  #查询最小节点
        if (self.root == None):
            return None
        else:
            return min(self.root)

    def min(self, x):  #查询某子树的最小节点
        if (x.lchild == None):
            return x.key
        else:
            return self.min(x.lchild)