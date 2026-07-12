# Bottom-up
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(nums):
            n = len(nums)
            dpL = [0] * (n + 1)
            dpL[0] = nums[0]
            if n == 1: 
                return dpL[0]
            dpL[1] = max(dpL[0], nums[1])

            for i in range(2, n):
                dpL[i] = max(dpL[i - 1], nums[i] + dpL[i - 2])
       
            return dpL[n - 1]

        
        return max(dp(nums[:-1]), dp(nums[1:]))