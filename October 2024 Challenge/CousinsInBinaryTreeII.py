# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def calc_update(siblings: List, level_sum: int) -> None:

            cur_sum = 0

            for sib_node, idx in siblings:
                cur_sum += sib_node.val

            for sib_node, idx in siblings:
                sib_node.val = level_sum - cur_sum

            return
        
        queue, next = [root], []
        level_sums = []

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

        i, level = 0, 0
        queue, next = [(root, i)], []
        siblings = []

        while queue:

            node, serial = queue.pop(0)
            
            if not siblings or siblings[0][1] == serial:
                siblings.append((node, serial))
            else:
                calc_update(siblings, level_sums[level])
                siblings = [(node, serial)]

            if node.left: next.append((node.left, i))
            if node.right: next.append((node.right, i))
            
            i += 1

            if not queue:
                queue = next.copy()
                next = []
                i = 0
                calc_update(siblings, level_sums[level])
                siblings = []
                level += 1

        return root