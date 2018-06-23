class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la, lb = len(a), len(b)
        numa = list(reversed(a))
        numb = list(reversed(b))
        ans = []
        car = 0
        if la >= lb:
            for i in range(la):
                if i < lb:
                    ans.append((int(numa[i]) + int(numb[i]) + car)%2)
                    car = (int(numa[i]) + int(numb[i]) + car)//2
                else:
                    ans.append((int(numa[i]) + car)%2)
                    car = (int(numa[i]) + car)//2
            if car:
                ans.append(1)
            
        else:
            for i in range(lb):
                if i < la:
                    ans.append((int(numa[i]) + int(numb[i]) + car)%2)
                    car = (int(numa[i]) + int(numb[i]) + car)//2
                else:
                    ans.append((int(numb[i]) + car)%2)
                    car = (int(numb[i]) + car)//2
            if car:
                ans.append(1)
        
        output = ''
        for dig in list(reversed(ans)):
            output += str(dig)
        
        return output