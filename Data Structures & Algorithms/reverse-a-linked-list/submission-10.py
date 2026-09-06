# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Prev, Curr_Ptr = None, head

        while Curr_Ptr is not None:
            nxt = Curr_Ptr.next
            Curr_Ptr.next = Prev
            Prev = Curr_Ptr
            Curr_Ptr = nxt

        return Prev