class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        if n == 1: return "0"

        length = 1 << n
        mid = length // 2

        if k < mid: return self.findKthBit(n - 1, k)

        if k == mid: return "1"

        flipbit = self.findKthBit(n - 1, length - k)

        return "0" if flipbit == "1" else "1"