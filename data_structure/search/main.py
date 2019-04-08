#!/usr/bin/python3

from ST import randoms, prtree
from bst import bst
from llrbt import llrbt
from scht import scht
from lpht import lpht

prt = prtree()


def printree(node):
    dot = prt.dot(node)
    dot.view()
    prt.dots.append(dot)
    # print(dot.source)
    # dot.render(
    # filename=None, directory=None, view=False, cleanup=False, format='png')


if __name__ == "__main__":
    # dots清理等
    prt.dots.clear()
    t_bst = bst()
    t_llrbt = llrbt()
    t_sc = scht()
    t_lp = lpht()
    # 取数据集
    d = randoms.dict_int(n=100)
    keys = [key for key in d]
    minkey = min(keys)
    maxkey = max(keys)
    # 插入
    for k, v in d.items():
        t_bst.insert(k, k)
        t_llrbt.insert(k, k)
        t_sc.insert(k, k)

    # test
    for i in range(1, len(keys)):
        if t_bst.search(i) != t_sc.search(i):
            print('search falied')
        if t_lp.search(i) != t_sc.search(i):
            print('search2 falied')
    for i in range(1, len(keys)):
        if t_bst.select(i) != t_llrbt.select(i):
            print('select falied')
    for key in keys:
        if t_bst.rank(key) != t_llrbt.rank(key):
            print('rank falied')

    # print(minkey, test.rank(minkey))
    # print(maxkey, test.rank(maxkey))
    # ert = bst.select_node(0, bst.root)

    # d = randoms.dict_int(n=15)
    # keys = [key for key in d]
    # test = llrbt()
    # for k, v in d.items():
    #     test.insert(k, k)
    #
    # printree(test.root)
    #
    # test.delete(keys[5])
    # printree(test.root)

    # while test.root:
    #     test.test_delemax()
    #     printree(test.root)

    # prt.gif()
    # dot.render(
    # filename=None, directory=None, view=False, cleanup=False, format='png')
    pass
