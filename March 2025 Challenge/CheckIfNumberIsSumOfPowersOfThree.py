
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        power = 16

        while n > 0:

            if 3 ** power <= n:
                n -= 3 ** power

            if 3 ** power <= n:
                return False
            
            power -= 1

        return True