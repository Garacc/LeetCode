# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxPath = []
        
        def nodeDFS(node):
            if node == None:
                 return 0
            
            lpath = nodeDFS(node.left)
            rpath = nodeDFS(node.right)
            
            maxPath.append(max(node.val + lpath + rpath, node.val, node.val + lpath, node.val + rpath))
            
            newpath = max(node.val, node.val + lpath, node.val + rpath)
            return newpath
        
        nodeDFS(root)
        
        return max(maxPath)