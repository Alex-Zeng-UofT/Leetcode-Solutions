# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        counter = 0

        def dfs(root: Optional[TreeNode], target: int) -> None:
            nonlocal counter

            if not root: return

            if root.val == target: counter += 1

            dfs(root.left, target - root.val)
            dfs(root.right, target - root.val)

            return

        def dfs2(root: Optional[TreeNode]) -> None:

            if not root: return

            dfs(root, targetSum)

            dfs2(root.left)
            dfs2(root.right)

            return

        dfs2(root)

        return counter