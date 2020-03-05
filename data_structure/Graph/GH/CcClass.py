#!/usr/bin/python3
from .GHclass import GH


# CC base class
class CC(object):
    # Pretreatment
    def __init__(self, G: GH):
        pass

    # whether w and v connected
    def connected(self, v: int, w: int) -> bool:
        return False

    # the number of Connected Component
    def count(self) -> int:
        return 0

    # the id number of Connected Component
    def id(self, v: int) -> int:
        return 0
