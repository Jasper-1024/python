#!/usr/bin/python3

from enum import Enum, unique


@unique
class Color(Enum):
    red = 'red'
    black = 'black'


class BtNode(object):
    # key值 ,节点值 ,颜 `色 ,左子树 ,右子树 ,节点计数器
    def __init__(self,
                 key=0,
                 value=0,
                 color=None,
                 leftBt=None,
                 rightBt=None,
                 N=0):
        self.key = key
        self.value = value
        self.color = color
        self.lchild = leftBt
        self.rchild = rightBt
        self.N = N

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key):
        if not isinstance(key, int):
            raise ValueError('key must be int!')
        self.__key = key

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, values):
        if not (isinstance(values, int) or isinstance(values, str)):
            raise ValueError('value must be int or str!')
        self.__value = values

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        if not (isinstance(color, str) or (color is None)):
            raise ValueError('color must be str')
        self.__color = color

    @property
    def lchild(self):
        return self.__lchild

    @lchild.setter
    def lchild(self, leftBt):
        if not (isinstance(leftBt, BtNode) or (leftBt is None)):
            raise ValueError('leftBt must be BtNode')
        self.__lchild = leftBt

    @property
    def rchild(self):
        return self.__rchild

    @rchild.setter
    def rchild(self, rightBt):
        if not (isinstance(rightBt, BtNode) or (rightBt is None)):
            raise ValueError('rightBt must be BtNode')
        self.__rchild = rightBt

    @property
    def N(self):
        return self.__N

    @N.setter
    def N(self, N):
        if not isinstance(N, int):
            raise ValueError('N must be an int!')
        self.__N = N
