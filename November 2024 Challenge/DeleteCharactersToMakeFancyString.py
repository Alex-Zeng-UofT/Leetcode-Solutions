class Solution:
    def makeFancyString(self, s: str) -> str:
        
        consecutive = 1
        prev = s[0]
        ret = [s[0]]

        for letter in s[1:]:

            if letter == prev:
                consecutive += 1
            else: 
                consecutive = 1
                prev = letter

            if consecutive < 3: ret.append(letter)

        return "".join(ret)
