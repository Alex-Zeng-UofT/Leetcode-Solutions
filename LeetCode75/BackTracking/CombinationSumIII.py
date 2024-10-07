class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(k: int, n: int, temp: List, ret: List, cur: int) -> None:

            if n < 0: return

            if k == 0:
                if n == 0: ret.append(temp)
                return

            for i in range(cur, 10):
                newTemp = temp.copy()
                newTemp.append(i)
                backtrack(k - 1, n - i, newTemp, ret, i + 1)

        ret = []
        backtrack(k, n, [], ret, 1)

        return ret

