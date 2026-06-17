# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        node = head
        while node:
            count += 1 
            node = node.next
        to_rem = count - n
        if to_rem == 0:
            temp = head.next
            head.next = None
            return temp 
        count = 0
        node = head
        while node:
            count += 1
            if count == to_rem:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None
            node = node.next
        return head