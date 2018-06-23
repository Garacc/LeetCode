class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            newnode = TreeNode(v)
            newnode.left = root
            return newnode
        
        level = 1
        nodelist = [root]
        while (level < d - 1):
            if len(nodelist) > 0:
                nodelist = [kid for node in nodelist for kid in (node.left, node.right) if kid]
                level += 1
                continue
            else:
                return root
        
        for node in nodelist:
            newnodeleft = TreeNode(v)
            node.left, node.left.left = newnodeleft, node.left
            
            newnoderight = TreeNode(v)
            node.right, node.right.right = newnoderight, node.right
        
        return root
    
