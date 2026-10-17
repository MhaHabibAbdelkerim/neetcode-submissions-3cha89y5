# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        #first: we gotta find the middle of the linkedlist
        slow_Ptr, fast_Ptr = head, head
        while fast_Ptr and fast_Ptr.next:
            slow_Ptr, fast_Ptr = slow_Ptr.next, fast_Ptr.next.next
        second_part = slow_Ptr.next
        slow_Ptr.next = None

        #second: reverse the second half of the linkedlist
        Curr_Ptr, Prev = second_part, None
        while Curr_Ptr is not None:
            nxt = Curr_Ptr.next
            Curr_Ptr.next = Prev
            Prev = Curr_Ptr
            Curr_Ptr = nxt
        Last = Prev

        #third: merge the two halves together
        Curr_Ptr = head
        while Last is not None:
            fh_nxt, sh_nxt = Curr_Ptr.next, Last.next
            Curr_Ptr.next = Last
            Last.next = fh_nxt
            Curr_Ptr, Last = fh_nxt, sh_nxt
    