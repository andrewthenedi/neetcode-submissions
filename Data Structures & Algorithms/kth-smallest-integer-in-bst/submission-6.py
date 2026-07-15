# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root: O(LOG N) if balanced; O(N) if skewed
        def recursive(node: Optional[TreeNode]):
            nonlocal k
            if not node:
                return -1
            left_val = recursive(node.left)
            if left_val >= 0:
                return left_val
            if k == 1:
                return node.val
            k -= 1
            return recursive(node.right)
        return recursive(root)
