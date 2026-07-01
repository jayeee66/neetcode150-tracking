# Union-Find(DSU)
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # init parent node list
        parent = []
        for i in range(len(edges)+1):
            # node's root node are itself in the beginning
            parent.append(i)
        
        # find node's root node
        def find(node):
            if parent[node] == node:
                return node
            return find(parent[node])
        # compare two nodes, 
        # if two nodes have different root,
        # change with the same root, means connected
        def union(n1, n2):
            if find(n1) != find(n2):
                parent[find(n2)] = find(n1)
                return True
            return False
        # if two nodes have same root before connecting, means cycle.
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
            
