class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = [(one, two) for one, two in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

        max_val, cur = 0, 0
        heap = []

        for one, two in pairs:

            heapq.heappush(heap, one)
            cur += one

            if len(heap) > k:
                min_val = heapq.heappop(heap)
                cur -= min_val
            if len(heap) == k and cur * two > max_val:
                max_val = cur * two
        
        return max_val
