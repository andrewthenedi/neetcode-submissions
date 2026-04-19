# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive
    def recursive(self, node: Optional[TreeNode], depth: int) -> int:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not node:
            return depth
        left_depth = self.recursive(node.left, depth + 1)
        right_depth = self.recursive(node.right, depth + 1)
        return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root, 0)
