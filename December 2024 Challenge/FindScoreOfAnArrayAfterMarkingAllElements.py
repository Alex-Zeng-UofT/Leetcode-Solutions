class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        score = 0

        pq = [(val, i) for i, val in enumerate(nums)]
        marked = set()

        heapify(pq)

        while pq:
            
            val, idx = heappop(pq)

            if idx in marked:
                continue
            
            score += val

            marked.add(idx)
            if idx > 0: marked.add(idx - 1)
            if idx < len(nums) - 1: marked.add(idx + 1)

        return score