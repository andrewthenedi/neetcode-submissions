# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative
    def iterative(self, node: Optional[TreeNode]) -> int:
        # T: O(N) | S: O(W)
        # W = O(N)
        if not node:
            return 0
        max_depth = 0
        queue = collections.deque([node])
        while queue:
            max_depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return max_depth

    # Recursive
    def recursive(self, node: Optional[TreeNode]) -> int:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not node:
            return 0
        return 1 + max(self.recursive(node.left), self.recursive(node.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iterative(root)
        # return self.recursive(root)
