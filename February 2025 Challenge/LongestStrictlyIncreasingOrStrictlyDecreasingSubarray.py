class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        cur_max = 1
        running = 1
        increasing = True

        for i in range(1, len(nums)):

            if nums[i] == nums[i - 1]:
                running = 1

            elif increasing:
                if nums[i] > nums[i - 1]:
                    running += 1
                else:
                    increasing = False
                    running = 2
                    
            else:
                if nums[i] < nums[i - 1]:
                    running += 1
                else:
                    increasing = True
                    running = 2

            cur_max = max(running, cur_max)

        return cur_max