class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        n = len(s)

        if len(goal) != n: return False
        
        for i in range(n):

            if s == goal: return True

            s = s[1:] + s[0]
        
        return False