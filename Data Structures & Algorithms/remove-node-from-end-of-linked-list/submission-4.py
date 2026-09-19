# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

      # Reverse the list
      CurrPtr, Prev = head, None
      while CurrPtr is not None:
        nxt = CurrPtr.next
        CurrPtr.next = Prev
        Prev = CurrPtr
        CurrPtr = nxt
      last = Prev
      Final_last = last

      # Find the nth node from linkedList_end
      count, TEMP = 1, None
      while last is not None:
        if count == n:
            if TEMP == None: Final_last = last.next
            else: TEMP.next = last.next
            break
    
        TEMP = last
        last = last.next
        count += 1

      # Reverse the list back
      NEXT = None
      while Final_last is not None:
        prev = Final_last.next
        Final_last.next = NEXT
        NEXT = Final_last
        Final_last = prev

      return NEXT
        