import math

class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if not area: return [0, 0]
        
        W = int(math.sqrt(area))
        while W:
            L = area // W
            if L * W == area and L >= W: return [L, W]
            W -= 1