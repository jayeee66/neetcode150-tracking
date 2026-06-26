class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            courseMap[pre].append(course)
        
        visiting = set()

        def dfs(pre):
            if pre in visiting:
                return False
            
            visiting.add(pre)
            
            for course in courseMap[pre]:
                if not dfs(course):
                    return False
            visiting.remove(pre)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                
        