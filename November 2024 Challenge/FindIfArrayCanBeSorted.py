class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        segments, cur_seg = [], []
        cur_bit_count = nums[0].bit_count()

        for num in nums:
            
            if num.bit_count() == cur_bit_count:
                cur_seg.append(num)

            else:
                segments.append(sorted(cur_seg))
                cur_seg = [num]
                cur_bit_count = num.bit_count()

        segments.append(sorted(cur_seg))

        final = []
        
        for seg in segments: final.extend(seg)

        return final == sorted(final)