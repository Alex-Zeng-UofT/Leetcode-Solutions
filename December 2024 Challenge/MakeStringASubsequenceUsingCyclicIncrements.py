class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def get_next(letter: str) -> str:
            
            if letter == 'z':
                return 'a'
            
            return chr(ord(letter) + 1)

        cur = 0
        for char in str1:
            
            if cur == len(str2):
                return True 

            if char == str2[cur] or get_next(char) == str2[cur]:
                cur += 1

        return cur == len(str2)
        