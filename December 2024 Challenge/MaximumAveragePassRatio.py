class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(passes: int, total: int) -> float:
            return -((passes + 1) / (total + 1) - passes / total)

        pq = []
        for pair in classes:
            pq.append((gain(pair[0], pair[1]), pair[0], pair[1]))

        heapify(pq)

        for i in range(extraStudents):
            cur = heappop(pq)
            heappush(pq, (gain(cur[1] + 1, cur[2] + 1), cur[1] + 1, cur[2] + 1))
        
        ret = 0
        for pair in pq:
            ret += pair[1] / pair[2]

        return ret / len(classes)