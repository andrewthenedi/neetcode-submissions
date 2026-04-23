# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursive_1(self, node: Optional[TreeNode]) -> int:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not node:
            return -1
        left_height = self.recursive_1(node.left)
        if left_height == -2:
            return -2
        right_height = self.recursive_1(node.right)
        if right_height == -2:
            return -2
        if abs(left_height - right_height) > 1:
            return -2
        return 1 + max(left_height, right_height)

    def recursive(self, node: Optional[TreeNode]) -> Tuple[int, bool]:
        # T: O(N) | S: O(H)
        # H = O(LOG N) / O(N)
        if not node:
            return -1, True
        left_height, is_left_balanced = self.recursive(node.left)
        right_height, is_right_balanced = self.recursive(node.right)
        is_curr_balanced = abs(left_height - right_height) <= 1
        is_tree_balanced = is_curr_balanced and is_left_balanced and is_right_balanced
        return 1 + max(left_height, right_height), is_tree_balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recursive_1(root) != -2
        # return self.recursive(root)[1]
