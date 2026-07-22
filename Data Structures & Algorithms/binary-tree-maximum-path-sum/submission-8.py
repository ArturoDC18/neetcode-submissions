# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        gmax = -1000
        def rec(root):
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            left = max(left, 0)
            right = max(right, 0)
            nonlocal gmax
            gmax = max(gmax, root.val + max(left,right), root.val+left+right)
            return root.val + max(left,right)
        rec(root)
        return gmax
