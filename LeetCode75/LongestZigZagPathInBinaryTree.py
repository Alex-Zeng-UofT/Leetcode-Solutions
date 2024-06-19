# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def zigzag(root: Optional[TreeNode], isLeft: bool, depth: int) -> int:

            if not root: return depth

            if isLeft:
                depth = max(
                    depth,
                    zigzag(root.right, False, depth + 1),
                    zigzag(root.left, True, 0),
                )

            else:
                depth = max(
                    depth,
                    zigzag(root.left, True, depth + 1),
                    zigzag(root.right, False, 0),
                )

            return depth

        return max(zigzag(root.left, True, 0), zigzag(root.right, False, 0))