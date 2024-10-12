class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        pq = []
        heapify(pq)

        for start, end in intervals:

            if pq and pq[0] < start:
                heappop(pq)
            
            heappush(pq, end)

        return len(pq)
        