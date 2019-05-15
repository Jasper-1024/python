#!/usr/bin/python3

from graphviz import Digraph, Graph


class prgraph(object):

    # 无向图
    def graph(self, gr) -> Graph:
        def filte(i: int, j: int) -> float:
            return (abs(i - j) + abs(i + j) * 10)

        filt = set()
        dot = self.dot_graph()
        V = gr.rV()
        for i in range(0, V):
            for j in gr.adjlist(i):
                ha = filte(i, j)
                if ha not in filt:
                    dot.edge(str(i), str(j))
                filt.add(ha)
        return dot

    # 有向图
    def digraph(self, digr) -> Digraph:
        dot = self.dot_digraph()
        V = digr.rV()
        for i in range(0, V):
            for j in digr.adjlist(i):
                dot.edge(str(i), str(j))
        return dot

    def dot_graph(self) -> Graph:
        dot = Graph(name='graph', node_attr={'shape': 'circle'})
        return dot

    def dot_digraph(self) -> Digraph:
        dot = Digraph(name='digraph', node_attr={'shape': 'circle'})
        return dot
