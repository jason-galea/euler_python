class Node(object):
  def __init__(self, id):
    self.neighbours = []
    self.id = id

  def addNeighbour(self, id, cost):
    self.neighbours.append([id, cost])
    print("Node", self.id, "added neighbour", id, "with cost", cost)

  def printNeighbours(self):
    print("%i: %s" %(self.id, self.neighbours))