class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        days = len(prices)
        
        visited1 = [False] * days
        dp1 = [0] * days

        def buy(day: int) -> int:
            if day == days:
                return 0

            if visited1[day]:
                return dp1[day]

            buying = sell(day + 1) - (prices[day] + fee)
            not_buying = buy(day + 1)

            visited1[day] = True
            dp1[day] = max(buying, not_buying)

            return dp1[day] 
    
        visited2 = [False] * days
        dp2 = [0] * days

        def sell(day: int) -> int:
            if day == days:
                return 0

            if visited2[day]:
                return dp2[day]

            selling = buy(day + 1) + prices[day]
            not_selling = sell(day + 1)

            visited2[day] = True
            dp2[day] = max(selling, not_selling)

            return dp2[day]

        return buy(0)
            