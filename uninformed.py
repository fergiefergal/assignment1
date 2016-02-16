""" uninformed.py """
from node import Node
from collections import deque
from heapq import heappush, heappop, heapify

# Find the index of "state" in "frontier"
def state_index(frontier, state):
  for i, n in enumerate(frontier):
    if n.state == state:
      return i
  return -1

def breadth_first_tree_search(problem):
  # Create the initial node containing the initial state
  initial_node = Node(problem.initial_state(), None, 0, 0)
  # Initialize a deque storing nodes to be visited
  frontier = deque()
  frontier.append(initial_node)
  counter = 0

  while True:
    # Is frontier empty?  
    if not frontier:  
      return (None, counter)   
    else:
      counter += 1
      # Remove a node from the frontier
      n = frontier.popleft()
      # Return the node if it contains a goal state
      if problem.is_goal(n.state):
        return (n, counter)
      else: # Generate successors and add to the frontier
        for s, c in problem.successors(n.state):
          new_node = Node(s, n, n.depth+1, n.cost+c)
          frontier.append(new_node)

def breadth_first_graph_search(problem):
  initial_node = Node(problem.initial_state(), None, 0, 0)
  frontier = deque()
  frontier.append(initial_node)
  # Initialize "explored" as a set to keep the states checked
  explored = set()
  counter = 0

  while True:
    if not frontier:
      return (None, counter)
    else:
      counter += 1
      n = frontier.popleft()
      # Add the state to "explored"
      explored.add(n.state)
      if problem.is_goal(n.state):
        return (n, counter)
      else:
        for s, c in problem.successors(n.state):
          # Add "s" to the frontier list only when it is 
          # not in the explored set nor in the frontier list
          if s not in explored and state_index(frontier, s) < 0:
            new_node = Node(s, n, n.depth+1, n.cost+c)
            frontier.append(new_node)

def uniform_cost_graph_search(problem):
  initial_node = Node(problem.initial_state(), None, 0, 0)
  frontier = []
  frontier.append(initial_node)
  explored = set()
  counter = 0

  while True:
    if not frontier:
      return (None, counter)
    else:
      counter += 1
      n = heappop(frontier)
      explored.add(n.state)
      if problem.is_goal(n.state):
        return (n, counter)
      else:
        for s, c in problem.successors(n.state):
          if s not in explored:
            i = state_index(frontier, s)
            new_node = Node(s, n, n.depth+1, n.cost+c)
            if i >= 0:
              if frontier[i].cost > new_node.cost:
                frontier[i] = new_node
                heapify(frontier)
            else:
              heappush(frontier, new_node)

def depth_first_tree_search(problem):
  initial_node = Node(problem.initial_state(), None, 0, 0)
  frontier = deque()
  frontier.append(initial_node)
  counter = 0

  while True:
    if not frontier:  
      return (None, counter)   
    else:
      counter += 1
      n = frontier.pop()
      if problem.is_goal(n.state):
        return (n, counter)
      else: 
        for s, c in problem.successors(n.state):
          new_node = Node(s, n, n.depth+1, n.cost+c)
          frontier.append(new_node)

def depth_first_graph_search(problem):
  initial_node = Node(problem.initial_state(), None, 0, 0)
  frontier = deque()
  frontier.append(initial_node)
  explored = set()
  counter = 0

  while True:
    if not frontier:
      return (None, counter)
    else:
      counter += 1
      n = frontier.pop()
      explored.add(n.state)
      if problem.is_goal(n.state):
        return (n, counter)
      else:
        for s, c in problem.successors(n.state):
          if s not in explored and state_index(frontier, s) < 0:
            new_node = Node(s, n, n.depth+1, n.cost+c)
            frontier.append(new_node)

def depth_limited_graph_search(problem, limit):
  initial_node = Node(problem.initial_state(), None, 0, 0)
  frontier = deque()
  frontier.append(initial_node)
  explored = set()
  counter = 0

  while True:
    if not frontier:
      return (None, counter)
    else:
      counter += 1
      n = frontier.pop()
      explored.add(n.state)
      if problem.is_goal(n.state):
        return (n, counter)
      elif n.depth < limit:
        for s, c in problem.successors(n.state):
          if s not in explored and state_index(frontier, s) < 0:
            new_node = Node(s, n, n.depth+1, n.cost+c)
            frontier.append(new_node)

def iterative_deepening_graph_search(problem):
  n = None
  l = 0
  counter = 0
  while n is None:
     n, c = depth_limited_graph_search(problem, l)
     counter += c
     l += 1
  return n, counter
