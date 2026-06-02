class Node:
        def __init__(self, val, next, prev, prevMin):
            self.val = val
            self.next = next
            self.prev = prev
            self.prevMin = prevMin
        
        def delete(self) -> bool:
            if self.prev and not self.next: #delete the head
                self.prev.next = None
            return True
class MinStack:

        
    def __init__(self, head = None, tail=None, Min=None):
        self.head = None
        self.tail = None
        self.Min = None

    def push(self, val: int) -> None:
        if self.head != None: #case where stack is non empty
            newNode = Node(val, None, self.head, None)
            self.head = newNode
            if newNode.val < self.Min.val: # if we have a new min
                newNode.prevMin = self.Min
                self.Min = newNode

        else: #case where stack is empty
            newNode = Node(val, None, None, None)
            self.head = newNode
            self.tail = newNode
            self.Min = newNode
        

    def pop(self) -> None:
        if self.head.prev != None: #Node is not the last one
            if self.head == self.Min:
                self.Min = self.head.prevMin
            newHead = self.head.prev
            self.head.delete()
            self.head = newHead
        else:
            self.head = None
            self.tail = None
            self.Min = None

    def top(self) -> int:
        if self.head != None:
            return self.head.val
        else:
            return  
        

    def getMin(self) -> int:
        return self.Min.val