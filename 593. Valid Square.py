class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        sides = [0 for _ in range(6)]
        sides[0] = (p1[1]-p2[1])*(p1[1]-p2[1]) + (p1[0]-p2[0])*(p1[0]-p2[0])
        sides[1] = (p1[1]-p3[1])*(p1[1]-p3[1]) + (p1[0]-p3[0])*(p1[0]-p3[0])
        sides[2] = (p1[1]-p4[1])*(p1[1]-p4[1]) + (p1[0]-p4[0])*(p1[0]-p4[0])
        sides[3] = (p2[1]-p3[1])*(p2[1]-p3[1]) + (p2[0]-p3[0])*(p2[0]-p3[0])
        sides[4] = (p2[1]-p4[1])*(p2[1]-p4[1]) + (p2[0]-p4[0])*(p2[0]-p4[0])
        sides[5] = (p3[1]-p4[1])*(p3[1]-p4[1]) + (p3[0]-p4[0])*(p3[0]-p4[0])
        
        sideset = set(sides)
        if len(sideset) != 2:
            return False
        checkside = sideset.pop()
        i = 0
        for side in sides:
            if side == checkside:
                i += 1
        if i == 2 or i == 4:
            return True
        return False