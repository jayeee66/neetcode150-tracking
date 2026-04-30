# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 
        
        while curr:
            nxt = curr.next # define a pointer point to the next node after current
            curr.next = prev # reverse the list, turn curr(head).next point to Null
            prev = curr # move prev to curr point, preparing for next change
            curr = nxt # move curr to next point
        return prev
            
            



            
        return curr