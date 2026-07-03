# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative
        # T: O(N) | S: O(W)
        # N = Size of root
        # W = Maximum width of root: O(N)
        queue = collections.deque([root]) if root else None
        depth = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
        return depth

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # Recursive
    #     # T: O(N) | S: O(H)
    #     # N = Size of root
    #     # H = Height of root: O(LOG N) if balanced root / O(N) if skewed root
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
