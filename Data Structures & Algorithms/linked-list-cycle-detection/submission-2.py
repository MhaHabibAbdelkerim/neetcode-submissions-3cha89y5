# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_Ptr, fast_Ptr = head, head

        while fast_Ptr and fast_Ptr.next:
            slow_Ptr, fast_Ptr = slow_Ptr.next, fast_Ptr.next.next

            if slow_Ptr == fast_Ptr:
                return True
        return False