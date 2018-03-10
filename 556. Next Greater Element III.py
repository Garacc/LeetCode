class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = list(str(n))
        flag = 0
        MAX_INT = 2147483647
        for i in reversed(range(1, len(s))):
            if s[i] > s[i-1]:
                flag = 1
                break
        if flag == 0:
            return -1
        for j in reversed(range(1, len(s))):
            if s[j] > s[i-1]:
                tmp = s[i-1]
                s[i-1] = s[j]
                s[j] = tmp
                break
        output = s[:i] + list(reversed(s[i:]))
        num = int(''.join(output))
        return num if num <= MAX_INT else -1

if __name__ == "__main__":
    n = 2
    sol = Solution()
    print(sol.nextGreaterElement(n))