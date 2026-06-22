#bfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        def bfs(r, c):
            queue = deque([(r ,c)])
            # add in visited set
            visited.add((r, c))
            area = 1
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (nr < 0 or nc < 0 or
                    nr >= rows or nc >= cols or 
                    grid[nr][nc] == 0 or
                    (nr, nc) in visited):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))      
                    area += 1

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = bfs(r, c)
                    maxArea = max(maxArea, currArea)
        return maxArea