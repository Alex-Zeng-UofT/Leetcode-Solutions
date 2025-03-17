class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def canDivide(num, k, candies):
            
            count = 0

            for candy in candies:
                count += candy // num

            return count >= k
        
        l, r = 1, max(candies) + 1

        while l < r:
            
            mid = (l + r) // 2

            if canDivide(mid, k, candies):
                l = mid + 1
            else:
                r = mid

        return l - 1
