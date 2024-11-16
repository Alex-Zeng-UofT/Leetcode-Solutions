class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        n = len(arr)
        right = n - 1

        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1

        ret = right
        left = 0
        
        while left < right and (left == 0 or arr[left] >= arr[left - 1]):
            
            while right < n and arr[left] > arr[right]:
                right += 1
            
            ret = min(ret, right - left - 1)
            left += 1

        return ret