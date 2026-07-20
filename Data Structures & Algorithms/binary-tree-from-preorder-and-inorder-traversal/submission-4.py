# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        find = defaultdict(int)
        for i, val in enumerate(inorder):
            find[val] = i
        pp = 0
        def rec(l,r):
            if l > r:
                return None
            nonlocal pp
            root = TreeNode(preorder[pp])
            pp += 1
            mid = find[root.val]
            root.left = rec(l,mid-1)
            root.right = rec(mid+1,r)
            return root
        return rec(0,len(inorder)-1)