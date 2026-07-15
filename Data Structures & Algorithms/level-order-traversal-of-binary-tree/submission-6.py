# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # T: O(N) | S: O(W)
        # N = Size of root
        # W = Width of root: O(N)
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            sub_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                sub_result.append(node.val)
            result.append(sub_result)
        return result
