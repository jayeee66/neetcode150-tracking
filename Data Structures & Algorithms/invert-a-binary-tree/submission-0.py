# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Swap both ondes
        temp = root.left
        root.left = root.right
        root.right = temp
        
        # Recursively call the same function on the children
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return the original root
        return root
