# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root: return []

        ret = [root.val]
        queue, next = [root], []

        while queue:

            cur = queue.pop(0)

            if cur.left: next.append(cur.left)
            if cur.right: next.append(cur.right)

            if not queue and next:
                
                ret.append(max([node.val for node in next]))

                queue = next.copy()
                next = []

        return ret

        