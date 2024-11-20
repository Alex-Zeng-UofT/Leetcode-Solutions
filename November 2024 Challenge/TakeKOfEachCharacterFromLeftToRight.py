class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        
        counter = {'a': 0, 'b': 0, 'c': 0}

        for char in s:
            counter[char] += 1

        if counter['a'] < k or counter['b'] < k or counter['c'] < k:
            return -1

        window = {'a': 0, 'b': 0, 'c': 0}

        beg = 0
        max_len = 0

        for end in range(len(s)):

            window[s[end]] += 1

            while beg <= end and(
                counter['a'] - window['a'] < k or
                counter['b'] - window['b'] < k or
                counter['c'] - window['c'] < k
            ):
                window[s[beg]] -= 1
                beg += 1

            max_len = max(max_len, end - beg + 1)

        return len(s) - max_len