class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None
        

class NumArray(object):

    '''
    Trickery Answer
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])
    '''
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        def creatTree(nums, l, r):
            if l > r:
                return None
            if l == r:
                node = Node(l, r)
                node.sum = nums[l]
                return node
            
            mid = (l + r) // 2
            root = Node(l, r)
            root.left = creatTree(nums, l, mid)
            root.right = creatTree(nums, mid+1, r)
            root.sum = root.left.sum + root.right.sum
            
            return root
        
        self.root = creatTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def updateVal(node, i, val):
            if node.start == node.end:
                node.sum = val
                return
            
            mid = (node.start + node.end) // 2
            if i <= mid:
                updateVal(node.left, i, val)
            else:
                updateVal(node.right, i, val)
            
            node.sum = node.left.sum + node.right.sum
            return
        
        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def rangeSum(node, i, j):
            if node.start == i and node.end == j:
                return node.sum
            
            mid = (node.start + node.end) // 2
            if j <= mid:
                return rangeSum(node.left, i, j)
            if i >= mid + 1:
                return rangeSum(node.right, i, j)
            else:
                return rangeSum(node.left, i, mid) + rangeSum(node.right, mid+1, j)
        
        return rangeSum(self.root, i, j)
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
            
if __name__ == "__main__":
    obj = NumArray([1,3,5])
    param_1 = obj.sumRange(0,2)
    obj.update(1,2)
    param_2 = obj.sumRange(0,2)