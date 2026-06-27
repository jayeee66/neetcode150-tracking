# Kahn’s algorithm
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # track how many prerequisites each course has with indegree
        indegree = [0] * numCourses
        # adjmap
        courseMap = defaultdict(list)
        for course, pre in prerequisites:
            # calculate the indegree of each course
            indegree[course] += 1
            courseMap[pre].append(course)
        # print(indegree)
        queue = deque()
        # start with courses that have no prerequisites
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        #print(queue)
        res = []
        while queue:
            c = queue.popleft()
            res.append(c)
            # reduce indegree for all courses that depend on c
            for course in courseMap[c]:
                indegree[course] -= 1
                # if all prerequisites are met, add to queue
                if indegree[course] == 0:
                    queue.append(course)
        # if not all courses are in res, there's a cycle
        if len(res) != numCourses:
                res = []
        return res
        


        
                
        
        
                
        