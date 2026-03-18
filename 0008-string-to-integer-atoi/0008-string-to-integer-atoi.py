class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        
        # Step 1: skip spaces
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            
            # Step 4: check overflow BEFORE adding
            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -2**31
            
            num = num * 10 + digit
            i += 1
        
        return sign * num