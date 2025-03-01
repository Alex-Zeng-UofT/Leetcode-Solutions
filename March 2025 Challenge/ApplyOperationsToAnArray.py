class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        cur = 0

        for i in range(n):

            if nums[i] == 0:
                continue

            nums[cur] = nums[i]
            cur += 1

        for i in range(cur, n):
            nums[i] = 0

        return nums