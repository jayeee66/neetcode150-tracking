class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for i in range(len(nums)):
            m[nums[i]] += 1
        
        arr = []
        for num, cnt in m.items():
            arr.append([cnt,num])
        arr.sort()

        res= []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
