class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:

        left = 0
        running = 0
        ret = 0

        for right in range(len(nums)):
            while running & nums[right]:
                running ^= nums[left]
                left += 1

            running |= nums[right]
            ret = max(ret, right - left + 1)

        return ret