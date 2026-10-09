class MinStack:

    def __init__(self):
        # T: O(1) | S: O(N)
        # N = Size of min_stack
        self.min_stack = []

    def push(self, val: int) -> None:
        # T: O(1) | S: O(1)
        min_val = val
        if self.min_stack:
            min_val = min(min_val, self.min_stack[-1][1])
        self.min_stack.append((val, min_val))

    def pop(self) -> None:
        # T: O(1) | S: O(1)
        self.min_stack.pop()

    def top(self) -> int:
        # T: O(1) | S: O(1)
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        # T: O(1) | S: O(1)
        return self.min_stack[-1][1]
