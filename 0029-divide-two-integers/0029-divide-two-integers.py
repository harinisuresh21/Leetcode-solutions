class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX =  2**31 - 1
        INT_MIN = -2**31

        # Handle overflow edge case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Work with positives, track sign separately
        negative = (dividend < 0) != (divisor < 0)
        a = abs(dividend)
        b = abs(divisor)

        quotient = 0

        while a >= b:
            temp = b
            multiple = 1

            # Double temp until it exceeds dividend
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            quotient += multiple

        return -quotient if negative else quotient