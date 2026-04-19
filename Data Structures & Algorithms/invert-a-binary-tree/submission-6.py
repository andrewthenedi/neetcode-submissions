# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T: O(N) | S: O(Height)
        # Height = O(LOG N) / O(N)
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

    # Recursive
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # T: O(N) | S: O(Height)
    #     # Height = O(LOG N) / O(N)
    #     if not root:
    #         return None
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
