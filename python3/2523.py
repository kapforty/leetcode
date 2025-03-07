class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # sieve of eratosthenes
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(sqrt(right)) + 1):
            if sieve[i] == False:
                continue
            for j in range(i*i, right + 1, i):
                sieve[j] = False
        
        # find closest primes
        primes = [x for x in range(left, right + 1) if sieve[x]]
        if len(primes) < 2: return [-1, -1]
        res = primes[:2]
        for i in range(len(primes) - 1):
            if primes[i+1] - primes[i] < res[1] - res[0]:
                res = [primes[i], primes[i+1]]
        return res
