# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def rec(root,maxim):
            if not root:
                return 0,maxim
            left = rec(root.left,maxim)
            right = rec(root.right,maxim)
            maxim[0] = max(maxim[0], left[0]+right[0])
            return max(left[0],right[0]) + 1,maxim
        
        return rec(root,[0])[1][0]