# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        answ = []
        def rec(root):
            if not root:
                answ.append('N')
                return
            answ.append(str(root.val))
            rec(root.left)
            rec(root.right)
        rec(root)
        return ','.join(answ)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        index = 0
        def rec():
            nonlocal index
            if data[index] == 'N':
                index += 1
                return None
            Node = TreeNode(int(data[index]))
            index += 1
            Node.left = rec()
            Node.right = rec()
            return Node
        return rec()