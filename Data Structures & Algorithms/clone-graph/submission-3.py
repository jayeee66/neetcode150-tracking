"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        oldToNew = {} #record new node copied

        def dfs(node):
            if node in oldToNew: # if visited
                return oldToNew[node] # return new node
            cloneNode = Node(node.val) # copy node
            oldToNew[node] = cloneNode # record into map
            for neighbor in node.neighbors:
                cloneNode.neighbors.append(dfs(neighbor)) # add clone neighbors
            return cloneNode
        return dfs(node)
            