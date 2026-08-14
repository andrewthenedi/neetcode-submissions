class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # T: O(N) | S: O(N)
        # N = Size of tokens
        stack = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num_2, num_1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(num_1 + num_2)
                elif token == '-':
                    stack.append(num_1 - num_2)
                elif token == '*':
                    stack.append(num_1 * num_2)
                elif token == '/':
                    stack.append(int(num_1 / num_2))
        return stack[0]
