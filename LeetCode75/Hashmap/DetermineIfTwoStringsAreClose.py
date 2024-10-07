class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2): return False

        dict1 = {}
        dict2 = {}

        # count occurences of each char
        for i in range(len(word1)):

            a, b = word1[i], word2[i]

            if a not in dict1:
                dict1[a] = 1
            else: dict1[a] += 1

            if b not in dict2:
                dict2[b] = 1
            else: dict2[b] += 1

        # count occurences of frequencies
        vals1 = {}
        for i in dict1.values():
            if i not in vals1:
                vals1[i] = 1
            else: vals1[i] += 1
        
        vals2 = {}
        for i in dict2.values():
            if i not in vals2:
                vals2[i] = 1
            else: vals2[i] += 1

        sameChars = len(set(dict1.keys()).difference(set(dict2.keys()))) == 0

        # stricly same chars and same frequencies
        return sameChars and vals1 == vals2