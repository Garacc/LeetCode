class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        
        height = len(matrix)
        width = len(matrix[0])
        
        square = [[0] * width for _ in range(height)]
        
        maxSquare = 0
        for i in range(height):
            square[i][0] = int(matrix[i][0])
            maxSquare = max(maxSquare, square[i][0])
        for j in range(width):
            square[0][j] = int(matrix[0][j])
            maxSquare = max(maxSquare, square[0][j])
        for i in range(1, height):
            for j in range(1, width):
                if(matrix[i][j] == '1'):
                    square[i][j] = min(square[i - 1][j - 1], 
                          min(square[i - 1][j], square[i][j - 1])) + 1
                    maxSquare = max(maxSquare, square[i][j])
        
        return maxSquare ** 2
        
        
    
if __name__ == "__main__":
    sol = Solution()
    testcase = [["1"]]
    print(sol.maximalSquare(testcase))