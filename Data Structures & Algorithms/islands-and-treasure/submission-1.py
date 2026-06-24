# Multi-source BFS
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                # add all the gates in queue first
                if grid[r][c] == 0:
                    queue.append((r ,c))

        while queue:
            cr, cc = queue.popleft()
            # move from gates
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
            
                if (nc < 0 or nr < 0 or 
                    nr >= rows or nc >= cols or
                    grid[nr][nc] != INF):
                    continue
                # if the gate reach the land first, means the closest
                grid[nr][nc] = grid[cr][cc] + 1
                queue.append((nr, nc)) # move to next land



