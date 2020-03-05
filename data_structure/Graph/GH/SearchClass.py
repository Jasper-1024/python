#!/usr/bin/python3


# Search base class
class Search(object):
    # find all vertices connected to s
    def search(self, Graph, s: int = 0):
        pass

    # return whether s and v connect
    def marked(self, v: int = 0) -> bool:
        return False

    # return the number  of all vertices connected to s
    def count(self) -> int:
        return 0


# Path base class
class Paths(object):
    # find all path which began with s
    def paths(self, Graph, s: int = 0):
        pass

    # whether v and s has path
    def hasPathTo(self, v: int = 0) -> bool:
        return False

    # retuen path between s and v ,if not exist return null
    def pathTo(self, v: int = 0):
        return None
