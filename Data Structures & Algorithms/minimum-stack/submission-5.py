class MinStack:
    # T: O(1) | S: O(N)
    # N = Size of min_stack

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        min_val = min(self.getMin(), val) if self.min_stack else val
        self.min_stack.append([val, min_val])

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]
