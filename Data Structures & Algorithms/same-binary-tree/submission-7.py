# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(W)
        # W = O(N)
        if not(p or q):
            return True
        if not(p and q):
            return False
        queue = collections.deque([(p, q)])
        while queue:
            p, q = queue.popleft()
            if p.val != q.val:
                return False
            
            if not(p.left or q.left):
                pass
            elif not(p.left and q.left):
                return False
            else:
                queue.append((p.left, q.left))
            
            if not(p.right or q.right):
                pass
            elif not(p.right and q.right):
                return False
            else:
                queue.append((p.right, q.right))
        return True

    def recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not(p or q):
            return True
        if not(p and q) or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.iterative(p, q)
        # return self.recursive(p, q)
