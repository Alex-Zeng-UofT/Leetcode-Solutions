class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        def is_vowel(word: str) -> bool:
            return word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u'
        
        ret = []
        counts = [0]

        for word in words:

            if is_vowel(word[0]) and is_vowel(word[-1]):
                counts.append(counts[-1] + 1)
            else:
                counts.append(counts[-1])

        for beg, end in queries:
            ret.append(counts[end + 1] - counts[beg])

        return ret
