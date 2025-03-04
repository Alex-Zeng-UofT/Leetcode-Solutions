class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less = 0
        pivots = 0
        ret = [0] * len(nums)
        
        for num in nums:
            if num < pivot:
                less += 1
            elif num == pivot:
                pivots += 1

        i, j = 0, less + pivots

        for num in nums:
            if num < pivot:
                ret[i] = num
                i += 1
            elif num > pivot:
                ret[j] = num
                j += 1
        
        for i in range(less, less + pivots):
            ret[i] = pivot

        return ret