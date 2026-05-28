class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case
        current_string = "1"
        
        # Build the sequence iteratively from 2 to n
        for _ in range(1, n):
            next_string = []
            i = 0
            
            # Process the current string to find run-length encodings
            while i < len(current_string):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(current_string) and current_string[i] == current_string[i + 1]:
                    count += 1
                    i += 1
                
                # Append count and the character itself
                next_string.append(str(count))
                next_string.append(current_string[i])
                i += 1
            
            # Update current_string for the next iteration
            current_string = "".join(next_string)
            
        return current_string