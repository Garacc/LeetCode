class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root: return False
        bfs, s = [root], set()
        for node in bfs:
            if k - node.val in s: return True
            s.add(node.val)
            if node.left: bfs.append(node.left)
            if node.right: bfs.append(node.right)
        return False