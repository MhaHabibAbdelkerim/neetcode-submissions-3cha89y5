# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ARRAY = []

        Curr_Ptr = head
        while Curr_Ptr is not None:
            ARRAY.append(Curr_Ptr)
            Curr_Ptr = Curr_Ptr.next

        COUNT = 1
        for listnode in range(len(ARRAY)-1, -1, -1):
            if COUNT == len(ARRAY):
                return head.next
            elif COUNT != n:
                COUNT += 1
            else:
                ARRAY[listnode - 1].next = ARRAY[listnode].next
                break
        
        return head