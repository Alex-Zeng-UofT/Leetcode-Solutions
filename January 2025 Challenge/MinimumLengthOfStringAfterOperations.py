class Solution:
    def minimumLength(self, s: str) -> int:
        
        counts = {}

        for letter in s:
            if letter not in counts:
                counts[letter] = 1
            else: counts[letter] += 1

        min_len = 0

        for letter in counts:
            min_len += 2 - counts[letter] % 2

        return min_len