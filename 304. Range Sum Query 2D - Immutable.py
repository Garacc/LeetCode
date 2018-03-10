class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matsum = matrix
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                self.matsum[i][j] += self.matsum[i][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ans = 0
        for i in range(row1, row2+1):
            if col1 == 0:
                ans += self.matsum[i][col2]
            else:
                ans += self.matsum[i][col2] - self.matsum[i][col1-1]
        return ans
            
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)