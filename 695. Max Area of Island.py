class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def Dfs(i, j):
            if(0 <= i < height and 0 <= j < width and grid[i][j]):
                grid[i][j] = 0
                return 1 + Dfs(i - 1, j) + Dfs(i, j - 1) + Dfs(i + 1, j) + Dfs(i, j + 1)
            return 0
        
        if not grid: return 0
        
        height, width = len(grid), len(grid[0])
        maxArea = 0
        for i in range(height):
            for j in range(width):
                maxArea = max(Dfs(i, j), maxArea)
        
        return maxArea

if __name__ == "__main__":
    sol = Solution()
    testcase = [[0,1,1,1,0],
                [0,1,0,1,0],
                [1,0,0,0,1],
                [1,1,1,1,1]]
    print(sol.maxAreaOfIsland(testcase))