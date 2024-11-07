class Solution:
    def minChanges(self, s: str) -> int:
        
        is_odd_one, is_odd_zero = False, False
        count = 0

        for bit in s:

            if is_odd_one:
                count += 1 if bit == '0' else 0
                is_odd_one = False
            
            elif is_odd_zero:
                count += 1 if bit == '1' else 0
                is_odd_zero = False

            else:
                if bit == '1':
                    is_odd_one = True
                else: is_odd_zero = True

        return count