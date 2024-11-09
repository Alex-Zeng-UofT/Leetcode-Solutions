class Solution:
    def minEnd(self, n: int, x: int) -> int:
        
        ret = x
        mask = 1
        n -= 1

        while n > 0:

            if x & mask == 0:
                ret |= (n & 1) * mask
                n = n >> 1

            mask = mask << 1

        return ret