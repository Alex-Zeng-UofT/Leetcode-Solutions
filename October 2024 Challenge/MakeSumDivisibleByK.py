class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        
        target = sum(nums) % p

        if target == 0: return 0

        map = {0: -1}
        ret = len(nums)
        accumulator = 0

        for i, num in enumerate(nums):
            
            accumulator += num
            accumulator %= p

            goal = (accumulator - target + p) % p

            if goal in map and i - map[goal] < ret:
                ret = i - map[goal]

            map[accumulator] = i

        return ret if ret < len(nums) else -1
