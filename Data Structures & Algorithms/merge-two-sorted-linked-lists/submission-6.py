# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        L1Curr, L2Curr = list1, list2
        CurrPtr = dummyNode

        while L1Curr and L2Curr:
            if L1Curr.val >= L2Curr.val:
                CurrPtr.next = L2Curr
                L2Curr = L2Curr.next
            else:
                CurrPtr.next = L1Curr
                L1Curr = L1Curr.next
            CurrPtr = CurrPtr.next

        while L1Curr:
            CurrPtr.next = L1Curr
            L1Curr = L1Curr.next
            CurrPtr = CurrPtr.next

        while L2Curr:
            CurrPtr.next = L2Curr
            L2Curr = L2Curr.next
            CurrPtr = CurrPtr.next

        return dummyNode.next

            
