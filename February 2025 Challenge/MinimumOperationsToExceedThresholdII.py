class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        ret = 0
        heapify(nums)

        while len(nums) >= 2 and nums[0] < k:
            x = heappop(nums)
            y = heappop(nums)
            heappush(nums, min(x, y) * 2 + max(x, y))
            ret += 1
            
        return ret