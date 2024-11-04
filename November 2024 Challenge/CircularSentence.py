class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        prev = sentence[-1]

        for word in sentence.split():

            if word[0] != prev: return False

            prev = word[-1]

        return True
        