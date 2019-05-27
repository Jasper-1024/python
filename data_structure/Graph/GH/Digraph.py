#!/usr/bin/python3
from .GHclass import GH
import pickle


class Digraph(GH):
    V: int = 0
    E: int = 0
    adj: list = []

    def __init__(self, V: int = 0):
        self.V = V
        self.E = 0
        self.adj = [[] for i in range(V)]  # 创建邻接表,初始化为空

    def rV(self) -> int:
        return self.V

    def rE(self) -> int:
        return self.E

    def addEdge(self, v: int, e: int):
        self.adj[v].append(e)  # 有向图单向添加
        self.E += 1

    def adjlist(self, v: int) -> list:
        return self.adj[v]

    def reverse(self):
        R = Digraph(self.V)
        for v, item in enumerate(self.adj):
            for e in item:
                R.addEdge(e, v)
        return R

    def save(self):
        file = open('Digraph.pickle', 'wb')
        pickle.dump(self, file)
        file.close

    def load(self):
        with open('Digraph.pickle', 'rb') as file:
            digraph = pickle.load(file)
        return digraph


class Digraph_AM(GH):
    V: int = 0
    E: int = 0
    adj: list = []

    def __init__(self, V: int = 0):
        self.V = V
        self.E = 0
        self.adj = [[0 for i in range(V)] for i in range(V)]  # 创建邻接矩阵

    def rV(self) -> int:
        return self.V

    def rE(self) -> int:
        return self.E

    def addEdge(self, v: int, e: int):
        self.adj[v][e] = 1  # 有向图单向添加
        self.E += 1

    def adjlist(self, v: int) -> list:
        vlist = []
        for e, item in enumerate(self.adj[v]):
            if item == 1:
                vlist.append(e)
        return vlist

    def reverse(self):
        R = Digraph_AM(self.V)
        for v, itemv in enumerate(self.adj):
            for e, iteme in enumerate(itemv):
                if iteme == 1:
                    R.addEdge(v, e)
        return R

    def save(self):
        file = open('Digraph_AM.pickle', 'wb')
        pickle.dump(self, file)
        file.close

    def load(self):
        with open('Digraph_AM.pickle', 'rb') as file:
            digraph = pickle.load(file)
        return digraph


if __name__ == "__main__":
    test = Digraph(5)
    pass
