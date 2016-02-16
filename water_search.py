""" water_bfgs.py """
import uninformed
import water
from node import print_solution

n, c  = uninformed.breadth_first_graph_search(water)
print_solution(n)
print("No. of visited nodes =", c)
