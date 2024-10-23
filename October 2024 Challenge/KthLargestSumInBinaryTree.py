# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        level_sums = []
        queue = [root]
        next = []

        cur_sum = 0

        while queue:

            node = queue.pop(0)
            cur_sum += node.val

            if node.left: next.append(node.left)
            if node.right: next.append(node.right)

            if not queue:
                level_sums.append(cur_sum)
                cur_sum = 0
                queue = next.copy()
                next = []

        level_sums.sort(reverse=True)

        return -1 if k > len(level_sums) else level_sums[k - 1]