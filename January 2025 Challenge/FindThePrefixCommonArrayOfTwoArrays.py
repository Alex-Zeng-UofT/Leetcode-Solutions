class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        a, b = set(), set()
        c = []
        cur = 0

        for i in range(len(A)):

            if A[i] == B[i]:
                cur += 1
            if A[i] in b:
                cur += 1
            if B[i] in a:
                cur += 1

            a.add(A[i])
            b.add(B[i])

            c.append(cur)

        return c