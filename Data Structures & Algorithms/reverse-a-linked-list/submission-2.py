# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        next = None
        while cur and cur.next != None:
            NewNode = ListNode(val = cur.val) # copy node
            NewNode.next = next # assign next in reverse order (from prev iteration)
            next = NewNode # assign next for following iteration
            cur = cur.next
        if cur: 
            cur.next = next
        return cur

        