# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        node = head
        array = []
        while node:
            count += 1 
            array.append(node)
            node = node.next
        to_rem = count - n

        if len(array) == 1 and n == 1:
            return None
        elif to_rem == 0:
            array[0].next = None
            return array[1]
        if len(array)-1 >= to_rem +1:
            array[to_rem - 1].next = array[to_rem + 1]
            return head
        else:
            array[to_rem - 1].next = None
            return head