class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minsumnum = len(nums) + 1
        tmpsum = 0
        start = 0
        for i, num in enumerate(nums):
            tmpsum += num
            while tmpsum >= s:
                minsumnum = min(minsumnum, i - start + 1)
                tmpsum -= nums[start]
                start += 1
        return minsumnum if minsumnum <= len(nums) else 0
    
if __name__ == '__main__':
    sol = Solution()
    s = 11
    nums = [1,2,3,4,5]
    print(sol.minSubArrayLen(s, nums))