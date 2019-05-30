#!/usr/bin/python3

from GH import Graph, Search, Paths
from gif import getGr, gif, dot_node


class DFS(Search):
    marked: list = []
    count: int = 0

    def __init__(self, gr: Graph, s: int):
        self.marked = [False] * gr.rV()
        self.dfs(gr, s)

    @dot_node
    def dfs(self, gr: Graph, v: int):
        self.marked[v] = True
        self.count += 1
        for w in gr.adjlist(v):
            if not self.rmarked(w):
                self.dfs(gr, w)

    def rmarked(self, w: int) -> bool:
        return self.marked[w]

    def rcount(self) -> int:
        return self.count


class DFP(Paths):
    marked: list[bool] = []
    edgeTo: list[int] = []
    s: int = 0

    def __init__(self, gr: Graph, s: int):
        self.marked = [False] * gr.rV()
        self.marked = [None] * gr.rV()
        self.s = s
        self.dfs(gr, s)

    def dfs(self, gr: Graph, v: int):
        self.marked[v] = True
        for w in gr.adjlist(v):
            if not self.rmarked(w):
                self.edgeTo[w] = v
                self.dfs(gr, w)

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
    df = DFS(gr, 0)
    gif()
    pass
