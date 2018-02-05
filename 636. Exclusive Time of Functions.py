class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        output = [0 for i in range(n)]
        pro_stack = []
        length = len(logs)
        now = 0
        for i in range(length):
            idx, status, time = logs[i].split(':')
            idx = int(idx)
            time = int(time)
            
            if(status == 'start'):
                if(len(pro_stack) != 0):
                    output[pro_stack[-1]] = output[pro_stack[-1]] + time - now
                pro_stack.append(idx)
                now = time
            elif(status == 'end'):
                output[pro_stack[-1]] = output[pro_stack[-1]] + time - now + 1
                pro_stack.pop(-1)
                now = time + 1
                
        return output