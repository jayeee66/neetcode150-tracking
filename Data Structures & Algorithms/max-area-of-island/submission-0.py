#dfs
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        def dfs(r, c):
            # find water or over grid's max col and row
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or 
                grid[r][c] == 0 or(r, c) in visited):
                return 0
            # add in visited set
            visited.add((r, c))

            area = 1
            for dr, dc in directions:
                # find adjcent lands
                area += dfs(r + dr, c + dc)

            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = dfs(r, c)
                    maxArea = max(maxArea, currArea)
        return maxArea