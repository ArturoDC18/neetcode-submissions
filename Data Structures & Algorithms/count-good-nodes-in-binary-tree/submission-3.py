# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def rec(root,maxim):
            if not root:
                return 
            nonlocal count
            if root.val >= maxim:
                print(root.val)
                maxim = max(root.val,maxim)
                count += 1
            rec(root.left,maxim)
            rec(root.right,maxim)
        rec(root,root.val)
        return count
        