class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights: return 0
        
        width = len(heights)
        
        checkstack = [[-1, 0]]
        MaxRect = 0
        for i in range(width + 1):
            if(i == width):
                area = 0
            else:
                area = heights[i]
            currentColumn = [i, area]
            while(checkstack[-1][1] > area):
                currentColumn = checkstack.pop()
                currentRect = (i - currentColumn[0]) * currentColumn[1]
                if(currentRect > MaxRect):
                    MaxRect = currentRect
            checkstack.append([currentColumn[0], area])
        
        return MaxRect

if __name__ == "__main__":
    sol = Solution()
    testcase = [2,1,5,6,2,3]
    print(sol.largestRectangleArea(testcase))    