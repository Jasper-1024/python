#!/usr/bin/python3
import unittest
from ran import randoms
from bt_base import BTree


class test_randoms(unittest.TestCase):
    def test_list_int(self):
        arr = randoms.list_int()
        self.assertTrue(isinstance(arr, list))
        for x in arr:
            self.assertTrue(isinstance(x, int))

    def test_list_str(self):
        strs = randoms.list_str()
        print(strs)
        self.assertTrue(isinstance(strs, str))
