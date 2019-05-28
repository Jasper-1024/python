#!/usr/bin/python3

from GH import Graph
from gif import getGr, gif, dot_node


class DFS(object):
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


if __name__ == "__main__":
    gr = getGr()
    df = DFS(gr, 0)
    gif()
    pass
