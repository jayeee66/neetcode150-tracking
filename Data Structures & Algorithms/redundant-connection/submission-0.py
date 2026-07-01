# DFS
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap = defaultdict(list)
        
        for i in range(1, len(edges)+1):
            adjMap[i] = []
        
        visited = set()
        # check is connected if I go with current path
        def dfs(node, target):
            visited.add(node)
            if node == target:
                return True
            for neighbor in adjMap[node]:
                if neighbor not in visited:
                    if dfs(neighbor, target):
                        return True
            return False

        for n1, n2 in edges:
            visited.clear()
            # If I can go to n2 with path, means the edges is Redundant Connection
            if dfs(n1, n2):
                return [n1, n2]
            else:
                adjMap[n1].append(n2)
                adjMap[n2].append(n1)
        return []