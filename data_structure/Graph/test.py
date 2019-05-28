#!/usr/bin/python3

from GH import Graph, Digraph, prgraph, randoms

G = [[1, 2], [1, 3], [1, 4], [3, 2], [3, 3], [4, 3]]


def randomGr(V: int = 10, E: int = 20) -> Graph:
    gr = Graph(V)
    i = E
    while i > 0:
        v = randoms.r_int(V - 1)
        w = randoms.r_int(V - 1)
        # if v-w not exist, add edj
        if w not in gr.adjlist(v) and v != w:
            gr.addEdge(v, w)
            i -= 1
    return gr


if __name__ == "__main__":
    test = prgraph()
    gr = Graph(4)
    # for item in G:
    #     gr.addEdge(item[0], item[1])
    # v = gr.rV()
    # dot = test.graph(gr)
    # dot.view()

    # digr = Digraph(5)
    # for item in G:
    #     digr.addEdge(item[0], item[1])

    # dot = test.digraph(digr)
    # dot.view()
    # gr = gr.load()

    gs = randomGr(50, 60)
    dot = test.graph(gs)
    dot.view()
    pass