class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        #romandict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        thou = num // 1000
        hun = (num%1000)//100
        ten = (num%100)//10
        one = num%10
        output = ''
        
        output += thou*'M'
        
        if hun == 9: output += 'CM'
        elif hun == 5 or hun == 6 or hun == 7 or hun == 8: output += 'D' + (hun-5)*'C'
        elif hun == 4: output += 'CD'
        else: output += hun*'C'
        
        if ten == 9: output += 'XC'
        elif ten == 5 or ten == 6 or ten == 7 or ten == 8: output += 'L' + (ten-5)*'X'
        elif ten == 4: output += 'XL'
        else: output += ten*'X'
        
        if one == 9: output += 'IX'
        elif one == 5 or one == 6 or one == 7 or one == 8: output += 'V' + (one-5)*'I'
        elif one == 4: output += 'IV'
        else: output += one*'I'
        
        return output