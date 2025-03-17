class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False

        for num in range(2, int(sqrt(right)) + 1):
            if sieve[num]:
                for multiple in range(num * num, right + 1, num):
                    sieve[multiple] = False
        
        primes = []
        minimum = 100000000
        ret = [-1, -1]

        for i in range(left, right + 1):
            if sieve[i]:
                primes.append(i)

        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < minimum:
                minimum = primes[i + 1] - primes[i] 
                ret = [primes[i], primes[i + 1]]

        return ret