# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answ = 0
        def rec(root):
            nonlocal answ
            if not root:
                return 0
            left = rec(root.left)
            right = rec(root.right)
            answ = max(answ, left+right)
            return max(left,right) + 1
        rec(root)
        return answ