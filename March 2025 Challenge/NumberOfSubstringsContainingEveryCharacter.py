class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        def is_satisfied(counts):
            return counts['a'] and counts['b'] and counts['c']
        
        counts = {'a': 0, 'b': 0, "c": 0}

        beg = 0
        ret = 0

        for end in range(len(s)):

            counts[s[end]] += 1

            while is_satisfied(counts):
                ret += len(s) - end
                counts[s[beg]] -= 1
                beg += 1

        return ret