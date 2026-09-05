# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        L1_Ptr, L2_Ptr = l1, l2
        carry = 0
        dummyNode = ListNode()
        Current = dummyNode

        while L1_Ptr and L2_Ptr:
            Sum = L1_Ptr.val + L2_Ptr.val + carry
            To_add = Sum % 10
            carry = Sum // 10
            Current.next = ListNode(To_add)
            L1_Ptr = L1_Ptr.next
            L2_Ptr = L2_Ptr.next
            Current = Current.next

        while L1_Ptr:
            Sum = L1_Ptr.val + carry
            To_add = Sum % 10
            carry = Sum // 10
            Current.next = ListNode(To_add)
            L1_Ptr = L1_Ptr.next
            Current = Current.next

        while L2_Ptr:
            Sum = L2_Ptr.val + carry
            To_add = Sum % 10
            carry = Sum // 10
            Current.next = ListNode(To_add)
            L2_Ptr = L2_Ptr.next
            Current = Current.next

        if carry != 0:
                Current.next = ListNode(carry)

        return dummyNode.next
        

            

        

            


