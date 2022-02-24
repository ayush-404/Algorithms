
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        stack = []
        visited = set()
        stack.append()
        while len(stack) != 0:
          curr_node = stack.pop()
          new_node = Node()
          new_node.val = curr_node.val
          if curr_node not in visited:
            for node in curr_node.neighbors:
              neigh = Node(node.val)
              new_node.neighbors.append(neigh)
              visited.add(curr_node)
          