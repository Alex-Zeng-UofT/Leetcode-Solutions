class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0] * (days[-1] + 1)

        i = 0
        for day in range(1, days[-1] + 1):

            if day < days[i]:
                dp[day] = dp[day - 1]

            else:
                # calculate cheapest cost for travelling on ${day}
                dp[day] = min(dp[max(0, day - 1)] + costs[0],
                            dp[max(0, day - 7)] + costs[1],
                            dp[max(0, day - 30)] + costs[2])

                i += 1


        return dp[days[-1]]