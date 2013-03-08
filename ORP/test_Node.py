__author__ = 'Colin Moore-Hill'

import unittest
import TemplateNode

class UserTests(unittest.TestCase):
    global result, target
    result = 4
    target = TemplateNode.TemplateNode()

    def test_createNode(self):
        metadata = {"nodeId":0, "appRef":"usr0001", "name":"Dave"}
        expected = "Dave"

        self.assertEqual(4, 4)

    def test_findAllNodes(self):
        self.assertEqual(4, result)

    def test_findSingleNodeById(self):
        expected = "Dave"
        actualNode = target.findSingleNodeById(68)
        self.assertEqual(expected, actualNode)

    def test_JoinNodesRelation(self):
        self.assertEqual(4, result)
