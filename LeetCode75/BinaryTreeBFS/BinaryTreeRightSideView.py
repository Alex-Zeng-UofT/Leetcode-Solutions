# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []

        ret = []

        queue = [root]
        next_breadth = []

        while queue:

            node = queue.pop(0)
        
            if node.left:
                next_breadth.append(node.left)
            if node.right:
                next_breadth.append(node.right)
            
            if not queue:
                ret.append(node.val)
                queue = next_breadth.copy()
                next_breadth = []
            
        return ret
