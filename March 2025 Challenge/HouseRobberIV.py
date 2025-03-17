class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def count_houses(nums, capability):

            count = 0
            i = 0
            
            while i < len(nums):

                if nums[i] <= capability:
                    count += 1
                    i += 1

                i += 1

            return count
                
        
        l, r = min(nums) - 1, max(nums)

        while l < r:

            mid = (l + r) // 2

            if count_houses(nums, mid) < k:
                l = mid + 1
            else:
                r = mid

        return r