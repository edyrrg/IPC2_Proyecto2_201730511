import unittest

from src.adt.my_matrix_list import MyMatrixList
from src.adt.node import Node


class TestMatrixList(unittest.case):
    def test_append_next(self):
        mlist = MyMatrixList()
        mlist.append_next(1)
        self.assertIsInstance(mlist.head, Node)


if __name__ == '__main__':
    unittest.main()
