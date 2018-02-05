class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        size = len(M)
        CircleNum = 0
        friend_circle = [0 for i in range(size)]
        checkstack = [i for i in range(size)]
        while(True):
            teststd = checkstack.pop()
            if(friend_circle[teststd] == 0):#new circle
                CircleNum += 1
                friend_circle[teststd] = CircleNum
            for i in range(size):
                if(M[teststd][i] == 1 and friend_circle[i] == 0):
                    friend_circle[i] = CircleNum
                    checkstack.append(i)
            if(checkstack == []):
                break
            
        return CircleNum
    
if __name__ == '__main__':
    a = Solution()
    M = [[1,1,0], [1,1,1], [0,1,1]]
    print(a.findCircleNum(M))