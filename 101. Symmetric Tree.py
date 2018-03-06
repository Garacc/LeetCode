# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        
        def isTrue(nodel, noder):
            if not nodel and not noder: return True
            elif not nodel or not noder: return False
            else:
                return (nodel.val == noder.val) and isTrue(nodel.left, noder.right) and \
                isTrue(nodel.right, noder.left)
        
        return isTrue(root.left, root.right)