class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i_flag, v_flag, x_flag, l_flag, c_flag, d_flag, m_flag = 1,1,1,1,1,1,1
        num = list(s)
        output = 0
        while(num):
            tmp = num.pop()
            if tmp == 'I':
                output += i_flag * 1
            elif tmp == 'V':
                output += v_flag * 5
                i_flag = -1
            elif tmp == 'X':
                output += x_flag * 10
                i_flag = -1
            elif tmp == 'L':
                output += l_flag * 50
                x_flag = -1
            elif tmp == 'C':
                output += c_flag * 100
                x_flag = -1
            elif tmp == 'D':
                output += d_flag * 500
                c_flag = -1
            elif tmp == 'M':
                output += m_flag * 1000
                c_flag = -1
        return output