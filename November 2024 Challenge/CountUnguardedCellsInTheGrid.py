class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        matrix = [([0] * n) for _ in range(m)]

        count = len(guards) + len(walls)

        for row, col in guards:
            matrix[row][col] = 2
        
        for row, col in walls:
            matrix[row][col] = 2

        def all_can_see(row, col):
            nonlocal matrix, m, n

            cur_count = 0

            r, c = row - 1, col
            while r >= 0 and matrix[r][c] < 2:
                if matrix[r][c] == 0: 
                    cur_count += 1
                    matrix[r][c] = 1
                r -= 1

            r, c = row + 1, col
            while r < m and matrix[r][c] < 2:
                if matrix[r][c] == 0: 
                    cur_count += 1
                    matrix[r][c] = 1
                r += 1

            r, c = row, col - 1
            while c >= 0 and matrix[r][c] < 2:
                if matrix[r][c] == 0: 
                    cur_count += 1
                    matrix[r][c] = 1
                c -= 1

            r, c = row, col + 1
            while c < n and matrix[r][c] < 2:
                if matrix[r][c] == 0: 
                    cur_count += 1
                    matrix[r][c] = 1
                c += 1

            return cur_count

        for guard in guards:
            count += all_can_see(guard[0], guard[1])

        return m * n - count