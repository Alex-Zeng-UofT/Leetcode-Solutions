class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        ret = []
        k = len(part)

        for i in range(len(s)):

            ret.append(s[i])

            if len(ret) >= k and "".join(ret[-k:]) == part:
                for j in range(k):
                    ret.pop()

        return "".join(ret)
        