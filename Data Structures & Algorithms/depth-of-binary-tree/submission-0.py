# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def rec(root, num):
            if not root:
                return num
            num += 1
            lef= rec(root.left,num)
            righ = rec(root.right,num)
            return max(lef,righ)
        return rec(root,0)
        
        