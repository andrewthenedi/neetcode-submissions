# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Iterative
        # T: O(MIN(M, N)) | S: O(MIN(W_M, W_N))
        # M = Size of p
        # N = Size of q
        # W_M = Width of p
        # W_N = Width of q
        if p and q:
            queue = collections.deque([(p, q)])
        elif p or q:
            return False
        else:
            return True
        while queue:
            for _ in range(len(queue)):
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
    #     # T: O(MIN(M, N)) | S: O(MIN(H_M, H_N))
    #     # M = Size of p
    #     # N = Size of q
    #     # H_M = Height of p: O(LOG M) if balanced tree / O(M) if skewed tree
    #     # H_N = Height of q: O(LOG N) if balanced tree / O(N) if skewed tree
    #     if not(p or q):
    #         return True
    #     if p and q and p.val == q.val:
    #         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    #     return False
