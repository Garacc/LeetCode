class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if not stack: return False
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            elif char == ']':
                if not stack: return False
                if stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            elif char == '}':
                if not stack: return False
                if stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return True if not stack else False