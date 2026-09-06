# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        Curr_Ptr = head

        while Curr_Ptr is not None:
            if Curr_Ptr in seen:
                return True
            seen.add(Curr_Ptr)
            Curr_Ptr = Curr_Ptr.next

        return False