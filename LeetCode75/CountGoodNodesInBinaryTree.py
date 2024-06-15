# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(cur: TreeNode, greatest: int) -> int:
            
            if not cur: return 0

            if cur.val >= greatest:
                return 1 + dfs(cur.left, cur.val) + dfs(cur.right, cur.val)

            return dfs(cur.left, greatest) + dfs(cur.right, greatest)

        return dfs(root, 0 - math.inf)