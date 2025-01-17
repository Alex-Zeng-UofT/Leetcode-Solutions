class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:

        original = [0]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        check_for_zero = original[0] == original[-1]
        
        original = [1]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        check_for_one = original[0] == original[-1]

        return check_for_zero or check_for_one