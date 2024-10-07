from typing import List

class Solution:

    def backtrack(self, ret: List[str], s: str, digits: str, mapping: dict) -> None:
        if len(digits) == 0:
            ret.append(s)
            return

        for letter in mapping[digits[0]]:
            self.backtrack(ret, s + letter, "" if len(digits) == 1 else digits[1:], mapping)

    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        ret = []
        mapping = {
            '2': 'abc', 
            '3': 'def', 
            '4': 'ghi', 
            '5': 'jkl', 
            '6': 'mno', 
            '7': 'pqrs', 
            '8': 'tuv', 
            '9': 'wxyz',  
        }

        self.backtrack(ret, "", digits, mapping)

        return ret

        