from node import Node

class Graph(object):
  def __init__(self):
    self.nodes = []

  def addNode(self, id):
    new_node = Node(id) # Eg, the first node's ID = 0
    print("Added node:", new_node.id)

    self.nodes.append(new_node)
    # return new_node.id

  def linkNodes(self, n1, n2, cost):
    self.nodes[n1].addNeighbour(n2, cost)

  def print(self):
    for x in self.nodes:
      x.printNeighbours()
    # print(self.nodes)
