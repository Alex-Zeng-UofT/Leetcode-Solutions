class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def can_repair(minutes, cars, ranks):

            count = 0

            for rank in ranks:
                count += floor(sqrt(minutes / rank))

            return count >= cars
        
        l, r = -1, max(ranks) * cars ** 2

        while l < r:

            mid = (l + r) // 2

            if can_repair(mid, cars, ranks):
                r = mid
            else:
                l = mid + 1

        return r