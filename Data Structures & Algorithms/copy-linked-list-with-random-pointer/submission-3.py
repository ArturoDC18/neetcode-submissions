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
        old2new = {}
        node = head
        while node:
            old2new[node] = Node(node.val)
            node = node.next
        
        node = head
        while node: 
            if node.next:
                old2new[node].next = old2new[node.next]
            else:
                old2new[node].next = None
            if node.random:
                old2new[node].random = old2new[node.random]
            else:
                old2new[node].random = None
            node = node.next
        if head:
            return old2new[head]
        else:
            return None

        