#!/usr/bin/python3
import unittest
from bt_base import BtNode, Btree


class test_bt(unittest.TestCase):
    def test_BtNode(self):
        tmp = BtNode()
        self.assertEqual(tmp.value, 0)
        self.assertEqual(tmp.lchild, None)
        self.assertEqual(tmp.rchild, None)
        with self.assertRaises(ValueError):
            tmp.value = 1.3
        with self.assertRaises(ValueError):
            tmp.lchild = 1.3
        with self.assertRaises(ValueError):
            tmp.rchild = 1.3

    def test_Btree(self):
        bt = Btree()
        tmp = bt.Cr_int()
        for node in tmp:
            self.assertTrue(isinstance(node, BtNode))
            self.assertTrue(isinstance(node.value, int))
            self.assertTrue(isinstance(node.lchild, (BtNode, type(None))))
            self.assertTrue(isinstance(node.rchild, (BtNode, type(None))))
        tmp = bt.Cr_str()
        for node in tmp:
            self.assertTrue(isinstance(node, BtNode))
            self.assertTrue(isinstance(node.value, str))
            self.assertTrue(isinstance(node.lchild, (BtNode, type(None))))
            self.assertTrue(isinstance(node.rchild, (BtNode, type(None))))
