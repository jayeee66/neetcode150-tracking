# Dijkstra's
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjMap = defaultdict(list)
        for i in range(n):
            adjMap[i]
        for s, d, cost in flights:
            adjMap[s].append([d, cost])
        heap = [(0, src, -1)]
        while heap:
            currCost, currStop, stops = heapq.heappop(heap)
            if stops > k:
                continue
            if stops <= k and currStop == dst:
                return currCost
            for nextStop, cost in adjMap[currStop]:
                nextCost = currCost + cost
                nextStops = stops + 1
                heapq.heappush(heap, (nextCost, nextStop, nextStops))
            #print(heap)
        return -1

