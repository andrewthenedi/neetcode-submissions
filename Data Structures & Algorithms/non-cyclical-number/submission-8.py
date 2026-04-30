class Solution:
    def sumSquaresDigits(self, n: int) -> int:
        sum_squares_digits = 0
        while n > 0:
            sum_squares_digits += (n % 10) ** 2
            n //= 10
        return sum_squares_digits

    def isHappy(self, n: int) -> bool:
        # T: O(LOG N) | S: O(1)
        slow, fast = n, self.sumSquaresDigits(n)
        while slow != fast:
            slow = self.sumSquaresDigits(slow)
            fast = self.sumSquaresDigits(self.sumSquaresDigits(fast))
        return slow == 1
