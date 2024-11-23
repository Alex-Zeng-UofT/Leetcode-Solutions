class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        
        frequencies = {}

        for row in matrix:

            pattern = "".join('t' if cur == row[0] else 'f' for cur in row)
            
            if pattern not in frequencies:
                frequencies[pattern] = 1
            else: frequencies[pattern] += 1

        return max(frequencies.values())