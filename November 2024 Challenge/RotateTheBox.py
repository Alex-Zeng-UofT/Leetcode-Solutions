class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:

            m, n = len(box), len(box[0])
            rotated = []

            for i in range(n):

                cur = []
                for j in range(m):
                    cur.append(box[j][i])

                cur.reverse()
                rotated.append(cur.copy())

            for col in range(m):

                lowest = n - 1

                for row in range(n - 1, -1, -1):
                    
                    if rotated[row][col] == '#':
                        rotated[row][col] = '.'
                        rotated[lowest][col] = '#'
                        lowest -= 1
                    
                    if rotated[row][col] == '*':
                        lowest = row - 1

            return rotated

                    