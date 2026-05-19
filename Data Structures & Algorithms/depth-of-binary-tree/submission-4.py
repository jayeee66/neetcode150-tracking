# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if not root:
            return depth
        
        queue = deque([root])
        # Loop continues as long as there are nodes to process in the next layer
        while queue:
            # Process all nodes belonging to the current level in one batch
            for i in range(len(queue)):
                node = queue.popleft()
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # After the for-loop finishes, one entire level has been completely peeled off.
            # Increment the depth counter.
            depth += 1
            # print(depth)
        return depth

        
        
