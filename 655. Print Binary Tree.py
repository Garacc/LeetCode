class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return 0
        
        def getHeight(Node):
            if not Node: return 0
            return 1 + max(getHeight(Node.left), getHeight(Node.right))
        
        height = getHeight(root)
        
        self.output = [[""] * (2 ** height - 1) for _ in range(height)]
        
        def buildTree(Node, row, left, right):
            if not Node: return
            mid = int((left + right) / 2)
            self.output[row][mid] = str(Node.val)
            buildTree(Node.left, row + 1, left, mid - 1)
            buildTree(Node.right, row + 1, mid + 1, right)
        
        buildTree(Node = root, row = 0, left = 0, right = 2 ** height - 1 - 1)
        
        return self.output