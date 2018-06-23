# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None: return False
        
        nodelist = [root]
        while(len(nodelist) > 0):
            for node in nodelist:
                if node.val == sum:
                    if node.left == None and node.right == None:
                        return True
                if node.left != None:
                    node.left.val += node.val
                if node.right != None:
                    node.right.val += node.val
                    
            nodelist = [kid for node in nodelist for kid in (node.left, node.right) if kid]
        
        return False
        