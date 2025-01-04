class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        ones, zeros = 0, 0
        ret = 0

        for char in s:
            if char == '0':
                zeros += 1
            else: ones += 1

        total = zeros
        
        for end in s[:-1]:
            if end == '0':
                zeros -= 1
            else: ones -= 1

            ret = max(ret, total - zeros + ones)

        return ret