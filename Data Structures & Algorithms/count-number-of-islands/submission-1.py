#bfs
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        island = 0
        visited = set()
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        def bfs(r, c):
            queue = deque([(r ,c)])
            visited.add((r, c))
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (nr < 0 or nc < 0 or
                    nr >= rows or nc >= cols or 
                    grid[nr][nc] == '0' or
                    (nr, nc) in visited):
                        continue
                    queue.append((nr, nc))
                    visited.add((nr, nc))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    island += 1
        return island
                