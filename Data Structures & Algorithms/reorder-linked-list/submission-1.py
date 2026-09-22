# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the middlepoint
        slow_Ptr, fast_Ptr = head, head
        while fast_Ptr and fast_Ptr.next:
            slow_Ptr = slow_Ptr.next
            fast_Ptr = fast_Ptr.next.next
        second_part = slow_Ptr.next
        slow_Ptr.next = None

        # Reverse the second half of the list
        Prev = None
        while second_part:
            nxt = second_part.next
            second_part.next = Prev
            Prev = second_part
            second_part = nxt

        # merge the two halves
        first, second = head, Prev
        while second is not None:
            Fnxt = first.next
            Snxt = second.next
            first.next = second
            second.next = Fnxt
            first = Fnxt
            second = Snxt
        
        



        
