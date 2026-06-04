# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# dfs
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # all the left nodes have to to less than root
        # all the right nodes have to greater than root 
        # need to compare with root node instead of parent node
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return dfs(node.left, min_val, node.val) and dfs(node.right, node.val, max_val)
        # first node between -∞ and ∞
        return dfs(root, float('-inf'), float('inf'))