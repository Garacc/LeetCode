class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def Dfs(i, j):
            if(0 <= i < height and 0 <= j < width and grid[i][j] == "1"):
                grid[i][j] = "0"
                #map(Dfs, list(zip((i, i + 1, i, i - 1), (j - 1, j, j + 1, j))))
                for a in list(zip((i, i+1, i, i-1), (j-1, j, j+1, j))):
                    Dfs(a[0], a[1])
                return 1
            return 0
        
        if not grid: return 0
        
        height, width = len(grid), len(grid[0])
        Num = 0
        for i in range(height):
            for j in range(width):
                Num += min(Dfs(i, j), 1)
        
        return Num

if __name__ == "__main__":
    sol = Solution()
    testcase = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
    print(sol.numIslands(testcase))