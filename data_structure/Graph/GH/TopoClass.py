#!/usr/bin/python3
from .GHclass import GH


# base class of Topological sort
class Topological(object):
    def __init__(self, G: GH):
        pass

    # G  is  DAG?
    def isDAG(self) -> bool:
        return False

    # return  result of Topological sort
    def order(self) -> list:
        return []
