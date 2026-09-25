# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        L1Curr, L2Curr = list1, list2
        dummyNode = ListNode()
        Curr_Ptr = dummyNode

        while L1Curr and L2Curr:
            if L1Curr.val >= L2Curr.val:
                Curr_Ptr.next = L2Curr
                L2Curr = L2Curr.next
            else:
                Curr_Ptr.next = L1Curr
                L1Curr = L1Curr.next
            Curr_Ptr = Curr_Ptr.next

        if L1Curr:
            Curr_Ptr.next = L1Curr
        elif L2Curr:
            Curr_Ptr.next = L2Curr

        return dummyNode.next