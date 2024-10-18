class Solution:
    def maximumSwap(self, num: int) -> int:

        dissected = []
        
        i = len(str(num)) - 1
        while num != 0:
            dissected.append((num % 10, i))
            num = num // 10
            i -= 1
        
        sorted = dissected.copy()
        sorted.sort(key=lambda x: (-x[0], -x[1]))
        dissected = dissected[::-1]

        for i in range(len(sorted)):

            pair = sorted[i]

            while i < len(dissected) and pair[0] == dissected[i][0]:
                i += 1

            if pair[1] > i:
                temp = dissected[i]
                dissected[i] = pair
                dissected[pair[1]] = temp
                break

        ret = 0
        for num, i in dissected:
            ret += num
            ret *= 10

        return ret // 10