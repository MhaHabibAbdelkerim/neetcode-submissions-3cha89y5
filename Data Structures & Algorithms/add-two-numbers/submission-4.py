# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1Curr = l1
        L2Curr = l2
        carry = 0
        dummyNode = ListNode()
        CurrPtr = dummyNode

        while L1Curr and L2Curr:
            Sum = L1Curr.val + L2Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            CurrPtr.next = ListNode(to_add)
            CurrPtr = CurrPtr.next
            L1Curr, L2Curr = L1Curr.next, L2Curr.next

        while L1Curr:
            Sum = L1Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            CurrPtr.next = ListNode(to_add)
            CurrPtr = CurrPtr.next
            L1Curr = L1Curr.next

        while L2Curr:
            Sum = L2Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            CurrPtr.next = ListNode(to_add)
            CurrPtr = CurrPtr.next
            L2Curr = L2Curr.next

        if carry:
            CurrPtr.next = ListNode(carry)

        return dummyNode.next