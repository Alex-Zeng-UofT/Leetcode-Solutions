class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        first, last = [-1] * 26, [-1] * 26
        ret = 0

        for i, letter in enumerate(s):

            idx = ord(letter) - 97

            if first[idx] == -1:
                first[idx] = i

            last[idx] = i

        for i in range(26):

            if last[i] - first[i] < 1: continue

            between = set()

            for j in range(first[i] + 1, last[i]):
                between.add(s[j])

            ret += len(between)

        return ret
        