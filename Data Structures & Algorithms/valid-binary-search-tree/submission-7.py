# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, node: Optional[TreeNode], low: int, high: int) -> bool:
        # T: O(N) | S: O(H)
        # N = Size of node
        # H = Height of node: O(LOG N) if balanced; O(N) if skewed
        if not node:
            return True
        if not(low < node.val < high):
            return False
        return self.recursive(node.left, low, node.val) \
            and self.recursive(node.right, node.val, high)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recursive(root, -math.inf, math.inf)
