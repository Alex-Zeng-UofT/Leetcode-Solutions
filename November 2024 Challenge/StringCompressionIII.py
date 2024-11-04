class Solution:
    def compressedString(self, word: str) -> str:

        ret = []

        count = 0
        prev = word[0]

        for i, letter in enumerate(word):

            if letter == prev and count < 9:
                count += 1

            else:
                ret.append(str(count))
                ret.append(prev)
                count = 1
                prev = letter

        ret.append(str(count))
        ret.append(prev)

        return "".join(ret)
        