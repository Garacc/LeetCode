# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None: return []
        if root.left == None and root.right == None:
            if sum == root.val:    
                return [[root.val]]
            else:
                return []
        
        nextlevel = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        
        return [[root.val] + path for path in nextlevel]