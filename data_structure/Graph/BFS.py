#!/usr/bin/python3

from GH import Graph, Search, Paths
from collections import deque
from gif import getGr, dot_node, gif


class BFS(Search):
    marked: list = []
    count: int

    def __init__(self, G: Graph, s: int):
        self.marked = [False] * G.rV()
        self.count = 0
        self.dfs(G, s)

    def dfs(self, G: Graph, s: int):
        dot_node(s)
        queue = deque()
        self.marked[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            for w in G.adjlist(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.count += 1
                    queue.append(w)

                    dot_node(w)

    def rmarked(self, v: int) -> bool:
        return self.marked[v]

    def rcount(self) -> int:
        return self.count


class BFP(Paths):
    marked: list = []
    edgeTo: list = []
    s: int

    def __init__(self, G: Graph, s: int):
        self.marked = [False] * G.rV()
        self.edgeTo = [None] * G.rV()
        self.s = s
        self.dfs(G, s)

    def dfs(self, G: Graph, s: int):
        queue = deque()
        self.marked[s] = True
        queue.append(s)
        while queue:
            v = queue.popleft()
            for w in G.adjlist(v):
                if not self.marked[w]:
                    self.edgeTo[w] = v
                    self.marked[w] = True
                    queue.append(w)

    def hasPathTo(self, v: int) -> bool:
        return self.marked[v]

    def pathTo(self, v: int) -> list:
        if not self.hasPathTo(v):
            return None

        path = []
        path.append(v)
        x = self.edgeTo[v]

        while x != v:
            x = self.edgeTo[x]
            path.append(x)
        path.append(self.s)
        return path


if __name__ == "__main__":
    gr = getGr()
    bf = BFS(gr, 0)
    gif()
    pass
