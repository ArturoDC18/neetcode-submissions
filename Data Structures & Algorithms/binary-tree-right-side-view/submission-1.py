# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lista = []
        def rec(root,level):
            if not root:
                return 
            if len(lista) <= level:
                lista.append(None)
            if lista[level] == None:
                lista[level] = root.val
            rec(root.right,level+1)
            rec(root.left,level+1)
        rec(root,0)
        return lista
        