class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # Use l < r because when they meet, that index is the minimum.
        while l < r:
            mid = (l + r) // 2
            # If mid element is greater than the rightmost element,
            # it means the minimum must be in the right half.
            if nums[mid] > nums[r]:
                l = mid + 1
            # If mid element is less than or equal to the rightmost element,
            # the minimum could be mid itself or to its left.
            else:
                r = mid
            # print(mid)
        # When l == r, we've narrowed it down to the minimum element.
        return nums[r]