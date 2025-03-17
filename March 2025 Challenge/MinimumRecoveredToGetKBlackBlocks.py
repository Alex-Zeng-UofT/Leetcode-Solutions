class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        ret = float('inf')
        cur = 0
        left = 0

        for right in range(len(blocks)):

            if blocks[right] == "W":
                cur += 1

            if right - left + 1 == k:

                ret = min(ret, cur)
                
                if blocks[left] == 'W':
                    cur -= 1
                
                left += 1

        return ret