class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = list(reversed(digits))
        car = 1
        for i in range(len(res)):
            if res[i] + car > 9:
                res[i] = 0
                car = 1
            else:
                res[i] += car
                car = 0
        
        if car == 1:
            res.append(1)
        ans = list(reversed(res))
        
        return ans