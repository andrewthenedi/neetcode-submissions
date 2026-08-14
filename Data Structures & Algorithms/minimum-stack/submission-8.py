class MinStack:
    # T: O(1) | S: O(N)
    # N = Size of stack

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = val
        if self.stack and self.getMin() < min_val:
            min_val = self.getMin()
        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
