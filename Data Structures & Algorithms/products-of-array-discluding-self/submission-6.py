class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        
        for i in range(len(nums)):
            count = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                count *= nums[j]

            l.append(count)
        return l








