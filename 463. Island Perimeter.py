import operator

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(sum(map(operator.ne, [0] + row, row + [0])) 
                   for row in (grid + list(map(list, zip(*grid)))))
                       
if __name__ == "__main__":  
    
    sol = Solution()
    testcase = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(sol.islandPerimeter(testcase))

