# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(N) | O(H_N)
        if not(p or q):
            return True
        if not(p and q) or p.val != q.val:
            return False
        return self.isSametree(p.left, q.left) and self.isSametree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # T: O(M * N) | S: O(H_M + H_N)
        # M = Size of root nodes
        # N = Size of subroot nodes
        # H_M = Height of root nodes: O(LOG M) if balanced else O(M)
        # H_N = Height of subRoot nodes: O(LOG N) if balanced else O(N)
        if not root:
            return False
        if root.val == subRoot.val and self.isSametree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
