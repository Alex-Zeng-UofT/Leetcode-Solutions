# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        ret = 0
        sigma = 0
        highest = 0 - math.inf
        count = 1

        queue = [root]
        breadth = []

        while queue:

            node = queue.pop(0)

            sigma += node.val
            if node.left: breadth.append(node.left)
            if node.right: breadth.append(node.right)

            if not queue:
                if sigma > highest:
                    highest = sigma
                    ret = count
                count += 1
                sigma = 0
                queue = breadth.copy()
                breadth = []

        return ret
        