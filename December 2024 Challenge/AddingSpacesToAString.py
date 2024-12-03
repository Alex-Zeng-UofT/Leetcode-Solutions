class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ret = []
        cur = 0

        for i in range(len(s)):

            if cur < len(spaces) and spaces[cur] == i:
                ret.append(' ')
                cur += 1
                
            ret.append(s[i])

        return "".join(ret)