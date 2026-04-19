# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive
    def recursive(self, node: Optional[TreeNode]) -> int:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not node:
            return 0
        return 1 + max(self.recursive(node.left), self.recursive(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root)
