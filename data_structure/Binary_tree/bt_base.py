#!/usr/bin/python3
import random
import copy
import string


class BtNode(object):
    def __init__(self, value=0, leftBt=None, rightBt=None):
        self.value = value
        self.lchild = leftBt
        self.rchild = rightBt

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, values):
        if not (isinstance(values, int) or isinstance(values, str)):
            raise ValueError('value must be an int or str!')
        self._value = values

    @property
    def lchild(self):
        return self._lchild

    @lchild.setter
    def lchild(self, leftBt):
        if not (isinstance(leftBt, BtNode) or (leftBt is None)):
            raise ValueError('leftBt must be BtNode')
        self._lchild = leftBt

    @property
    def rchild(self):
        return self._rchild

    @rchild.setter
    def rchild(self, rightBt):
        if not (isinstance(rightBt, BtNode) or (rightBt is None)):
            raise ValueError('rightBt must be BtNode')
        self._rchild = rightBt


class Btree(object):
    def __init__(self, len=50):
        self.__len = len
        self.__arr = [BtNode() for i in range(self.__len)]
        self.__link()

    def Cr_int(self):
        self.__arr = list(map(self.__randomint, self.__arr))
        return copy.deepcopy(self.__arr)

    def Cr_str(self, len=50):
        self.__arr = list(map(self.__randomstr, self.__arr))
        return copy.deepcopy(self.__arr)

    def __link(self):
        for i in range(self.__len - 1, 1, -1):
            if (i % 2) == 1:
                self.__arr[i // 2].rchild = self.__arr[i]
            else:
                self.__arr[i // 2].lchild = self.__arr[i]

    def __randomint(self, btNode):
        btNode.value = random.randint(0, 100)
        return btNode

    def __randomstr(self, btNode):
        btNode.value = ''.join(random.choices(string.ascii_lowercase, k=1))
        return btNode

    @classmethod
    def visit(self, node):
        return print(node.value, end=' ')


if __name__ == "__main__":
    bt = Btree()
    tmp = bt.Cr_str()
    for node in tmp:
        print(node.value)
    print(tmp)
