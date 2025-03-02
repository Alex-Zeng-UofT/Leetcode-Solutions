class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        
        ret = []

        def appender(arr, idx, val):
            if arr and arr[-1][0] == idx:
                arr[-1][1] += val
            else:
                arr.append([idx, val])

        i, j = 0, 0
        n, m = len(nums1), len(nums2)
        cur = -1

        while i < n or j < m:

            if i < n and j < m:
                if nums1[i][0] < nums2[j][0]:
                    appender(ret, nums1[i][0], nums1[i][1])
                    i += 1
                else:
                    appender(ret, nums2[j][0], nums2[j][1])
                    j += 1
            elif i < n:
                appender(ret, nums1[i][0], nums1[i][1])
                i += 1
            else:
                appender(ret, nums2[j][0], nums2[j][1])
                j += 1

        return ret