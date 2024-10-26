# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        map = {}

        def max_depth(root: Optional[TreeNode]) -> int:
            nonlocal map

            if not root: return -1

            depth = 1 + max(max_depth(root.left), max_depth(root.right))

            map[root.val] = depth

            return depth

        max_depth(root)

        queue, next = [root], []
        levels, cur_level = [], []
        level_mapper = {}

        while queue:

            node = queue.pop(0)
            
            if node.left: next.append(node.left)
            if node.right: next.append(node.right)
            
            level_mapper[node.val] = len(levels)
            cur_level.append(map[node.val])

            if not queue:
                queue = next.copy()
                next = []
                levels.append(cur_level.copy())
                cur_level = []

        ret = []
        maxes = []

        for level in levels:

            first, second = -1, -1

            for height in level:
                if height >= first:
                    second = first
                    first = height
                elif height > second:
                    second = height

            maxes.append((first, second))

        for query in queries:
            level = level_mapper[query]
            ret.append(level + (maxes[level][0] if maxes[level][0] != map[query] else maxes[level][1]))

        return ret