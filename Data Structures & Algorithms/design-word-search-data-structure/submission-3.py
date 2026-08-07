class Node:
    def __init__(self,value):
        self.value = value
        self.children = dict()

class WordDictionary:

    def __init__(self):
        self.root = Node('*')
        self.activeNodes = []

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new = Node(char)
                node.children[char] = new
                node = new
        node.children['*'] = Node('*') 
        

    def search(self, word: str) -> bool:
        #print("searching word: ",word)
        self.activeNodes.append(self.root)
        for char in word:
            nextActive = []
            for node in self.activeNodes:
                #print('processing node: ',node.value)
                if char == '.':
                    for key,child in node.children.items():
                        nextActive.append(child)
                else:
                    if char in node.children:
                        #print('found match in children')
                        nextActive.append(node.children[char])
            self.activeNodes = nextActive
            if not self.activeNodes:
                #print('No active nodes, returning False')
                self.activeNodes = [self.root]
                return False
        for node in self.activeNodes:
            if '*' in node.children:
                #print("conclusive word FOUND, returning True")
                self.activeNodes = [self.root]
                return True
        #print("Not conclusive word found")
        self.activeNodes = [self.root]
        return False
        

        
