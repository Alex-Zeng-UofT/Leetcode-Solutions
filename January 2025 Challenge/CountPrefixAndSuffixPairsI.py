class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        n = len(words)
        count = 0

        for i in range(n - 1):
            for j in range(i + 1, n):

                l1, l2 = len(words[i]), len(words[j])

                if l2 < l1: continue

                if words[i] == words[j][:l1] and words[i] == words[j][-l1:]:
                    count += 1

        return count
        