class Solution:
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return 'Zero'
        numdict = {1:'One', 2:'Two', 3:'Three', 4:'Four',\
                   5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine',\
                   10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',\
                   14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen',\
                   18:'Eighteen', 19:'Nineteen', 20:'Twenty', 30:'Thirty',\
                   40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy',\
                   80: 'Eighty', 90:'Ninety'}
        numpart = []
        while(num):
            tmp = num%1000
            numpart.append(tmp)
            num = num // 1000
        
        output = ''
        
        for i, tmpnum in enumerate(numpart):
            tmpstr = ''
            if tmpnum // 100: tmpstr += numdict[tmpnum//100] + ' Hundred'
            tmpnum = tmpnum % 100
            if numdict.get(tmpnum, 0):
                if tmpstr: tmpstr += ' '
                tmpstr += numdict[tmpnum]
            elif tmpnum == 0:
                pass
            else: #21~99
                if tmpstr: tmpstr += ' '
                tmpstr += numdict[(tmpnum//10)*10] + ' ' + numdict[tmpnum%10]
            
            if tmpstr:
                if i == 0:
                    output = tmpstr + output
                if i == 1:
                    if output:
                        output = tmpstr + ' Thousand ' + output
                    else:
                        output = tmpstr + ' Thousand'
                if i == 2:
                    if output:
                        output = tmpstr + ' Million ' + output
                    else:
                        output = tmpstr + ' Million'
                if i == 3:
                    if output:
                        output = tmpstr + ' Billion ' + output
                    else:
                        output = tmpstr + ' Billion'
        return output
        
if __name__ == "__main__":
    num = 4213562341234
    sol = Solution()
    print(sol.numberToWords(num))