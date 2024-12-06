class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        forbidden = set(banned)

        cur_sum = 0
        count = 0

        for i in range(1, n + 1):
            
            if i in forbidden: continue

            cur_sum += i

            if cur_sum > maxSum:
                return count

            count += 1

        return count
        