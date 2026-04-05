class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        for i in range(len(nums)):
            prob = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                prob *= nums[j]
        
            output[i] = prob
        return output 