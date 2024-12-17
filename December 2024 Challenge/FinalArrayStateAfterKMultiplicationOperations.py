class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        ret = [0] * len(nums)
        pq = [(val, i) for i, val in enumerate(nums)]

        heapify(pq)

        for i in range(k):
            cur = heappop(pq)
            heappush(pq, (cur[0] * multiplier, cur[1]))

        for val, i in pq:
            ret[i] = val
        
        return ret