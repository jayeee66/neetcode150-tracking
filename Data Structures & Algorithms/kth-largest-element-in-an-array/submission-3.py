# optimal
# Quick Select
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        index = len(nums) - k # Index of the kth largest element
        def quickSelect(targetNums, target):
            # Choose pivot in random
            pivot = random.choice(targetNums)
            
            left = [x for x in targetNums if x < pivot]
            mid = [x for x in targetNums if x == pivot]
            right = [x for x in targetNums if x > pivot]

            if target < len(left):
                return quickSelect(left, target)
            elif target < len(left) + len(mid):
                return pivot
            else:
                newTarget = target - len(left) - len(mid)
                return quickSelect(right, newTarget)
        return quickSelect(nums, index)
