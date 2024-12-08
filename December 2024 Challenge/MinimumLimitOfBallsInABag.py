class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def canObtain(max_balls: int) -> bool:

            operations_needed = 0

            for balls in nums:
                operations_needed += ceil(balls / max_balls) - 1

            return operations_needed <= maxOperations

        left, right = 1, max(nums)

        while left < right:

            mid = (left + right) // 2

            if canObtain(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
        