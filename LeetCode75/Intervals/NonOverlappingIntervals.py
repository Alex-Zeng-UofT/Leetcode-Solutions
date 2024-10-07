class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()

        removed, prev = 0, -10000000

        for interval in intervals:

            if interval[0] < prev:
                removed += 1
                prev = min(prev, interval[1])
                
            else: prev = interval[1]

        return removed