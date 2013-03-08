__author__ = 'Colin Moore-Hill'

from py2neo import neo4j, rest, cypher
graph_db = neo4j.GraphDatabaseService("http://localhost:7474/db/data/")

class TemplateNode():

    def findSingleNodeById(self, ref):
        node = graph_db.get_node(68)          # to find node by Id.
        print(node)
        return node["name"]

    def getNodeListing(self):
        pass

    def createNode(self):
        pass

    def findAllNodes(self):
        pass


