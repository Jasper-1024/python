#!/usr/bin/python3
from graphviz import Digraph, nohtml

if __name__ == "__main__":
    dot = Digraph(
        name='tree',
        comment='Tree',
        node_attr={
            'shape': 'record',
            'style': 'filled',
            'color': 'black',
            'fontcolor': 'white'
        })
    dot.node('9', nohtml('<f0> |<f1> 9|<f2>'))
    dot.node('5', nohtml('<f0> |<f1> 5|<f2>'))
    dot.edge('9:f0:sw', '5:f1')
    dot.node('18', nohtml('<f0> |<f1> 18|<f2>'), color='red')
    dot.edge('9:f2:se', '18:f1')
    print(dot.source)
    dot.render(
        filename=None, directory=None, view=False, cleanup=False, format='png')
    # dot.view()
