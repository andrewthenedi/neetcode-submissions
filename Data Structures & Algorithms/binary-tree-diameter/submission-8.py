# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursive
    def recursive(self, node: Optional[TreeNode]) -> (int, int):
        # T: O(N) | S: O(H)
        # N = Size of root
        # H = Height of root; O(LOG N) if balanced else O(N)
        if not node:
            return -1, 0
        left_length, left_diameter = self.recursive(node.left)
        right_length, right_diameter = self.recursive(node.right)
        curr_diameter = 2 + left_length + right_length
        max_diameter = max(curr_diameter, left_diameter, right_diameter)
        max_length = 1 + max(left_length, right_length)
        return max_length, max_diameter


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recursive(root)[1]


