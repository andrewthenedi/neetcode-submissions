class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # T: O(N) | O(N)
        # N = Size of tokens
        nums = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                nums.append(int(token))
            else:
                num_2, num_1 = nums.pop(), nums.pop()
                if token == "+":
                    nums.append(num_1 + num_2)
                elif token == "-":
                    nums.append(num_1 - num_2)
                elif token == "*":
                    nums.append(num_1 * num_2)
                elif token == "/":
                    nums.append(int(num_1 / num_2))
        return nums[0]
