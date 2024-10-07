import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        ret = right

        while left <= right:

            k = (left + right) // 2

            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            
            if hours <= h:
                ret = k
                right = k - 1
            else:
                left = k + 1

        return ret