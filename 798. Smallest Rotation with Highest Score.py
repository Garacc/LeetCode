class Solution:
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        '''
        TLE
        score = [0 for _ in range(len(A))]
        for k in range(len(A)):
            checklist = A[k:] + A[:k]
            tmp = 0
            for i, num in enumerate(checklist):
                if num <= i:
                    tmp += 1
            score[k] = tmp
        
        maxscore = max(score)
        
        return score.index(maxscore)
        '''
        N = len(A)
        change = [1] * N
        for i in range(N): change[(i - A[i] + 1) % N] -= 1
        for i in range(1, N): change[i] += change[i - 1]
        return change.index(max(change))