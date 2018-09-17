# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0: return []
        
        def node(val, left, right):
            newnode = TreeNode(val)
            newnode.left = left
            newnode.right = right
            
            return newnode
        
        def tree(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in tree(first, root - 1)
                    for right in tree(root + 1, last)] or [None]
        
        return tree(1, n)