# Dijkstra's
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (0, -1), (1 ,0), (-1, 0)]
        heap = [[grid[0][0], 0, 0]]
        visited = set()

        visited.add((0, 0))
        while heap:
            currLevel, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return currLevel
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (nr < 0 or nr == n or
                    nc < 0 or nc == n or
                    (nr, nc) in visited):
                    visited.add((nr, nc))
                    maxLevel = max(currLevel, grid[nr][nc])
                    heapq.heappush(heap, [maxLevel, nr, nc])
        

                