# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # # Iterative
        # # T: O(N) | S: O(N)
        # # N = Size of root
        # if not root:
        #     return None
        # queue = collections.deque([root])
        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         node.left, node.right = node.right, node.left
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        # return root

        # Recursive
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
