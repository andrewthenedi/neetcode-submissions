# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, node: TreeNode, p: TreeNode, q: TreeNode, high: int, low: int) -> TreeNode:
        # T: O(N) | S: O(1)
        # N = Size of root nodes
        while True:
            if high < node.val:
                node = node.left
            elif low > node.val:
                node = node.right
            else:
                return node

    def recursive(self, node: TreeNode, p: TreeNode, q: TreeNode, high: int, low: int) -> TreeNode:
        # T: O(N) | S: O(H)
        # N = Size of root nodes
        # H = Height of root nodes: O(LOG N) if balanced else O(N)
        if high < node.val:
            return self.recursive(node.left, p, q, high, low)
        if low > node.val:
            return self.recursive(node.right, p, q, high, low)
        return node

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        high, low = max(p.val, q.val), min(p.val, q.val)
        return self.iterative(root, p, q, high, low)
        # return self.recursive(root, p, q, high, low)
        