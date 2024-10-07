class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = 0

        for i in nums: ret ^= i

        return ret