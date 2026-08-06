class Node:
    def __init__(self,value,children = None):
        self.value = value
        self.children = dict()

class PrefixTree:

    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new = Node(char)
                node.children[char] = new
                node = new
        node.children['*'] = '*'


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        if '*' in node.children:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True
        
        