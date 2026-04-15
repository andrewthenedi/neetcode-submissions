class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(N) | S: O(N)
        close_to_open = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in close_to_open:
                stack.append(c)
            elif not stack or stack[-1] != close_to_open[c]:
                return False
            else:
                stack.pop()
        return not stack
