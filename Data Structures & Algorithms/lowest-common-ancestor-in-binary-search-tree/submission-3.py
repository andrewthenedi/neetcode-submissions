# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root: O(N) if root is balanced; O(LOG N) if root is skewed
        if not root:
            return None
        left_node = right_node = None
        if max(p.val, q.val) < root.val:
            left_node = self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val:
            right_node = self.lowestCommonAncestor(root.right, p, q)
        return left_node or right_node or root
