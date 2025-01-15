class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        
        count = 0
        while num2 > 0:
            if num2 & 1 == 1:
                count += 1
            num2 = num2 >> 1

        bits = []
        while num1 > 0:
            bits.append(num1 & 1)
            num1 = num1 >> 1
        
        bits = ([0] * (32 - len(bits))) + bits[::-1]
        ret = [0] * 32

        for i in range(32):
            if bits[i] == 1 and count:
                ret[i] = 1
                count -= 1
        
        pos = -1
        while count:
            if bits[pos] == 0:
                ret[pos] = 1
                count -= 1
            pos -= 1

        ret = ret[::-1]
        ans = 0

        for i in range(32):
            if ret[i]:
                ans += 2 ** i

        return ans