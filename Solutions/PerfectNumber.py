class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        divisors = set()

        for i in range(1, int(sqrt(num)) + 1):

            if num % i == 0:
                divisors.add(i)
                divisors.add(num / i)
        
        return sum(divisors) == num * 2