class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        ret = []
        pq = []

        if a != 0: pq.append((-a, 'a'))
        if b != 0: pq.append((-b, 'b'))
        if c != 0: pq.append((-c, 'c'))

        heapify(pq)

        while pq:
            
            num, char = heappop(pq)

            if len(ret) >= 2 and ret[-1] == char and ret[-2] == char:

                if not pq: break

                next_num, next_char = heappop(pq)
                ret.append(next_char)
                
                if next_num + 1 < 0: heappush(pq, (next_num + 1, next_char))
                heappush(pq, (num, char))

            else:
                ret.append(char)
                if num + 1 < 0: heappush(pq, (num + 1, char))
                
        return "".join(ret)