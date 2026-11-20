# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # T: O(N) | S: O(H)
        # N = Size of tree
        # H = Height of tree; O(LOG N) if balanced else O(N)
        idx_pre = idx_in = 0
        def dfs(limit: int) -> Optional[TreeNode]:
            nonlocal idx_pre, idx_in
            if idx_pre == len(preorder):
                return None
            if inorder[idx_in] == limit:
                idx_in += 1
                return None
            node = TreeNode(preorder[idx_pre])
            idx_pre += 1
            node.left = dfs(node.val)
            node.right = dfs(limit)
            return node
        return dfs(math.inf)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.recursive(preorder, inorder)
        