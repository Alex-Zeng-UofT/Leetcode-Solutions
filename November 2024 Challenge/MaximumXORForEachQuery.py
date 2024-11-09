class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:

        maximize = (1 << maximumBit) - 1
        res = 0
        ret = []

        for num in nums:
            res ^= num

        for num in nums[::-1]:
            ret.append(res ^ maximize)
            res ^= num

        return ret