class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        for i in range(k - 1):
            colors.append(colors[i])

        end = 0
        ret = 0

        for beg in range(len(colors) - k + 1):

            end = max(end, beg)

            while end < len(colors) - 1 and colors[end] + colors[end + 1] == 1:
                end += 1
            
            if end - beg + 1 >= k:
                ret += 1

        return ret
            