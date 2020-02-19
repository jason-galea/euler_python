from node import Node

class Graph(object):
  def __init__(self):
    self.nodes = []

  def addNode(self, id, value):
    new_node = Node(id, value) # Eg, the first node's ID = 0

    self.nodes.append(new_node)
    # return new_node.id

  def linkNodes(self, n1, n2, cost):
    self.nodes[n1].addNeighbour(n2, cost)

  def print(self):
    for i in self.nodes:
      i.printNeighbours()
    # print(self.nodes)
