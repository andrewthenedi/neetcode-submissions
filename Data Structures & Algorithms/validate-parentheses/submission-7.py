class Solution:
    def isValid(self, s: str) -> bool:
        # T: O(N) | S: O(N)
        # N = Length of s
        stack = []
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for c in s:
            if c in open_to_close:
                stack.append(c)
            elif not stack or open_to_close[stack.pop()] != c:
                return False
        return not stack
