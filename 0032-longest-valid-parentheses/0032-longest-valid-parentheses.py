class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Initialize stack with -1 to handle the base case for length calculation
        stack = [-1]
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                # Push the index of the open parenthesis
                stack.append(i)
            else:
                # Pop the matching open parenthesis index (or the previous invalid base)
                stack.pop()
                
                if not stack:
                    # If stack is empty, this ')' is invalid. Push its index to be the new base.
                    stack.append(i)
                else:
                    # Calculate the length of the valid substring
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len