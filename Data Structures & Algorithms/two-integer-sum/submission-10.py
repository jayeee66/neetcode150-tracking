class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in nums_hash:
                return [nums_hash[diff], i]
            nums_hash[n] = i
            
        return []
