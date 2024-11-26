class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:

        possibilities = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]

        exist = set()
        ret = []

        for row in board:
            for num in row:
                ret.append(str(num))

        cur = "".join(ret)
        exist.add(cur)

        queue = [cur]
        next = []
        breadth = 0

        while queue:

            cur = queue.pop()
            lst = [i for i in cur]

            if cur == '123450':
                return breadth

            for i in range(6):
                if cur[i] != '0': continue
                
                for pos in possibilities[i]:

                    temp = lst[i]
                    lst[i] = lst[pos]
                    lst[pos] = temp

                    new = "".join(lst)
                    if new not in exist:
                        next.append(new)
                        exist.add(new)

                    lst[pos] = lst[i]
                    lst[i] = temp
                    
            if not queue:
                queue = next.copy()
                next = []
                breadth += 1
            
        return -1