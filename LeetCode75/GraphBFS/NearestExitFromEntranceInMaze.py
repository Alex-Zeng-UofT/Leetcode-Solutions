class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        count = 1

        queue = [entrance]
        temp = []

        n, m = len(maze), len(maze[0])
        maze[entrance[0]][entrance[1]] = '+'

        while len(queue) > 0:

            pos = queue.pop(0)

            r, c = pos[0], pos[1]

            if r > 0 and maze[r - 1][c] == '.':
                if r == 1 or c == 0 or c == m - 1: break
                temp.append([r - 1, c])
                maze[r - 1][c] = '+'

            if c > 0 and maze[r][c - 1] == '.':
                if c == 1 or r == 0 or r == n - 1: break
                temp.append([r, c - 1])
                maze[r][c - 1] = '+'

            if r < n - 1 and maze[r + 1][c] == '.':
                if r == n - 2 or c == 0 or c == m - 1: break
                temp.append([r + 1, c])
                maze[r + 1][c] = '+'

            if c < m - 1 and maze[r][c + 1] == '.':
                if c == m - 2 or r == 0 or r == n - 1: break
                temp.append([r, c + 1])
                maze[r][c + 1] = '+'

            if len(queue) == 0:
                if len(temp) == 0: return -1
                count += 1
                queue = temp.copy()
                temp = []

        return count