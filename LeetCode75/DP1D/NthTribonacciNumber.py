class Solution:
    def tribonacci(self, n: int) -> int:
        
        i, j, k = 0, 1, 1

        if n < 1:
            return i
        elif n < 2:
            return j
        elif n < 3:
            return k

        for m in range(3, n):
            temp = i + j + k
            i = j
            j = k
            k = temp
        
        return i + j + k