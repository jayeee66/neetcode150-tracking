# Heap
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build hash map to store count
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # print(count)
        
        # Append items into heap and pop the least frequency item if the size of the heap is greater than k
        heap = []
        for num, cnt in count.items():
            heapq.heappush(heap, [cnt, num])
        # print(len(heap))
            if len(heap) > k:
                heapq.heappop(heap)
        # print(heap)
        
        # Build result array from the heap
        res = []
        for freq in heap:
            res.append(freq[1])
        return res








        


