# Kruskal's
# find the minimum distance manhattan distance between the two points and sort
# connect them first
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # record all edges and sort it
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((dist, i, j))
        edges.sort()

        # Find-Union
        parents = []
        for i in range(n):
            parents.append(i)
        #print(parents)
        def find(node):
            if parents[node] == node:
                return node
            return find(parents[node])
        
        def union(n1, n2):
            if find(n1) != find(n2):
                parents[find(n2)] = find(n1)
                return False
            return True
        
        cost = 0
        # if not cycle(haven't connected), add it
        for dist, i, j in edges:
            if not union(i, j):
                cost += dist
        
        return cost
        