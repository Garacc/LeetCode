class Solution:
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        ismatch = [[0 for _ in range((len(B) + 1))] for _ in range((len(A) + 1))]
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    ismatch[i][j] = ismatch[i - 1][j - 1] + 1
        return max(max(row) for row in ismatch)

if __name__ == '__main__':
    sol = Solution()
    A = [1,2,3,2,1]
    B = [3,2,1,4,7]
    print(sol.findLength(A, B))