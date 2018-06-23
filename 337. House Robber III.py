# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def robNode(node):
            if node == None:
                return 0
            else:
                if node.left == None and node.right == None:
                    return node.val
                elif node.left == None:
                    return max(node.val + robNode(node.right.left) + robNode(node.right.right), \
                           robNode(node.right))
                elif node.right == None:
                    return max(node.val + robNode(node.left.left) + robNode(node.left.right), \
                           robNode(node.left))
                else:
                    return max(node.val + robNode(node.left.left) + robNode(node.left.right) \
                           + robNode(node.right.left) + robNode(node.right.right), \
                           robNode(node.left)+robNode(node.right))
        
        return robNode(root)
TLE
'''
class Solution(object):
    def rob(self, root):
        return self.robDFS(root)[1]
    def robDFS(self,node):
        if node is None:
            return (0,0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))