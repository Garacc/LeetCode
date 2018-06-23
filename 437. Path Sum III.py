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
        :rtype: int
        """
        self.count = 0
        
        def nodeDFS(node):
            if node == None:
                return []
            posvalue = []
            if node.left != None:
                posvalue += nodeDFS(node.left)
            if node.right != None:
                posvalue += nodeDFS(node.right)
            
            posvalue.append(0)
            for value in posvalue:
                if node.val + value == sum:
                    self.count += 1
            
            upvalue = [node.val + value for value in posvalue]
            return upvalue
        
        nodeDFS(root)
        return self.count