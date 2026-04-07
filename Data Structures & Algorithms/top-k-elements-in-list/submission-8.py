# Bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Build hash map to store count
        # Build bucket array where the index is the frequency and the value is the list of numbers with that frequency
        # Iterate the bucket array from the end and append the numbers to the result until the size of the result is k
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            bucket[cnt].append(num)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res








        


