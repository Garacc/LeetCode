class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True] * n
        for i in range(n):
            if i < 2:
                isPrime[i] = False
                continue
            elif isPrime[i]:
                for j in range(2, (n-1) // i + 1):
                    isPrime[i*j] = False
        return sum(isPrime)