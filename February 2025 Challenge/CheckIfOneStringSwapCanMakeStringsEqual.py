class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        if Counter(s1) != Counter(s2):
            return False

        count = 0

        for i in range(len(s1)):

            if s1[i] != s2[i]:
                count += 1

            if count > 2:
                return False
                
        return True