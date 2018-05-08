class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = set()
        for i in range(len(nums)):
            if nums[i] not in visited:
                nums[i], nums[len(visited)] = nums[len(visited)], nums[i]
                visited.add(nums[len(visited)])
                
        return len(visited)
if __name__ == "__main__":
    testcase = [1,1,2]
    sol = Solution()
    print(sol.removeDuplicates(testcase))