class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        n = len(potions)
        ret = []

        potions.sort()

        for i in spells:

            l, r, = 0, n - 1
            idx = n

            while l <= r:

                mid = (l + r) // 2

                if i * potions[mid] >= success:
                    r = mid - 1
                    idx = mid
                else: 
                    l = mid + 1

            ret.append(n - idx)

        return ret
            


            

        