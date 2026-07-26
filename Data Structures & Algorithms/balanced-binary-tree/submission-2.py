# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec(root,depth):
            if not root:
                return True,depth
            bol,left = rec(root.left, depth+1)
            bor,right = rec(root.right, depth+1)
            if abs(left - right) > 1:
                return False, 0
            return (bol and bor), max(left,right)
        return rec(root,0)[0]
                

        