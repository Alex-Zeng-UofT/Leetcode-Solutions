class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()

        ending = points[0][1]
        count = 1

        for balloon in points[1:]:

            if balloon[0] > ending:
                count += 1
                ending = balloon[1]
                
            else: ending = min(ending, balloon[1])
        
        return count