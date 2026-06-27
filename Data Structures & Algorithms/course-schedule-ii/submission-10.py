# topological sort DFS
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            courseMap[pre].append(course)
        
        visiting = set()
        visited = set()
        res = []
        def dfs(pre):
            # detect cycle
            if pre in visiting:
                return False

            if pre in visited:
                return True
            visiting.add(pre)
            
            for course in courseMap[pre]:
                # report false if any cycle in a path
                if not dfs(course):
                    return False
            # no cycle and clean the visiting list

            res.append(pre)
            # print(visiting)
            visiting.remove(pre)
            visited.add(pre)
            # print(visited)
            # good path
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        # reverse the order in the end.
        return res[::-1]
        
                
        
        
                
        