#!/usr/bin/python3
import unittest
from randoms import randoms
from bt import BtNode


class test_randoms(unittest.TestCase):
    def test_r_int(self):
        a = randoms.r_int()
        self.assertTrue(isinstance(a, int))

    def test_r_str(self):
        a = randoms.r_str(10)
        self.assertTrue(isinstance(a, str))

    def test_list_int(self):
        arr = randoms.list_int()
        self.assertTrue(isinstance(arr, list))
        for x in arr:
            self.assertTrue(isinstance(x, int))

    def test_BtNode(self):
        tmp = BtNode()
        for i in [
                i for i in dir(tmp)
                if not callable(i) and not i.startswith("__")
        ]:
            self.assertTrue((getattr(tmp, i) is None)
                            or (getattr(tmp, i) == 0))
            with self.assertRaises(ValueError):
                setattr(tmp, i, 1.3)
