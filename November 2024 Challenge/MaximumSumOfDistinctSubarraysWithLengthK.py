class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        cur_sum, max_sum = 0, 0

        indicator = 0
        counts = {}

        for i in range(k):

            num = nums[i]
            cur_sum += num
            
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

            indicator += counts[num]

        if indicator == k:
            max_sum = max(max_sum, cur_sum)
        
        for i in range(k, len(nums)):

            num = nums[i]
            start = nums[i - k]

            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1

            indicator += counts[num] - counts[start]
            counts[start] -= 1

            cur_sum += num - start

            if indicator == k:
                max_sum = max(max_sum, cur_sum)
        
        return max_sum