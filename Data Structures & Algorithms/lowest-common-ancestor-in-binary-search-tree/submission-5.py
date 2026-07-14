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
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                break
        return root

    # def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    #     # Recursive
    #     # T: O(H) | S: O(H)
    #     # H = Height of root: O(LOG N) if root is balanced; O(N) if root is skewed
    #     if not root:
    #         return None
    #     left_node = right_node = None
    #     if max(p.val, q.val) < root.val:
    #         left_node = self.lowestCommonAncestor(root.left, p, q)
    #     elif min(p.val, q.val) > root.val:
    #         right_node = self.lowestCommonAncestor(root.right, p, q)
    #     return left_node or right_node or root
