class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)
        r = []
        d = []

        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else: d.append(i)
        
        while r and d:
            if r[0] < d[0]:
                r.append(r[0] + n)
            else: d.append(d[0] + n)
            r.pop(0)
            d.pop(0)

        return "Radiant" if r else "Dire"

        