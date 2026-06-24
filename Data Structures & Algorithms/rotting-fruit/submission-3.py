# BFS
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        # record fresh fruit
        fresh = 0
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while queue and fresh != 0: # avoid the fresh all gone but still count
            # multi rotten fruit spread at the same time
            for i in range(len(queue)):
                cr, cc = queue.popleft()
            
                for dr, dc in directions:
                    nr, nc = cr + dr, cc + dc
                    if (nc < 0 or nr < 0 or 
                        nr >= rows or nc >= cols or
                        grid[nr][nc] != 1):
                        continue
                    else:
                        grid[nr][nc] += 1
                        queue.append((nr, nc))
                        fresh -= 1
            minutes += 1
        return -1 if fresh != 0 else minutes
