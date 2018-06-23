class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        la, lb = len(num1), len(num2)
        numa = list(reversed(num1))
        numb = list(reversed(num2))
        ans = []
        car = 0
        if la >= lb:
            for i in range(la):
                if i < lb:
                    ans.append((int(numa[i]) + int(numb[i]) + car)%10)
                    car = (int(numa[i]) + int(numb[i]) + car)//10
                else:
                    ans.append((int(numa[i]) + car)%10)
                    car = (int(numa[i]) + car)//10
            if car:
                ans.append(1)
            
        else:
            for i in range(lb):
                if i < la:
                    ans.append((int(numa[i]) + int(numb[i]) + car)%10)
                    car = (int(numa[i]) + int(numb[i]) + car)//10
                else:
                    ans.append((int(numb[i]) + car)%10)
                    car = (int(numb[i]) + car)//10
            if car:
                ans.append(1)
        
        output = ''
        for dig in list(reversed(ans)):
            output += str(dig)
        
        return output