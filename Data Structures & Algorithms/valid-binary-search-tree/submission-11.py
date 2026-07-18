# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def rec(root,le,ri):
            if not root:
                return True
            if root.val <= le or root.val >= ri:
                return False
            left = rec(root.left,le,min(root.val,ri))
            right = rec(root.right,max(root.val,le),ri)
            if left and right:
                return True
            return False
        return rec(root,-100000,100000)