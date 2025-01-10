class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        ret = []
        sup = {chr(key + 97) : 0 for key in range(0, 26)}

        for sub in words2:

            two = {}
            for letter in sub:
                if letter in two:
                    two[letter] += 1
                else: two[letter] = 1
            
            for key in two:
                sup[key] = max(sup[key], two[key])

        for candidate in words1:

            one = {}
            for letter in candidate:
                if letter in one:
                    one[letter] += 1
                else: one[letter] = 1

            is_subset = True

            for key in sup:

                if sup[key] == 0: continue

                if key not in one or sup[key] > one[key]:
                    is_subset = False
                    break

            if is_subset:
                ret.append(candidate)

        return ret