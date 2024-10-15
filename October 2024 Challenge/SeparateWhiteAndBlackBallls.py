class Solution:
    def minimumSteps(self, s: str) -> int:
        
        steps = 0
        left = 0

        for i in range(len(s)):
            if s[i] == '0':
                steps += i - left
                left += 1
        
        return steps