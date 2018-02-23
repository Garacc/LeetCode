class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        part = [p for p in path.split('/') if p != '.' and p != '']
        stack = []
        for p in part:
            if p == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return '/' + '/'.join(stack)