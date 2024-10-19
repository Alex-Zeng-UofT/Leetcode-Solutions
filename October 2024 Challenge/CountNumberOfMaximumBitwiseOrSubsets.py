class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        ret = []

        def backtrack(nums: List[int], lst: List[int], ret: List[List[int]]):
            temp = nums.copy()
            new_lst = lst.copy()

            for i in range(len(temp)):
                new_lst.append(temp.pop(0))
                ret.append(new_lst.copy())
                backtrack(temp, new_lst, ret)
                new_lst.pop()

        backtrack(nums, [], ret)

        count, maximum = 0, 0

        for lst in ret:

            cur = 0
            for num in lst:
                cur |= num
            
            if cur > maximum:
                count = 1
                maximum = cur
            elif cur == maximum: count += 1

        return count
        