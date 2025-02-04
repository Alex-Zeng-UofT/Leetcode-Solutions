class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        ret = nums[0]
        running = nums[0]

        for i in range(1, len(nums)):

            if nums[i] > nums[i - 1]:
                running += nums[i]
            else:
                running = nums[i]

            ret = max(running, ret)

        return ret
        