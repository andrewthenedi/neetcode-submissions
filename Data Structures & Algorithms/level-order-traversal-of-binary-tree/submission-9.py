# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive(self, root: Optional[TreeNode]) -> List[List[int]]:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        result = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return None
            if len(result) == depth:
                result.append([])
            result[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return result

    def iterative(self, root: Optional[TreeNode]) -> List[List[int]]:
        # T: O(N) | S: O(N)
        # N = Size of root
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            sub_result = []
            for _ in range(len(queue)):
                node = queue.popleft()
                sub_result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sub_result)
        return result

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.recursive(root)
        # return self.iterative(root)

