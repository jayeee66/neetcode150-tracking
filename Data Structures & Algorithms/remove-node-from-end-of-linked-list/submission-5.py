# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 1
        curr = head
        l = 0
        # Count the length first
        while curr:
            curr = curr.next
            l += 1

        # edge case: prevent no prev node to operate
        remove = l - n + 1
        if remove == 1:
            return head.next

        # Traverse stop before the target node
        curr = head
        for i in range(remove - 2):
            curr = curr.next
        # print(curr.val)
        # Delete the target node
        curr.next = curr.next.next

        return head