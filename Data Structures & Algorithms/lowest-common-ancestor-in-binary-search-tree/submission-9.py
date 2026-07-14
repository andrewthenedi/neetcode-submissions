# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Iterative
        # T: O(H) | S: O(1)
        # H = Height of root: O(LOG N) if root is balanced; O(N) if root is skewed
        high, low = max(p.val, q.val), min(p.val, q.val)
        while root:
            if high < root.val:
                root = root.left
            elif low > root.val:
                root = root.right
            else:
                break
        return root

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Recursive
        # T: O(H) | S: O(H)
        # H = Height of root: O(LOG N) if root is balanced; O(N) if root is skewed
        high, low = max(p.val, q.val), min(p.val, q.val)
        if high < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif low > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
