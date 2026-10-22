# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Iterative
    def iterative(self, root: Optional[TreeNode]) -> int:
        # T: O(N) | S: O(N)
        # N = Size of root
        depth = 0
        if not root:
            return depth
        queue = collections.deque([root])
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return depth


    # Recursive
    def recursive(self, node: Optional[TreeNode], depth: int) -> int:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        if not node:
            return depth
        return max(self.recursive(node.left, depth + 1), self.recursive(node.right, depth + 1))
        

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.iterative(root)
        # return self.recursive(root, 0)
