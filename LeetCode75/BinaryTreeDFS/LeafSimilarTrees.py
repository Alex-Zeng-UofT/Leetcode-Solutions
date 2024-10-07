# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leafs1, leafs2 = [], []

        def traverse(root: TreeNode, lst: List[int]) -> None:
            
            if root == None: return

            if root.left == None and root.right == None:
                lst.append(root.val)
                return

            traverse(root.left, lst)
            traverse(root.right, lst)

        traverse(root1, leafs1)
        traverse(root2, leafs2)

        return leafs1 == leafs2        
