class Solution:
    def check(self, nums: List[int]) -> bool:

        broken = False
        
        for i in range(1, len(nums)):

            if not broken and nums[i] < nums[i - 1]:
                broken = True
                if nums[i] > nums[0]:
                    return False
                continue
            
            if broken and (nums[i] < nums[i - 1] or nums[i] > nums[0]):
                return False

        return True