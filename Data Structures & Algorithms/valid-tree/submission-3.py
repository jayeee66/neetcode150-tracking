# DFS
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap = defaultdict(list)
        for n1, n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)
        
        visited = set()
        #print(adjMap)

        def dfs(node, parent): # add parent to record parent node
            visited.add(node)
            # print(visited)
            for neighbor in adjMap[node]:
                # avoid getting back to parent
                if neighbor == parent:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor, node):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        # check if any node is isolated, a tree shouldn't have any
        if len(visited) != n:
            return False
        return True
                


