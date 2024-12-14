class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        piles = [-pile for pile in gifts]
        heapify(piles)

        for i in range(k):
            cur = heappop(piles)
            heappush(piles, -floor((-cur) ** 0.5))

        return -sum(piles)