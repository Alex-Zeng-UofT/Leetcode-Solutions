class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        count = 1

        for i in range(0, len(nums)):

            if i > 0 and nums[i] == nums[i - 1] + 1:
                if count < k: count += 1
            else: count = 1

            if i >= k - 1:
                ret.append(nums[i] if count == k else -1)

        return ret