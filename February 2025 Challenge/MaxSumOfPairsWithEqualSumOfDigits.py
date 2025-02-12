class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        map = {}
        highest = -1

        for num in nums:

            val, i = 0, num

            while i > 0:
                val += i % 10
                i //= 10

            if val not in map:
                map[val] = [num]
                continue
            elif len(map[val]) < 2:
                map[val].append(num)
            else:
                idx = 1 if map[val][0] > map[val][1] else 0
                map[val][idx] = num
            
            highest = max(map[val][0] + map[val][1], highest)
                
        return highest
        