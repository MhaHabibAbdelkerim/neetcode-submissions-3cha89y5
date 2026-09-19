# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        CurrPtr = dummyNode
        right_Ptr = head

        while n > 0 and right_Ptr:
            right_Ptr = right_Ptr.next
            n -= 1

        while right_Ptr:
            CurrPtr = CurrPtr.next
            right_Ptr = right_Ptr.next
        
        CurrPtr.next = CurrPtr.next.next
        return dummyNode.next
            

