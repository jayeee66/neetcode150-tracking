# Dijkstra
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adjMap = defaultdict(list)
        for u, v, t in times:
            adjMap[u].append((v ,t))
        visited = set()
        heap = [(0, k)]
        time = 0
        while heap:
            t1, node = heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            time = t1
            # add node into heap
            for v, t2 in adjMap[node]:
                if v not in visited:
                    heapq.heappush(heap, (t1 + t2, v))
        if len(visited) == n:
            return time
        else:
            return -1
