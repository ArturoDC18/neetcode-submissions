# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, node: Optional[ListNode]) -> Optional[ListNode]:
        if not node:
            return None
        newHead = node
        if node.next:
            newHead = self.reverseList(node.next)
            node.next.next = node
        node.next = None
        return newHead

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        second = self.reverseList(second)
        
        first = head
        while second and first:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
            
            


            
        

