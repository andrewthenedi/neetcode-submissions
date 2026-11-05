# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(N)
        # N = Size of roots
        if not(p or q):
            return True
        if not(p and q):
            return False
        queue = collections.deque([(p, q)])
        while queue:
            node_p, node_q = queue.popleft()
            if node_p.val != node_q.val:
                return False
            if node_p.left and node_q.left:
                queue.append((node_p.left, node_q.left))
            elif node_p.left or node_q.left:
                return False
            if node_p.right and node_q.right:
                queue.append((node_p.right, node_q.right))
            elif node_p.right or node_q.right:
                return False
        return True

    def recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(H)
        # N = Size of roots
        # H = Height of roots | O(LOG N) if balanced else O(N)
        if not(p or q):
            return True
        if not(p and q) or p.val != q.val:
            return False
        return self.recursive(p.left, q.left) and self.recursive(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.iterative(p, q)
        # return self.recursive(p, q)
