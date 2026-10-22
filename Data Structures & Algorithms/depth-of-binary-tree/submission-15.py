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
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        if not node:
            return depth
        return max(self.recursive(node.left, depth + 1), self.recursive(node.right, depth + 1))
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root, 0)
