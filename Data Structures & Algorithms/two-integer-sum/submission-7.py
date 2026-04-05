class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for x in range(len(nums)-1):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    l.append(x)
                    l.append(y)
                    return l
                else:
                    pass