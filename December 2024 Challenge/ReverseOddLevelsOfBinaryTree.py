# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        is_odd = False
        queue, next = [root], []

        while queue:

            cur = queue.pop(0)

            if cur.left: next.append(cur.left)
            if cur.right: next.append(cur.right)

            if not queue:

                if not is_odd and next:
                    for i in range(len(next) // 2):
                        temp = next[i].val
                        next[i].val = next[len(next) - 1 - i].val
                        next[len(next) - 1 - i].val = temp
                
                queue = next.copy()
                next = []
                is_odd = not is_odd

        return root