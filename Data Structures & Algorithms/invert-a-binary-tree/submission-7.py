# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # T: O(N) | S: O(MAX Width)
        # MAX Width = N
        if not root:
            return None
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

    # Recursive
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     # T: O(N) | S: O(Height)
    #     # Height = O(LOG N) / O(N)
    #     if not root:
    #         return None
    #     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #     return root
