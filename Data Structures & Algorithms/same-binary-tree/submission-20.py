# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative
        # T: O(N) | S: O(W)
        # N = The lesser size among p and q
        # W = The lesser width among p and q
        if p and q:
            queue = collections.deque([(p, q)])
        elif p or q:
            return False
        else:
            return True
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
        

    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     # Recursive
    #     # T: O(N) | S: O(H)
    #     # N = The lesser nodes among p and q
    #     # H = The smaller height among p and q: O(LOG N) if balanced / O(N) if skewed
    #     if not(p or q):
    #         return True
    #     if p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False
