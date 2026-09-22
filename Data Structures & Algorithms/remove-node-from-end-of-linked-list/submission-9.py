# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):, no_type_check
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        left_Ptr = dummyNode
        right_Ptr = head

        while n > 0 and right_Ptr:
            right_Ptr = right_Ptr.next
            n -= 1

        while right_Ptr:
            left_Ptr = left_Ptr.next
            right_Ptr = right_Ptr.next
        left_Ptr.next = left_Ptr.next.next

        return dummyNode.next
