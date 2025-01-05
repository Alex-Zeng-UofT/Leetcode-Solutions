# Leetcode Interview 150 Strategy

**Chapters**

1. [Array/String](#arraystring)


## Array/String

### Merge Sorted Array (EASY)

> Take advantage of the fact that both given array ares already sorted, so we can use a two pointer approach to compare indices and merge.
> This can be done in reverse order to allow for modification in place since nums1 contains '0' paddings in the end.

- **Time Complexity**: O(M + N)
- **Space Complexity**: O(1)

```python
def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

    i, j = m - 1, n - 1
    cur = len(nums1) - 1
  
    while i >= 0 or j >= 0:
    
        # case: both arrays are non-empty
        if i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j]
                j -= 1
    
        # case: nums2 in empty
        elif i >= 0:
            nums1[cur] = nums1[i]
            i -= 1
            
        # case: nums1 in empty
        else:
            nums1[cur] = nums2[j]
            j -= 1
        
        cur -= 1
    
    return
```

### Remove Element (EASY)

> Use a two pointer approach, one for iterating and one for keeping track of positions of subarray not containing the element .

- **Time Complexity**: O(N)
- **Space Complexity**: O(1)

```python
def removeElement(self, nums: List[int], val: int) -> int:
    
    pos = 0

    for num in nums:

        if num == val: 
            continue

        nums[pos] = num
        pos += 1

    return pos
```
