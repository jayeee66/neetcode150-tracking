
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd Cycle
        fast = 0
        slow = 0
        # Finding the intersection point in the cycle
        while True:
            # moves 1 steps
            slow = nums[slow]
            # moves 2 steps
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # print(fast, slow)
        # Finding the entrance of the cycle (the duplicate number)
        # Reset one pointer to the start of the array
        slow = 0
        while True:
            # Move both pointers at the same speed (1 step at a time)
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:    
                return slow