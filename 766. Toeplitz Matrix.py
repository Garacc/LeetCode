class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if not matrix: return True
        
        h = len(matrix)
        w = len(matrix[0])
        for i in range(w):
            j = 0
            k = i
            val = matrix[j][k]
            while (j < h and k < w):
                if not val == matrix[j][k]:
                    return False
                j += 1
                k += 1
        for i in range(1, h):
            j = i
            k = 0
            val = matrix[j][k]
            while (j < h and k < w):
                if not val == matrix[j][k]:
                    return False
                j += 1
                k += 1
        return True
    
if __name__ == "__main__":
    matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    sol = Solution()
    print(sol.isToeplitzMatrix(matrix))