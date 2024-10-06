class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        split1 = sentence1.split(' ')
        split2 = sentence2.split(' ')

        n, m = len(split1), len(split2)
        
        if n < m:
            return self.areSentencesSimilar(sentence2, sentence1)

        beg, end1, end2 = 0, n - 1, m - 1

        while beg < m and split1[beg] == split2[beg]:
            beg += 1
        
        while end2 >= 0 and split1[end1] == split2[end2]:
            end1 -= 1
            end2 -= 1

        return beg > end2
        