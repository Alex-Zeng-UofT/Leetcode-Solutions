import sys
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        ret = [0]
        offset = 1

        for i in range(1, n + 1):
            
            if offset * 2 == i:
                offset = i

            ret.append(1 + ret[i - offset])

        return ret