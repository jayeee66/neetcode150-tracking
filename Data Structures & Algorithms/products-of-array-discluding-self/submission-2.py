class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        output = [0] * leng

        for i in range(leng):
            prob = 1
            for j in range(leng):
                if i == j :
                    continue
                prob *= nums[j]
            output[i] += prob



        return output 