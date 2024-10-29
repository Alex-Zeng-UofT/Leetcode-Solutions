class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        streak = 0

        numbers = set(nums)

        for num in numbers:

            cur_streak = 0
            cur_num = num

            while cur_num in numbers:
                
                cur_streak += 1
                cur_num *= cur_num

                if cur_num > 10 ** 5: break

            streak = max(streak, cur_streak)

        return streak if streak > 1 else -1

