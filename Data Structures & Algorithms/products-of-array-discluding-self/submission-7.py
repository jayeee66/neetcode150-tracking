class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Brute Force
        # l = []
        
        # for i in range(len(nums)):
        #     count = 1
        #     for j in range(len(nums)):
        #         if i == j:
        #             continue
        #         count *= nums[j]

        #     l.append(count)
        # return l
        n = len(nums)
        l = [1] * n
        prefix = 1
        for i in range(n):
            l[i] = prefix
            prefix *= nums[i]
        print(l)
        postfix = 1
        for i in range(n - 1, -1, -1):
            l[i] *= postfix
            postfix *= nums[i]
        return l









