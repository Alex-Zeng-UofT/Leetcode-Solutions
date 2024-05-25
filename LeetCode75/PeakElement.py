class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums)

        while left < right:

            mid = (left + right) // 2

            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid
                

        return left
            
        