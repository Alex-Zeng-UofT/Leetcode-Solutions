class Solution:
    def minOperations(self, nums: List[int]) -> int:

        ret = 0

        for i in range(2, len(nums)):

            if nums[i - 2] == 0:

                for j in range(i - 2, i + 1):
                    nums[j] = 1 - nums[j]
                
                ret += 1

        return ret if sum(nums[-3:]) == 3 else -1

                

            
        