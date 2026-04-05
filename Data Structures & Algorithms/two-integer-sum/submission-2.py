class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = {}
        for i in range(len(nums)):
            pair[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            print(diff)
            if diff in pair and pair[diff] != i:
               return [i, pair[diff]]
        return []