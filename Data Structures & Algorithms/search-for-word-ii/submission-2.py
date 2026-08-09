class Node:
    def __init__(self,value):
        self.value = value
        self.children = dict()
class Trie:
    def __init__(self):
        self.root = Node('*')
    def build(self,words):
        for word in words:
            node = self.root
            for char in word:
                if char in node.children:
                    node = node.children[char]
                else:
                    new = Node(char)
                    node.children[char] = new
                    node = new
            node.children['*'] = Node('*')
        


class Solution:
    def rec(self,x,y,board,meta,node):
        neighbors = []
        answ = []
        char = board[x][y]

        if char not in node.children:
            return []

        node = node.children[char]
        original = board[x][y]
        board[x][y] = '#'
        if 0<x and board[x-1][y] in node.children:
            neighbors.append((x-1,y))
        if x<len(board)-1 and board[x+1][y] in node.children:
            neighbors.append((x+1,y))
        if 0<y and board[x][y-1] in node.children:
            neighbors.append((x,y-1))
        if y<len(board[0])-1 and board[x][y+1] in node.children:
            neighbors.append((x,y+1))
        #print(f'neighbors of {node.value} are: {neighbors}')
        if '*' in node.children:
            #print(f"found word {meta}")
            answ.append(meta)
        if not neighbors:
            #print(f"original had no valid neighbors")
            board[x][y] = original
            return answ
        else:
            for neighbor in neighbors:
                nx,ny = neighbor
                answ += self.rec(nx,ny,board,meta + board[nx][ny], node)
            board[x][y] = original
            return answ
            

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        trie.build(words)
        answ = []

        for x,column in enumerate(board):
            for y,line in enumerate(column):
                lis = self.rec(x,y,board,board[x][y],trie.root)
                answ += lis
        return list(set(answ))












