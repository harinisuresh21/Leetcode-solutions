class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current: list[str], open: int, close: int):
            # Base case: used all n pairs
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            # Add open bracket if we still have some left
            if open < n:
                current.append("(")
                backtrack(current, open + 1, close)
                current.pop()

            # Add close bracket only if it won't become unmatched
            if close < open:
                current.append(")")
                backtrack(current, open, close + 1)
                current.pop()

        backtrack([], 0, 0)
        return result