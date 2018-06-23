class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cur, ans = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                cur += 1
                ans += cur
            else:
                cur = 0
                
        return ans
    
if __name__ == "__main__":
    A = [1,2,3,4,6]
    sol = Solution()
    print(sol.numberOfArithmeticSlices(A))