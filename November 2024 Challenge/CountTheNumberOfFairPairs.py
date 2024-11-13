class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()

        def count_less_than(nums: List[int], upperbound: int) -> int:

            left, right = 0, len(nums) - 1
            count = 0

            while left < right:

                cur_sum = nums[left] + nums[right]

                if cur_sum > upperbound:
                    right -= 1
                else:
                    count += right - left
                    left += 1

            return count

        return count_less_than(nums, upper) - count_less_than(nums, lower - 1)
        