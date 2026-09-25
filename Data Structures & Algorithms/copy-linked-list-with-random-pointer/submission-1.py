"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        To_Copy = { None : None}

        curr_Ptr = head
        while curr_Ptr:
            copy = Node(curr_Ptr.val)
            To_Copy[curr_Ptr] = copy
            curr_Ptr = curr_Ptr.next

        curr_Ptr = head
        while curr_Ptr:
            copy = To_Copy[curr_Ptr]
            copy.next = To_Copy[curr_Ptr.next]
            copy.random = To_Copy[curr_Ptr.random]
            curr_Ptr = curr_Ptr.next

        return To_Copy[head]

            

        