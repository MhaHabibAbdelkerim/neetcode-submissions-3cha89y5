# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        Current = dummyNode

        L1Curr, L2Curr = list1, list2

        while L1Curr and L2Curr:
            if L1Curr.val >= L2Curr.val:
                Current.next = L2Curr
                L2Curr = L2Curr.next
                Current = Current.next
            else:
                Current.next = L1Curr
                L1Curr = L1Curr.next
                Current = Current.next

        while L1Curr:
            Current.next = L1Curr
            L1Curr = L1Curr.next
            Current = Current.next

        while L2Curr:
            Current.next = L2Curr
            L2Curr = L2Curr.next
            Current = Current.next

        return dummyNode.next