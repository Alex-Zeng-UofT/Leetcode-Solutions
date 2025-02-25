class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        ret = 0
        evens, odds = 1, 0
        mod = 10 ** 9 + 7
        sum = 0

        for i in arr:

            sum += i

            if sum % 2 == 0:
                ret += odds
                evens += 1
            else:
                ret += evens
                odds += 1
            
            ret %= mod

        return ret
                

        return ret