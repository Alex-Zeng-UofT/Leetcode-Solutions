class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        events.sort()

        pq = []

        ret = 0
        max_before_idx = 0

        for beg, end, val in events:
            
            while pq and pq[0][0] < beg:
                cur = heappop(pq)
                max_before_idx = max(max_before_idx, cur[1])

            ret = max(ret, val + max_before_idx)

            heappush(pq, (end, max(val, max_before_idx)))

        return ret