import re

class Solution:
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        if code == '': return False
        code = re.sub(r'<!\[CDATA\[.*?\]\]>', '.', code)
        check = ''
        while code != check:
            check = code
            code = re.sub(r'<([A-Z]{1,9})>[^<]*</\1>', ',', code)
        return code == ','
    
if __name__ == "__main__":
    testcase = "<DIV>>><<<<<<![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"
    sol = Solution()
    print(sol.isValid(testcase))