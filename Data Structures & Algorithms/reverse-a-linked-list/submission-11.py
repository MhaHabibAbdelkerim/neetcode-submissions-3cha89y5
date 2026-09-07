# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        CurrPtr, Prev = head, None

        while CurrPtr is not None:
            nxt = CurrPtr.next
            CurrPtr.next = Prev
            Prev = CurrPtr
            CurrPtr = nxt

        return Prev