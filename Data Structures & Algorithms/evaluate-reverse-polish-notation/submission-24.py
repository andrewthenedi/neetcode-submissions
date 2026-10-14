class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # T: O(N) | S: O(N)
        # N = Size of tokens
        operators = {"+", "-", "*", "/"}
        stack = []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand_2, operand_1 = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(operand_1 + operand_2)
                elif token == "-":
                    stack.append(operand_1 - operand_2)
                elif token == "*":
                    stack.append(operand_1 * operand_2)
                elif token == "/":
                    stack.append(int(operand_1 / operand_2))
        return stack[0]
