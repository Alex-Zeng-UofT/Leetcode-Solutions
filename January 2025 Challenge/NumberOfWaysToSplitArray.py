class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        total = sum(nums)
        sums = []
        cur, ret = 0, 0

        for num in nums:
            cur += num
            sums.append(cur)

        for i in range(len(nums) - 1):
            if sums[i] >= total - sums[i]:
                ret += 1

        return ret