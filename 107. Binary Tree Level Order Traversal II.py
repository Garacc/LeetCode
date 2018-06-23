# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        checknode = [root]
        nodelist = []
        while (len(checknode) > 0):
            nodelist.append([node.val for node in checknode])
            checknode = [kid for node in checknode for kid in (node.left, node.right) if kid]
            
        return nodelist[::-1]