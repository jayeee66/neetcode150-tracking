# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two Pointer
        # Set dummy, let left pointer to 0
        # Right pointer to head
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # Right pointer go first and stop at n
        while n > 0:
            right = right.next
            n -= 1

        # Left and Right pointer go together, 
        # and left one will stop right before the target node
        while right:
            left = left.next
            right = right.next
        # delete target node
        left.next =left.next.next

        return dummy.next