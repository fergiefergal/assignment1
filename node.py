""" node.py """
from collections import deque
from functools import total_ordering

@total_ordering
class Node:
  def __init__(self, state, parent, depth, cost):
    self.state = state    # State
    self.parent = parent  # Node generating this node
    self.depth = depth    # Depth from the initial node
    self.cost = cost      # Accumulated cost

  def __str__(self):
    return "(" + str(self.state) + "," + str(self.depth) + \
        "," + str(self.cost) + ")"

  def __repr__(self):
    return str(self)

  def __eq__(self, s):
    return isinstance(s, self.__class__) and \
        self.cost == s.cost

  def __lt__(self, s):
    return isinstance(s, self.__class__) and \
        self.cost < s.cost

def print_solution(n):
  if n is None:
    print("No solution")
    return
  r = deque()
  while n is not None:
    r.appendleft(n.state)
    n = n.parent
  for s in r:
    print(s)
