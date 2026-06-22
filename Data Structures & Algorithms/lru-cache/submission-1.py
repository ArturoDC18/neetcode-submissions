class Node:
    def __init__(self, val, next = None, prev = None, key = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
class LinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def pop(self):
        key = -1
        if self.head and self.tail and self.head != self.tail:
            self.tail.prev.next = None
            key = self.tail.key
            self.tail = self.tail.prev
        elif self.head == self.tail:
            key = self.tail.key
            self.head = None
            self.tail = None
        return key
    def add(self,val):
        new = Node(val)
        if self.head:
            new.next = self.head
            self.head.prev = new
            self.head = new
        else:
            self.head = new
            self.tail = new
        return new
    def makehead(self,node):
        if node.next and node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.next and not node.prev:
            return
        elif node.prev and not node.next:
            node.prev.next = None
            self.tail = node.prev

        node.next = self.head
        node.prev = None
        self.head.prev = node
        self.head = node
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hash = {}
        self.ll = LinkedList()
        
    def get(self, key: int) -> int:
        if key in self.hash and self.hash[key] != None:
            self.ll.makehead(self.hash[key])
            return self.hash[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash and self.hash[key] != None:
            self.ll.makehead(self.hash[key])
            self.hash[key].val = value
            self.hash[key].key = key
        else:
            self.size += 1
            new = self.ll.add(value)
            new.key = key
            self.hash[key] = new
            if self.size > self.capacity:
                deletekey = self.ll.pop()
                self.hash[deletekey] = None


        
