class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:

        pq = [(-ord(c), cnt) for c, cnt in Counter(s).items()]
        heapify(pq)
        ret = []

        while pq:

            char_neg, count = heappop(pq)
            char = chr(-char_neg)
            use = min(count, repeatLimit)

            ret.append(char * use)

            if count > use and pq:

                next_char_neg, next_count = heappop(pq)
                ret.append(chr(-next_char_neg))

                if next_count > 1:
                    heappush(pq, (next_char_neg, next_count - 1))
                    
                heappush(pq, (char_neg, count - use))

        return "".join(ret)