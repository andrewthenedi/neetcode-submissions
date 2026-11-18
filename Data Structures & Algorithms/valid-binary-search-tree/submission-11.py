# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, root: TreeNode) -> bool:
        queue = collections.deque([root])

    def recursive(self, root: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        def dfs(node: Optional[TreeNode], low: int, high: int) -> bool:
            if not node:
                return True
            if not(low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, -math.inf, math.inf)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.iterative(root)
        return self.recursive(root)
        