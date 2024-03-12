import unittest

from src.adt.node import Node


class TestNode(unittest.TestCase):
    def testDataNode(self):
        node = Node(1)
        self.assertEqual(node.data, 1, 'Node return data should be 1')

    def testNodeNext(self):
        node2 = Node(2)
        node1 = Node(1, _next=node2)
        self.assertEqual(node1.next, node2)

    def testNodeUp(self):
        node2 = Node(2)
        node1 = Node(3, _up=node2)
        self.assertEqual(node1.up, node2)

    def testNodeDown(self):
        node2 = Node(2)
        node1 = Node(3, _down=node2)
        self.assertEqual(node1.down, node2)

    def testNodePrev(self):
        node1 = Node(3)
        node2 = Node(2, _prev=node1)
        self.assertEqual(node2.prev, node1)

    def testNodeNotEquals(self):
        node1 = Node(1)
        node2 = Node(2)
        self.assertFalse(node1.__eq__(node2))

    def testNodeGreaterThan(self):
        node1 = Node(5)
        node2 = Node(2)
        self.assertTrue(node1.__gt__(node2))

    def testNodeLessThan(self):
        node1 = Node(5)
        node2 = Node(10)
        self.assertTrue(node1.__lt__(node2))

    def testNodeGreaterThanEquals(self):
        node1 = Node(5)
        node2 = Node(5)
        node3 = Node(1)
        self.assertTrue(node1.__ge__(node2))
        self.assertTrue(node1.__ge__(node3))

    def testNodeLessThanEqualsEquals(self):
        node1 = Node(4)
        node2 = Node(4)
        node3 = Node(15)
        self.assertTrue(node1.__le__(node2))
        self.assertTrue(node1.__le__(node3))


if __name__ == '__main__':
    unittest.main()
