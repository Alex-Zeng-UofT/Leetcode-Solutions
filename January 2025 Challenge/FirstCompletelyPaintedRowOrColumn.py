class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        
        m, n = len(mat), len(mat[0])
        rows, cols = {}, {}
        r_fulfill, c_fulfill = [0] * m, [0] * n

        for i in range(m):
            for j in range(n):
                rows[mat[i][j]] = i
                cols[mat[i][j]] = j

        for i in range(len(arr)):

            r_fulfill[rows[arr[i]]] += 1
            c_fulfill[cols[arr[i]]] += 1
            
            if r_fulfill[rows[arr[i]]] == n or c_fulfill[cols[arr[i]]] == m:
                return i

        return 42