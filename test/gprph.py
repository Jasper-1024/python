#!/usr/bin/python3
from graphviz import Digraph, Graph

if __name__ == "__main__":
    g = Graph('G', filename='process.gv')

    g.edge('0', '1')
    g.edge('0', '1')
    g.edge('0', '2')
    g.edge('0', '3')
    g.edge('0', '0')
    g.edge('1', '2')

    g.view()
