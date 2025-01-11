class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        
        if k > len(s): return False

        singles = set()

        for letter in s:
            if letter not in singles:
                singles.add(letter)
            else: singles.remove(letter)

        return len(singles) <= k