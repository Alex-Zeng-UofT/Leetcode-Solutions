class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        n = len(nums)
        global_sort = sorted(nums)
        clusters = [deque()]
        num_to_cluster = {}

        for i in range(n):

            num = global_sort[i]

            if i != 0 and num - global_sort[i - 1] > limit:
                clusters.append(deque())

            clusters[-1].append(num)
            num_to_cluster[num] = len(clusters) - 1


        for i in range(n):
            nums[i] = clusters[num_to_cluster[nums[i]]].popleft()

        return nums