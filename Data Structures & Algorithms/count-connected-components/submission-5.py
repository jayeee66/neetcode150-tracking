#BFS
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
        def bfs(node):
            queue = deque([node])
            while queue:
                n = queue.popleft()
                visited.add(n)
                for neighbor in adjMap[n]:
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
        count = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                count += 1
        return count
