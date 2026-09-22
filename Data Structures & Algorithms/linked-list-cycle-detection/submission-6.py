# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        curr_Ptr = head
        while curr_Ptr is not None:
            if curr_Ptr in seen:
                return True
            seen.add(curr_Ptr)
            curr_Ptr = curr_Ptr.next
        
        return False