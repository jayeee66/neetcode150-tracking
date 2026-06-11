class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # For max heap, upside down the sort
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first_s = heapq.heappop(stones)
            second_s = heapq.heappop(stones)
            # If two stones are the same, both destroyed
            if first_s != second_s:
                heapq.heappush(stones, first_s - second_s)
        # print(stones)
        # If all destroyed, return 0
        return abs(stones[0]) if stones else 0