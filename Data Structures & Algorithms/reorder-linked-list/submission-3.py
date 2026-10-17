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
        second_half = slow_Ptr.next
        slow_Ptr.next = None

        #second: we want to reverse the secondhalf of the linkedlist
        Curr_Ptr, Prev = second_half, None
        while Curr_Ptr is not None:
            nxt = Curr_Ptr.next
            Curr_Ptr.next = Prev
            Prev = Curr_Ptr
            Curr_Ptr = nxt

        #third: merge the two halves together
        CurrPtr, second_half = head, Prev
        while second_half is not None:
            fh_nxt = CurrPtr.next
            sf_nxt = second_half.next
            CurrPtr.next = second_half
            second_half.next = fh_nxt
            CurrPtr, second_half = fh_nxt, sf_nxt


