#!/usr/bin/python3
from .GHclass import GH
import pickle


# 图数据结构
class Graph(GH):
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
        self.adj[v].append(e)  # 无向图双向添加
        self.adj[e].append(v)
        self.E += 1

    def adjlist(self, v: int) -> list:
        return self.adj[v]

    def save(self, fileName: str = 'Graph.pickle'):
        file = open(fileName, 'wb')
        pickle.dump(self, file)
        file.close

    def load(self, fileName: str = 'Graph.pickle'):
        with open(fileName, 'rb') as file:
            graph = pickle.load(file)
        return graph


# 图数据结构
class Graph_AM(GH):
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
        self.adj[v][e] = 1  # 无向图双向添加
        self.adj[e][v] = 1
        self.E += 1

    def adjlist(self, v: int) -> list:
        vlist = []
        for e, item in enumerate(self.adj[v]):
            if item == 1:
                vlist.append(e)
        return vlist

    def save(self, fileName: str = 'Graph_AM.pickle'):
        file = open(fileName, 'wb')
        pickle.dump(self, file)
        file.close

    def load(self, fileName: str = 'Graph_AM.pickle'):
        with open(fileName, 'rb') as file:
            graph = pickle.load(file)
        return graph
