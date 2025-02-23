# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        map = {}
        stack = []
        n = len(preorder)
        j = 0

        for i in range(n):
            
            stack.append(preorder[i])
            node = TreeNode(preorder[i], None, None)

            if map:

                prev = map[stack[-2]]

                if not prev.left:
                    prev.left = node
                else:
                    prev.right = node
            
            while stack and stack[-1] == postorder[j]:
                j += 1
                stack.pop()

            map[preorder[i]] = node

        return map[preorder[0]]