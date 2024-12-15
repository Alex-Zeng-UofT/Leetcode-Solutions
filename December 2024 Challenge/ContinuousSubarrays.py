class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        
        ret = 0
        beg = 0

        smallest, largest = float('inf'), 0

        for end in range(len(nums)):
            
            smallest = min(smallest, nums[end])
            largest = max(largest, nums[end])

            if largest - smallest > 2:

                diff = end - beg
                ret += diff * (diff + 1) // 2

                beg = end
                smallest = largest = nums[end]

                while beg > 0 and abs(nums[beg - 1] - nums[end]) <= 2:
                    beg -= 1
                    smallest = min(smallest, nums[beg])
                    largest = max(largest, nums[beg])

                if beg < end:
                    diff = end - beg
                    ret -= diff * (diff + 1) // 2

        diff = len(nums) - beg
        return ret + diff * (diff + 1) // 2    