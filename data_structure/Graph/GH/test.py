#!/usr/bin/python3
import unittest
from Graph import Graph, Graph_AM
from Digraph import Digraph, Digraph_AM


class test_GH(unittest.TestCase):
    G = [[1, 2], [1, 3], [1, 4], [3, 2], [3, 3], [4, 3]]

    def test_Graph(self):
        gr = Graph(5)
        gram = Graph_AM(5)
        for item in self.G:
            gr.addEdge(item[0], item[1])
            gram.addEdge(item[0], item[1])

        self.assertTrue(gr.V == gram.V)
        self.assertTrue(gr.E == gram.E)

        a = gr.adjlist(1)
        b = gram.adjlist(1)
        self.assertTrue(a == b)

    def test_Digraph(self):
        gr = Digraph(5)
        gram = Digraph_AM(5)
        for item in self.G:
            gr.addEdge(item[0], item[1])
            gram.addEdge(item[0], item[1])

        self.assertTrue(gr.V == gram.V)
        self.assertTrue(gr.E == gram.E)

        a = gr.adjlist(1)
        b = gram.adjlist(1)
        self.assertTrue(a == b)


if __name__ == "__main__":
    unittest.main()
