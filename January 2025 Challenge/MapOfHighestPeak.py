class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        n, m = len(isWater), len(isWater[0])
        ret = [[-1 for i in range(m)] for j in range(n)]

        next = deque()

        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    ret[i][j] = 0
                    next.append((i, j))

        height = 0

        while next:

            cur_len = len(next)

            for i in range(cur_len):

                r, c = next.popleft()

                if r > 0 and ret[r - 1][c] == -1:
                    ret[r - 1][c] = height + 1
                    next.append((r - 1, c))

                if c > 0 and ret[r][c - 1] == -1:
                    ret[r][c - 1] = height + 1
                    next.append((r, c - 1))

                if r < n - 1 and ret[r + 1][c] == -1:
                    ret[r + 1][c] = height + 1
                    next.append((r + 1, c))

                if c < m - 1 and ret[r][c + 1] == -1:
                    ret[r][c + 1] = height + 1
                    next.append((r, c + 1))
            
            height += 1

        return ret