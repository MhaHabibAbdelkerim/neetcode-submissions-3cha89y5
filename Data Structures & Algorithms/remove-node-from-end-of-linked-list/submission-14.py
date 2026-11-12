# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        List_LinkedList = []

        CurrPtr = head
        while CurrPtr is not None:
            List_LinkedList.append(CurrPtr)
            CurrPtr = CurrPtr.next

        if len(List_LinkedList) == n:
            return head.next

        COUNT = 1
        for node in range(len(List_LinkedList)-1, -1, -1):
            if COUNT == n:
                List_LinkedList[node - 1].next = List_LinkedList[node].next
                break
            else:
                COUNT += 1

        return head