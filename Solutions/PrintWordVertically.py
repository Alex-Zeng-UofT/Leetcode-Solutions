class Solution:
    def printVertically(self, s: str) -> List[str]:
        
        ret = []

        words = s.split(' ')
        length = 0

        for w in words:
            if len(w) > length:
                length =len(w)
        

        for i in range(length):
            st = ''

            for word in words:
                if i < len(word):
                    st += word[i]
                else: st += ' '

            ret.append(st.rstrip())

        return ret