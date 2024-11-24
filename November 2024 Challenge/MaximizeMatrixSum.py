class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        
        total = 0
        smallest = 1000000
        count_neg = 0

        for row in matrix:
            for num in row:

                total += abs(num)
                smallest = min(smallest, abs(num))

                if num < 0: count_neg += 1
        
        return total if count_neg % 2 == 0 else total - smallest * 2
