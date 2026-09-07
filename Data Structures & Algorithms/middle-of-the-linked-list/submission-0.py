# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow_Ptr, fast_Ptr = head, head

        while fast_Ptr and fast_Ptr.next:
            slow_Ptr, fast_Ptr = slow_Ptr.next, fast_Ptr.next.next
        return slow_Ptr