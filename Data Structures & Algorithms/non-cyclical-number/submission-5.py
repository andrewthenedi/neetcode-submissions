class Solution:
    def sumSquaresDigits(self, n: int) -> int:
        sum_squares_digits = 0
        while n > 0:
            sum_squares_digits += (n % 10) ** 2
            n //= 10
        return sum_squares_digits

    def isHappy(self, n: int) -> bool:
        # T: O(N) | S: O(1)
        slow = self.sumSquaresDigits(n)
        fast = self.sumSquaresDigits(self.sumSquaresDigits(n))
        if slow == 1 or fast == 1:
            return True
        while slow != fast:
            slow = self.sumSquaresDigits(slow)
            fast = self.sumSquaresDigits(self.sumSquaresDigits(fast))
            if slow == 1 or fast == 1:
                return True
        return False
