# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        if len(inorder) == 1:
            return TreeNode(preorder[0])
        for i,val in enumerate(inorder):
            if val == preorder[0]:
                break
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:i+1],inorder[0:i])
        root.right = self.buildTree(preorder[i+1:],inorder[i+1:])
        return root
