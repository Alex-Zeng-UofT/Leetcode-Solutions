# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):

        self.vals = set()
        
        def dfs(node, val, dir):
            
            if not node: return

            node_val = 0

            if dir == 1:
                node_val = val * 2 + 2
            elif dir == -1:
                node_val = val * 2 + 1

            self.vals.add(node_val)

            dfs(node.left, node_val, -1)
            dfs(node.right, node_val, 1)

            return

        dfs(root, 0, 2)
        

    def find(self, target: int) -> bool:
        return target in self.vals
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)