# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #  Initialize a dummy node to store new nodes
        # 'curr' will be used to build the new list node by node
        dummy = ListNode(0)
        curr = dummy
        # 'carry' stores the value (1 or 0) to be added to the next higher digit
        carry = 0
        # Iterate as long as there are nodes in l1 OR l2, OR a remaining carry
        while l1 or l2 or carry:
            # Get values from current nodes; if a list has ended, use 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # Calculate the sum of the digits and the carry
            val = v1 + v2 + carry
            carry = val // 10    # Get the tens digit (e.g., 1 from 13)
            digit = val % 10     # Get the ones digit (e.g., 3 from 13)

            curr.next = ListNode(digit)
            # Move the pointers
            curr = curr.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        return dummy.next


