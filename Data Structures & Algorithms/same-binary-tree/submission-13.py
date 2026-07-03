# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Recursive
        # T: O(MIN(M, N)) | S: O(MIN(H_M, H_N))
        # M = Size of p
        # N = Size of q
        # H_M = Height of p: O(LOG M) if balanced tree / O(M) if skewed tree
        # H_N = Height of q: O(LOG N) if balanced tree / O(N) if skewed tree
        if not(p or q):
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
