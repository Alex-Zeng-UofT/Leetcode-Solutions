class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        required, window = {}, {}
        n, m = len(s1), len(s2)

        if m < n: return False

        for letter in s1:
            if letter not in required:
                required[letter] = 1
            else: required[letter] += 1
        
        for i in range(n - 1):
            if s2[i] not in window:
                window[s2[i]] = 1
            else: window[s2[i]] += 1

        for i in range(m - n + 1):

            cur = i + n - 1

            if s2[cur] not in window:
                window[s2[cur]] = 1
            else: window[s2[cur]] += 1
            
            exists = True
            for key in required:
                if key not in window or required[key] != window[key]:
                    exists = False
                    break
            if exists: return True

            window[s2[i]] -= 1
    
        return False
            


