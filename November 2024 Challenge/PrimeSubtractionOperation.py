class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:

        def is_prime(num: int) -> bool:

            if num == 1: return False
            
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False

            return True
        
        prev = 0

        for num in nums:

            if num <= prev:
                return False

            cur = num - prev - 1

            while cur > 0 and not is_prime(cur):
                cur -= 1
            
            prev = num - cur

        return True