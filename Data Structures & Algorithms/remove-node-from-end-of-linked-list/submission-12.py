# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        Array_LinkedList = []

        CurrPtr = head
        while CurrPtr is not None:
            Array_LinkedList.append(CurrPtr)
            CurrPtr = CurrPtr.next
        
        count = 1
        for listnode in range(len(Array_LinkedList)-1, -1, -1):
            if n == len(Array_LinkedList):
                return head.next
            elif count != n:
                count += 1
            else:
                Array_LinkedList[listnode - 1].next = Array_LinkedList[listnode].next
                break
        
        return head
        
