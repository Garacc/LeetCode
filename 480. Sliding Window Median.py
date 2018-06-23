import bisect

class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        window = sorted(nums[:k])
        medians = []
        for i, addnum in enumerate(nums[k:]+[0]):
            medians.append((window[k//2] + window[(k-1)//2]) / 2.0)
            window.remove(nums[i])
            bisect.insort(window, addnum)
        
        return medians