# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None: return []
        
        nodelist = [root]
        average = []

        while(len(nodelist) > 0):
            sumnode = 0
            for node in nodelist:
                sumnode += node.val
            average.append(sumnode / len(nodelist))
            nodelist = [kid for node in nodelist for kid in (node.left, node.right) if kid]
        
        return average