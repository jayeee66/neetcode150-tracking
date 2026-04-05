class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        res = [1] * leng
        
        prefix = 1
        for i in range(leng):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(leng - 1, -1 , -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res







