class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        
        teams = set([i for i in range(n)])
        losers = set()

        for winner, loser in edges:
            losers.add(loser)
        
        winners = teams.difference(losers)

        return list(winners)[0] if len(winners) == 1 else -1