# Two Pointer
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            # Prevent two duplicate numbers
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            # To prevent left index passing right index, it's important
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if three_sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    # Make sure the left index won't count again
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    l += 1

        return res
