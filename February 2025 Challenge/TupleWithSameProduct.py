class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        ret = 0
        mults = {}

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                mult = nums[i] * nums[j]

                if mult not in mults:
                    mults[mult] = 1
                else:
                    mults[mult] += 1

        for prod in mults:
            ret += comb(mults[prod], 2) * 8
        
        return ret