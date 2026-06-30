# BFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
    
        visited = set()
        queue = deque([(0, -1)])
        visited.add(0)
        while queue:
            node, parent = queue.popleft()
            for neighbor in adjMap[node]:
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                
                visited.add(neighbor)
                queue.append((neighbor, node))
        return len(visited) == n