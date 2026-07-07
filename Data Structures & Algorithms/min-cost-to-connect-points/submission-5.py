# Prim's
# Optimal
# Start from node, find the least weight path to go.
# Get min cost of traversing the whole nodes.
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # record distance and the index of points to represent the node
        heap = [(0, 0)]
        visited = set()
        cost = 0
        while heap:
            # start from current node
            dist, i = heapq.heappop(heap) # 'i' is index of point
            if i in visited:
                continue
            # add the minimum cost
            cost += dist
            visited.add(i)
            # Record all the cost to other nodes from current node
            for j in range(n):
                if i == j or j in visited:
                    continue
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap,(d, j))
            #print(heap)
            
        return cost
            
        