class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        max_idx = []
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        for idx, query in enumerate(queries):
            a, b = query
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )

        for idx, height in enumerate(heights):

            while max_idx and max_idx[0][0] < height:
                _, q_idx = heapq.heappop(max_idx)
                results[q_idx] = idx
            
            for element in store_queries[idx]:
                heapq.heappush(max_idx, element)

        return results