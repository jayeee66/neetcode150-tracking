class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjMap = {}
        for i in range(n):
            if i not in adjMap:
                adjMap[i] = []
        
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
    
        visited = set()
        # to find nodes that connected
        def dfs(node):
            visited.add(node)
            for neighbor in adjMap[node]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        count = 0
        for i in range(n):
            # find number of connected components with number of time of running dfs
            if i not in visited:
                dfs(i)
                count += 1
        return count
            

        


        