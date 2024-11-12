class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        
        items.sort()
        sorted_queries = sorted(queries)

        map = {}

        cur_item = 0
        cur_max = 0

        for query in sorted_queries:
            
            while cur_item < len(items) and items[cur_item][0] <= query:
                cur_max = max(cur_max, items[cur_item][1])
                cur_item += 1
            
            map[query] = cur_max

        ret = []

        for query in queries:
            ret.append(map[query])

        return ret