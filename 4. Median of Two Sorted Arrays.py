class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m < n:
            nums1, nums2, m, n = nums2, nums1, n, m
        if n == 0 and m == 0:
            return 0.0
        elif n == 0:
            if m % 2 == 1:
                return nums1[m//2] * 1.0
            else:
                return (nums1[m//2 - 1] + nums1[m//2]) / 2
        
        i_min, i_max = 0, n
        half = (m + n + 1) // 2
        while i_min <= i_max:
            i = (i_min + i_max) // 2
            j = half - i
            if i < n and nums1[j-1] > nums2[i]:
                i_min = i + 1
            elif i > 0 and nums1[j] < nums2[i-1]:
                i_max = i - 1
            else:
                if i == 0: maxleft = nums1[j-1]
                elif j == 0: maxleft = nums2[i-1]
                else:
                    maxleft = max(nums1[j-1], nums2[i-1])
                if (m + n)%2 == 1:
                    return maxleft * 1.0
                if i == n: minright = nums1[j]
                elif j == m: minright = nums2[i]
                else:
                    minright = min(nums1[j], nums2[i])
                    
                return (maxleft + minright) / 2.0

if __name__ == "__main__":
    a = []
    b = []
    sol = Solution()
    print(sol.findMedianSortedArrays(a, b))