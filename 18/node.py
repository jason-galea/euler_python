class Node(object):
  def __init__(self, id, value):
    self.neighbours = []
    self.id = id
    self.value = value

  def addNeighbour(self, id, cost):
    self.neighbours.append([id, cost])
    # print("Node", self.id, "added neighbour", id, "with cost", cost)

  def printNeighbours(self):
    print("Node %i (%i) has links: %s" %(self.id, self.value, self.neighbours))