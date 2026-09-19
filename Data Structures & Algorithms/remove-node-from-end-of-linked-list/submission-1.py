# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummyNode = ListNode()
        Curr = dummyNode
        LIST, count = [], 1
        CurrPtr = head
        while CurrPtr is not None:
            LIST.append(CurrPtr)
            CurrPtr = CurrPtr.next

        if n == len(LIST): return head.next

        for node in range(len(LIST)-1, -1, -1):
            if count != n: count += 1
            else: 
                LIST[node - 1].next = LIST[node].next
                break
        
        return head


        