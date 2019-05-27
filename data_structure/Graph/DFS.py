#!/usr/bin/python3

from GH import Graph, prgraph
from test import randomGr
import functools

test = prgraph()
gr = randomGr(50, 100)
dot = test.graph(gr)


def dot_node(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        dot.node(str(args[2]), color='red')
        return func(*args, **kw)

    return wrapper


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
    df = DFS(gr, 5)
    dot.view()
    pass
