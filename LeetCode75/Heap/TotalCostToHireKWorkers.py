class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        pq = []

        left = 0
        right = len(costs) - 1

        for i in range(candidates):
            heapq.heappush(pq, (costs[i], False))
            left += 1

        for i in range(candidates):
            if left > right : break
            heapq.heappush(pq, (costs[right], True))
            right -= 1
            
        total = 0
        for i in range(k):
            val, isRight = heapq.heappop(pq)
            
            if left <= right:
                if isRight:
                    heapq.heappush(pq, (costs[right], True))
                    right -= 1
                else:
                    heapq.heappush(pq, (costs[left], False))
                    left += 1

            total += val

        return total