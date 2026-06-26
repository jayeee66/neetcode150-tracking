#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            courseMap[pre].append(course)
        
        visiting = set()
        # record visited to decrease runtime
        visited = set()
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
            visiting.remove(pre)
            visited.add(pre)
            #print(visited)
            # good path
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
                
        