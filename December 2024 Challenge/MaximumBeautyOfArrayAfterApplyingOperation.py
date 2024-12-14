class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        beg, ret = 0, 0

        for end in range(len(nums)):
            
            while beg <= end and nums[end] - k > nums[beg] + k:
                beg += 1
            
            ret = max(ret, end - beg + 1)

        return ret

