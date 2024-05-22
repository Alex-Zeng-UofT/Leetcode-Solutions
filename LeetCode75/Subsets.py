import sys
from typing import List

class Solution:

    def backtrack(self, lst: List[List[int]], stock: List[int], prev: List[int]) -> None:
        temp = stock.copy()
        sub = prev.copy()
        for i in range(len(temp)):
            cur = temp[0]
            sub.append(cur)
            lst.append(sub.copy())
            temp.pop(0)
            self.backtrack(lst, temp, sub)
            sub.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = [[]]

        self.backtrack(ret, nums, [])

        return ret

    

            
