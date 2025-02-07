class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        ret = []
        colours = set()
        b_to_c, c_count = {}, {}

        for ball, colour in queries:
            
            if ball in b_to_c and b_to_c[ball] == colour:
                ret.append(len(colours))
                continue

            colours.add(colour)

            if ball in b_to_c:
                c_count[b_to_c[ball]] -= 1
                if c_count[b_to_c[ball]] == 0:
                    colours.remove(b_to_c[ball])
            
            b_to_c[ball] = colour

            if colour not in c_count:
                c_count[colour] = 1
            else:
                c_count[colour] += 1

            ret.append(len(colours))
        
        return ret