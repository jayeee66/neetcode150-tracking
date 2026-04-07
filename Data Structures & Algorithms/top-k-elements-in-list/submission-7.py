class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # print(count)

        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, [cnt, num])
        # print(len(heap))
            if len(heap) > k:
                heapq.heappop(heap)
        print(heap)
        
        res = []
        for freq in heap:
            res.append(freq[1])
        return res








        


