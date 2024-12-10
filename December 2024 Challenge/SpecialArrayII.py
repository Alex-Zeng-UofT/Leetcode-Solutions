class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        ret = []
        windows = []
        end = 0

        for start in range(0, len(nums)):

            end = max(end, start)

            while end < len(nums) - 1 and (nums[end] + nums[end + 1]) % 2 == 1:
                end += 1
            
            windows.append(end)
        
        for beg, end in queries:
            ret.append(end <= windows[beg])

        return ret

