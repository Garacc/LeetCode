class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        output = []
        for num in nums1:
            idx = nums2.index(num)
            flag = 0
            for i in range(idx+1, len(nums2)):
                if nums2[i] > num:
                    output.append(nums2[i])
                    flag = 1
                    break
            if not flag: output.append(-1)
        
        return output
                    
            