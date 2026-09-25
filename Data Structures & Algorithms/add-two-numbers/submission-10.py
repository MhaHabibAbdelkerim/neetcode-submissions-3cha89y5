# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        L1Curr, L2Curr = l1, l2
        dummyNode = ListNode()
        Curr_Ptr = dummyNode

        while L1Curr and L2Curr:
            Sum = L1Curr.val + L2Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            Curr_Ptr.next = ListNode(to_add)
            Curr_Ptr = Curr_Ptr.next
            L1Curr, L2Curr = L1Curr.next, L2Curr.next

        while L1Curr:
            Sum = L1Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            Curr_Ptr.next = ListNode(to_add)
            Curr_Ptr = Curr_Ptr.next
            L1Curr = L1Curr.next

        while L2Curr:
            Sum = L2Curr.val + carry
            to_add = Sum % 10
            carry = Sum // 10
            Curr_Ptr.next = ListNode(to_add)
            Curr_Ptr = Curr_Ptr.next
            L2Curr = L2Curr.next

        if carry: Curr_Ptr.next = ListNode(carry)

        return dummyNode.next
