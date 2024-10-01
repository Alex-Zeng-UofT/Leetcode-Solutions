class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        n = len(arr)
        
        for i in range(len(arr)):
            arr[i] %= k

        arr = sorted(arr)
        cur = 0
        
        while cur < n and arr[cur] == 0:
            cur += 1

        if cur % 2 != 0: return False
        
        for i in range((len(arr) - cur) // 2):
            if arr[i + cur] + arr[-(i + 1)] != k:
                return False

        return True