#!/usr/bin/env python3
from graph import Graph
        
tri = [
  [75],
  [95, 64],
  [17, 47, 82],
  [18, 35, 87, 10],
  [20, 4, 82, 47, 65],
  [19, 1, 23, 75, 3, 34],
  [88, 2, 77, 73, 7, 63, 67],
  [99, 65, 4, 28, 6, 16, 70, 92],
  [41, 41, 26, 56, 83, 40, 80, 70, 33],
  [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
  [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
  [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
  [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
  [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]
result = 0

graph = Graph()

###### Converting tri[] into a graph ######

graph.addNode(0, 0) # Dummy node above tri
current_node = 1

for i, row in enumerate(tri):
  for j, value in enumerate(row):
    graph.addNode(current_node, value)

    if i > 0: # The top row cannot link to anything above it
      if j > 0: # The value furthest left cannot link to top-left
        graph.linkNodes(current_node - len(row), current_node, tri[i][j]) # Link top-left

      if j != len(row) - 1: # The value furthest right cannot link to top-right
        graph.linkNodes(current_node - len(row) + 1, current_node, tri[i][j]) # Link top-right

    else: # len(tri[0]) == 1, so this is only done once
      graph.linkNodes(0, 1, tri[0][0]) # Link dummy node to tri[0][0]

    current_node += 1

graph.print()

###### Dijkstra's Algorithm ######

