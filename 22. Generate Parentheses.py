class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """        
        def generate(left, right, part, parens = []):
            if left: generate(left-1, right, part+'(')
            if right > left: generate(left, right-1, part+')')
            if not right: parens.append(part)
            return parens
        
        return generate(n, n, '')

    
if __name__ == "__main__":
    n = 3
    sol = Solution()
    print(sol.generateParenthesis(3))