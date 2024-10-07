class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        count = 0
        threshold = 0
        prev = nums[0]

        for num in nums:
            if num != prev or threshold < 2:

                nums[count] = num
                count += 1

                if num == prev: threshold += 1
                else: threshold = 1

            prev = num

        return count