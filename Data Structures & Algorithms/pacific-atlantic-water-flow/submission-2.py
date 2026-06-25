class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1 ,0), (0 ,1), (0, -1)]
        # record start node from both oceans
        pacific = []
        atlantic = []
        # record visited nodes
        pacific_visited = set()
        atlantic_visited = set()
        # append nodes close to oceans
        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r, cols - 1))
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows - 1, c))
        # print(pacific,atlantic)
        def dfs(r, c, prev, visited):
            if (r < 0 or c < 0 or 
                r >= rows or c >= cols or
                heights[r][c] < prev):
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            
            for dr, dc in directions:
                dfs(r + dr, c + dc, heights[r][c], visited)
        
        # start from each ocean
        for r, c in pacific:
            dfs(r, c, heights[r][c], pacific_visited)
        for r, c in atlantic:
            dfs(r, c, heights[r][c], atlantic_visited)
        
        # get coordinates in both list,
        # which means can flow in both oceans
        for r, c in atlantic_visited:
            if (r, c) in pacific_visited:
                res.append([r, c])

        return res
            