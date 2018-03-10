class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        
        nummap = ["" for _ in range(numRows)]
        flag = 1
        poi = 0
        for i in range(len(s)):
            nummap[poi] += s[i]
            if poi == 0:
                flag = 1
            elif poi == numRows - 1:
                flag = -1
            poi += flag
        output = ""
        for row in nummap:
            output += row
        return output

if __name__ == "__main__":
    testcase = "ABABAB"
    sol = Solution()
    print(sol.convert(testcase, 2))