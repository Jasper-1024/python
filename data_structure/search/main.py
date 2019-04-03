#!/usr/bin/python3

from ST import randoms, prtree
from bst import bst

if __name__ == "__main__":
    d = randoms.dict_int(n=15)
    keys = [key for key in d]
    minkey = min(keys)
    maxkey = max(keys)
    test = bst()
    for k, v in d.items():
        test.insert(k, v)
#    print(minkey, test.rank(minkey))
#    print(maxkey, test.rank(maxkey))
#    ert = bst.select_node(0, bst.root)
    prt = prtree()
    dot = prt.dot(test.root)
    print(dot.source)
    dot.render(
        filename=None, directory=None, view=False, cleanup=False, format='png')
