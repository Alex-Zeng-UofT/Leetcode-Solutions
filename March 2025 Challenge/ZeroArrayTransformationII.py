class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        n = len(nums)
        prefix = [0] * (n + 1)
        running = 0
        ret = 0

        for i in range(n):

            while running + prefix[i] < nums[i]:

                if ret == len(queries):
                    return -1

                l, r, val = queries[ret]

                if r >= i:
                    prefix[max(l, i)] += val
                    prefix[r + 1] -= val

                ret += 1

            running += prefix[i]

        return ret