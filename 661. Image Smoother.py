class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not M: return 0
        
        w, h = len(M[0]), len(M)
        output = [[0] * w for _ in range(h)]
        
        if w < 2 or h < 2:
            if w == 1 and h == 1:
                return M
            if w == 1 and h > 1:
                for i in range(h):
                    if i == 0:
                        output[i][0] = (M[i][0]+M[i+1][0])//2
                    elif i == h - 1:
                        output[i][0] = (M[i][0]+M[i-1][0])//2
                    else:
                        output[i][0] = (M[i-1][0]+M[i][0]+M[i+1][0])//3
                
                return output
            if w > 1 and h == 1:
                for j in range(w):
                    if j == 0:
                        output[0][j] = (M[0][j]+M[0][j+1])//2
                    elif j == w - 1:
                        output[0][j] = (M[0][j]+M[0][j-1])//2
                    else:
                        output[0][j] = (M[0][j-1]+M[0][j]+M[0][j+1])//3
                
                return output
        
        for i in range(h):
            for j in range(w):
                if 0 < i < h - 1 and 0 < j < w - 1:
                    output[i][j] = (M[i-1][j-1]+M[i][j-1]+M[i+1][j-1]\
                          +M[i-1][j]+M[i][j]+M[i+1][j]+M[i-1][j+1]\
                          +M[i][j+1]+M[i+1][j+1])//9
                elif i == 0 and 0 < j < w - 1:
                    output[i][j] = (M[i][j-1]+M[i][j]+M[i][j+1]\
                          +M[i+1][j-1]+M[i+1][j]+M[i+1][j+1])//6
                elif i == h - 1 and 0 < j < w - 1:
                    output[i][j] = (M[i-1][j-1]+M[i-1][j]+M[i-1][j+1]\
                          +M[i][j-1]+M[i][j]+M[i][j+1])//6
                elif 0 < i < h - 1 and j == 0:
                    output[i][j] = (M[i-1][j]+M[i][j]+M[i+1][j]\
                          +M[i-1][j+1]+M[i][j+1]+M[i+1][j+1])//6
                elif 0 < i < h - 1 and j == w - 1:
                    output[i][j] = (M[i-1][j-1]+M[i][j-1]+M[i+1][j-1]\
                          +M[i-1][j]+M[i][j]+M[i+1][j])//6
                elif i == 0 and j == 0:
                    output[i][j] = (M[i][j]+M[i+1][j]+M[i][j+1]+M[i+1][j+1])//4
                elif i == h - 1 and j == 0:
                    output[i][j] = (M[i][j]+M[i-1][j]+M[i][j+1]+M[i-1][j+1])//4
                elif i == 0 and j == w - 1:
                    output[i][j] = (M[i][j]+M[i+1][j]+M[i][j-1]+M[i+1][j-1])//4
                elif i == h - 1 and j == w - 1:
                    output[i][j] = (M[i][j]+M[i-1][j]+M[i][j-1]+M[i-1][j-1])//4
                else:
                    continue
        return output

if __name__ == "__main__":
    sol = Solution()
    testcase = [[1,2,1],[1,0,1],[3,1,1]]
    print(sol.imageSmoother(testcase))