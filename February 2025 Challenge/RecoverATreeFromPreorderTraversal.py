# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        map = {}
        level = -1
        i = 0

        while i < len(traversal):

            if traversal[i] == '-':
                level += 1
                i += 1
                continue
            
            num = []

            while i < len(traversal) and traversal[i] != '-':
                num.append(traversal[i])
                i += 1

            val = int("".join(num))
            node = TreeNode(val, None, None)
            
            if level >= 0:
                if not map[level].left:
                    map[level].left = node
                else:
                    map[level].right = node

            map[level + 1] = node
            level = -1

        return map[0]
        