class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        nums = [-num for num in nums]

        heapify(nums)
        score = 0

        for i in range(k):

            head = heappop(nums)
            score -= head
            heappush(nums, head // 3)

        return score
