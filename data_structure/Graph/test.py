#!/usr/bin/python3

from GH import Graph, Digraph, prgraph

G = [[1, 2], [1, 3], [1, 4], [3, 2], [3, 3], [4, 3]]

if __name__ == "__main__":
    test = prgraph()
    gr = Graph(5)
    for item in G:
        gr.addEdge(item[0], item[1])
    v = gr.rV()
    dot = test.graph(gr)
    dot.view()

    # digr = Digraph(5)
    # for item in G:
    #     digr.addEdge(item[0], item[1])
    # dot = test.digraph(digr)
    # dot.view()
    pass