# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            cur_idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[cur_idx])
            root.left = self.buildTree(preorder, inorder[:cur_idx])
            root.right = self.buildTree(preorder, inorder[cur_idx+1:])
            return root