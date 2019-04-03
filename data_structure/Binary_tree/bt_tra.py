#!/usr/bin/python3
from bt_base import Btree


class Btree_tra(object):
    @classmethod
    def Pre_Order_Re(self, root):
        if root:
            Btree.visit(root)
        if root.lchild:
            self.Pre_Order_Re(root.lchild)
        if root.rchild:
            self.Pre_Order_Re(root.rchild)

    @classmethod
    def In_Order_Re(self, root):
        if root.lchild:
            self.In_Order_Re(root.lchild)
        if root:
            Btree.visit(root)
        if root.rchild:
            self.In_Order_Re(root.rchild)

    @classmethod
    def Post_Order_Re(self, root):
        if root.lchild:
            self.Post_Order_Re(root.lchild)
        if root.rchild:
            self.Post_Order_Re(root.rchild)
        if root:
            Btree.visit(root)

    @classmethod
    def Pre_Order_loop(self, root):
        stack = []
        stack.append(root)
        while stack:
            p = stack.pop()
            Btree.visit(p)
            if p.rchild:
                stack.append(p.rchild)
            if p.lchild:
                stack.append(p.lchild)

    @classmethod
    def In_Order_loop(self, root):
        stack = []
        p = root
        while stack or p:
            while p:
                stack.append(p)
                p = p.lchild
            if stack:
                p = stack.pop()
                Btree.visit(p)
                p = p.rchild

    @classmethod
    def Post_Order_loop(self, root):
        stack = []
        stackb = []
        stack.append(root)
        while stack:
            p = stack.pop()
            stackb.append(p)
            if p.lchild:
                stack.append(p.lchild)
            if p.rchild:
                stack.append(p.rchild)
        while stackb:
            Btree.visit(stackb.pop())


if __name__ == "__main__":
    tmp = Btree()
    arr = tmp.Cr_int()
    Btree_tra.Pre_Order_Re(arr[1])
    print('\n')
    Btree_tra.Pre_Order_loop(arr[1])
    print('\n')
    Btree_tra.In_Order_Re(arr[1])
    print('\n')
    Btree_tra.In_Order_loop(arr[1])
    print('\n')
    Btree_tra.Post_Order_Re(arr[1])
    print('\n')
    Btree_tra.Post_Order_loop(arr[1])
