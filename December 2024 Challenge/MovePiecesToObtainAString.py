class Solution:
    def canChange(self, start: str, target: str) -> bool:

        if start.count("_") != target.count("_"):
            return False

        j = 0
        n = len(start)

        for i in range(n):

            if start[i] == '_': continue

            while j < n and target[j] == '_':
                j += 1
            
            if start[i] != target[j]:
                return False

            if start[i] == "L" and i < j:
                return False

            if start[i] == "R" and i > j:
                return False

            j += 1
        
        return True