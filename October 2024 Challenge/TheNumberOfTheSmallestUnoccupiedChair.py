class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        starts = [(pair[0], i) for i, pair in enumerate(times)]
        ends = []

        starts = sorted(starts)
        heapq.heapify(ends)

        chairs = [i for i in range(len(times))]
        heapq.heapify(chairs)

        for start, i in starts:

            while ends and ends[0][0] <= start:
                heapq.heappush(chairs, heapq.heappop(ends)[1])

            if i == targetFriend: return chairs[0]
            
            heapq.heappush(ends, (times[i][1], heapq.heappop(chairs)))

        return -1
        