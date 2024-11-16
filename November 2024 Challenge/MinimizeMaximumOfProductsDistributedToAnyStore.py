class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        left, right = 1, max(quantities)
        ret = right

        # O(M)
        def is_valid(capacity: int) -> bool:
            nonlocal n, quantities

            count = 0

            for quant in quantities:
                count += ceil(quant / capacity)

            return count <= n

    
        while left < right:

            mid = (left + right) // 2

            if is_valid(mid):
                right = mid
            else:
                left = mid + 1

        return left

