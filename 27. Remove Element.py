class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        valnums = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[valnums] = nums[valnums], nums[i]
                valnums += 1
        return valnums