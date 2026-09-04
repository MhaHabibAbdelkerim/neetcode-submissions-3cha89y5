# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_ptr, current_ptr = None, head

        while current_ptr is not None:
            nxt = current_ptr.next
            current_ptr.next = prev_ptr
            prev_ptr = current_ptr
            current_ptr = nxt

        return prev_ptr
