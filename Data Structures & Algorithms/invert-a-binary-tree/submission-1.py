# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Use queue first in first out
        queue = deque([root])
        while queue:
            # pop first node
            node = queue.popleft()
            # swap children
            node.left, node.right = node.right, node.left
            # put adjacent nodes in
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
            