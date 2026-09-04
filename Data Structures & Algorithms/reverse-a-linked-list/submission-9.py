# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev, Current_Ptr = None, head

        while Current_Ptr:
            nxt = Current_Ptr.next
            Current_Ptr.next = Prev
            Prev = Current_Ptr
            Current_Ptr = nxt

        return Prev