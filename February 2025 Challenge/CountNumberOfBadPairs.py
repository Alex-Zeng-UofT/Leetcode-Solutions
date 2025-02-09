class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        frequencies = {}

        for i in range(n):

            val = i - nums[i]

            if val not in frequencies:
                frequencies[val] = 1
            else:
                frequencies[val] += 1

        ret = 0

        for val in frequencies:
            ret += frequencies[val] * (frequencies[val] - 1) // 2

        return (n * (n - 1) // 2) - ret