class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:

        n = len(words)
        words.sort(key=lambda x : len(x))
        ret = []

        for i in range(n - 1):
            for j in range(i + 1, n):
                if words[j].find(words[i]) != -1:
                    ret.append(words[i])
                    break
        
        return ret