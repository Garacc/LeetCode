class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def getMaxRect(idx, width):
            checkstack = [[-1, 0]]
            MaxRect = 0
            for i in range(width + 1):
                if(i == width):
                    area = 0
                else:
                    area = self.square[idx][i]
                currentColumn = [i, area]
                while(checkstack[-1][1] > area):
                    currentColumn = checkstack.pop()
                    currentRect = (i - currentColumn[0]) * currentColumn[1]
                    if(currentRect > MaxRect):
                        MaxRect = currentRect
                checkstack.append([currentColumn[0], area])
            
            return MaxRect
        
        if not matrix: return 0
        
        height = len(matrix)
        width = len(matrix[0])
        
        self.square = [[0] * width for _ in range(height)]
        
        for i in range(height):
            for j in range(width):
                self.square[i][j] = int(matrix[i][j])
        
        for i in range(1, height):
            for j in range(width):
                if(self.square[i][j]):
                    self.square[i][j] += self.square[i - 1][j]
        
        self.maxRectangle = 0
        
        for i in range(height):
            self.maxRectangle = max(self.maxRectangle, getMaxRect(i, width))
            
        return self.maxRectangle
    
    
if __name__ == "__main__":
    sol = Solution()
    testcase = [["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
    print(sol.maximalRectangle(testcase))    
    
    

                