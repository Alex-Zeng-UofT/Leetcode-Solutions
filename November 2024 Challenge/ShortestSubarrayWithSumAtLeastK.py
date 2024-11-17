class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        def bs(nums: List[Tuple[int, int]], target: int) -> int:

            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid][0] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return right
        
        n = len(nums)

        shortest = 1000000
        cur_sum = 0

        stack = [(0, -1)]

        for i in range(n):

            cur_sum += nums[i]

            while stack and cur_sum <= stack[-1][0]:
                stack.pop()
            
            stack.append((cur_sum, i))

            idx = bs(stack, cur_sum - k)

            if idx >= 0:
                shortest = min(shortest, i - stack[idx][1])

        return shortest if shortest < 1000000 else -1