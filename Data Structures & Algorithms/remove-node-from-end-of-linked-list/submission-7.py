# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        LIST = []
        Curr_Ptr = head
        while Curr_Ptr is not None:
            LIST.append(Curr_Ptr)
            Curr_Ptr = Curr_Ptr.next

        Count = 1
        for node in range(len(LIST)-1, -1, -1):
            if Count == len(LIST):
                return head.next
                break
            elif Count != n:
                Count += 1
            else:
                LIST[node - 1].next = LIST[node].next 
                break         

        return head
            
