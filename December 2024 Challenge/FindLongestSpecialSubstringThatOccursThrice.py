class Solution:
    def maximumLength(self, s: str) -> int:
        
        def is_valid_length(length: int) -> bool:
            
            def is_special(counts) -> str:

                for key in counts:
                    if counts[key] == length:
                        return key
                
                return ""

            window = [s[i] for i in range(0, length - 1)]
            counts = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
            special_occurences = {}

            for letter in window:
                counts[letter] += 1

            for i in range(length - 1, len(s)):

                window.append(s[i])
                counts[s[i]] += 1
                
                cur = is_special(counts)
                
                if cur:
                    if cur in special_occurences:
                        special_occurences[cur] += 1
                        if special_occurences[cur] == 3:
                            return True
                    else: special_occurences[cur] = 1

                popped = window.pop(0)
                counts[popped] -= 1

            return False

        left, right = 1, len(s)
        best = -1

        while left < right:

            mid = (left + right) // 2

            if not is_valid_length(mid):
                right = mid
            else:
                best = max(best, mid)
                left = mid + 1

        return best