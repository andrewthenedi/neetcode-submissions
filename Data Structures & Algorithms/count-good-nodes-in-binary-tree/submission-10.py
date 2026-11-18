# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def iterative(self, root: TreeNode) -> int:
        # T: O(N) | S: O(N)
        # N = Size of root
        queue = collections.deque([(root, root.val)])
        result = 0
        while queue:
            node, max_val = queue.popleft()
            if node.val >= max_val:
                max_val = node.val
                result += 1
            if node.left:
                queue.append((node.left, max_val))
            if node.right:
                queue.append((node.right, max_val))
        return result

    def recursive(self, root: TreeNode) -> int:
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        def dfs(node: Optional[TreeNode], max_val: int) -> int:
            if not node:
                return 0
            curr_good = 0
            if node.val >= max_val:
                max_val = node.val
                curr_good = 1
            return curr_good + dfs(node.left, max_val) + dfs(node.right, max_val)
        return dfs(root, root.val)

    def goodNodes(self, root: TreeNode) -> int:
        # return self.iterative(root)
        return self.recursive(root)
        