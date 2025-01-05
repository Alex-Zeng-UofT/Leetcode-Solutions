class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        n = len(s)
        letters = [letter for letter in s]
        diffs = [0] * n

        for beg, end, ind in shifts:

            dir = 1 if ind == 1 else -1
            
            diffs[beg] += dir

            if end + 1 < n:
                diffs[end + 1] -= dir

        cur_diff = 0
        
        for i in range(n):
            cur_diff += diffs[i]
            letters[i] = chr(((ord(letters[i]) - 97 + cur_diff) % 26) + 97)

        return "".join(letters)