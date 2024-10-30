class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        lis, lds = [], []
        n = len(nums)

        for i in range(n):

            i_cur, d_cur = nums[i], nums[n - 1 - i]
            i_longest, d_longest = 1, 1

            for j in range(0, i):
                if nums[j] < i_cur:
                    i_longest = max(i_longest, lis[j] + 1)
                if nums[n - 1 - j] < d_cur:
                    d_longest = max(d_longest, lds[j] + 1)
        
            lis.append(i_longest)
            lds.append(d_longest)

        lds = lds[::-1]

        max_len = 0

        for peak in range(1, n - 1):
            if lis[peak] > 1 and lds[peak] > 1:
                max_len = max(max_len, lis[peak] + lds[peak] - 1)
        
        return n - max_len