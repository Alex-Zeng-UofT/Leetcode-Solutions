class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        sorted = []

        for i, lst in enumerate(nums):
            for num in lst:
                sorted.append((num, i))
        
        sorted.sort()

        visited = [10000000 for i in nums]
        ret = [0, 10000000]

        complete = False
        beg = 0

        for num, i in sorted:
            
            visited[i] = num

            if not complete:
                complete = not 10000000 in visited
                if not complete: continue
            
            while beg < len(sorted) and visited[sorted[beg][1]] != sorted[beg][0]:
                beg += 1
            
            min_num = sorted[beg][0]
            range = ret[1] - ret[0]

            if num - min_num < range or num - min_num == range and min_num < ret[0]:
                ret = [min_num, num]

        return ret