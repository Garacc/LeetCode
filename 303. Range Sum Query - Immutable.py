class NumArray:
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans = 0
        for idx in range(i, j + 1):
            ans += self.nums[idx]
        return ans
    TLE
    '''
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sums = nums
        for i in range(1, len(nums)):
            self.sums[i] += self.sums[i - 1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        else:
            return self.sums[j] - self.sums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)