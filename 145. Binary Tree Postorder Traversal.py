# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        
        self.output = []
        
        def iterator(node):
            if node.left:
                iterator(node.left)
            if node.right:
                iterator(node.right)
            self.output.append(node.val)
        
        iterator(root)
        return self.output