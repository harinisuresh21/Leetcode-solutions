class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        result = []

        def backtrack(index: int, current: list[str]):
            if index == len(digits):
                result.append("".join(current))
                return

            for letter in phone_map[digits[index]]:
                current.append(letter)
                backtrack(index + 1, current)
                current.pop()

        backtrack(0, [])
        return result

# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         if not digits:
#             return []

#         phone_map = {
#             "2": "abc", "3": "def",
#             "4": "ghi", "5": "jkl", "6": "mno",
#             "7": "pqrs", "8": "tuv", "9": "wxyz"
#         }

#         result = []

#         def backtrack(index: int, current: list[str]):
#             # Base case: combination is complete
#             if index == len(digits):
#                 result.append("".join(current))
#                 return

#             for letter in phone_map[digits[index]]:
#                 current.append(letter)       # Choose
#                 backtrack(index + 1, current)  # Explore
#                 current.pop()                # Un-choose

#         backtrack(0, [])
#         return result
# ```

# **Recursion Tree for `"23"`:**
# ```
# backtrack(0, [])
# ├── 'a' → backtrack(1, [a])
# │         ├── 'd' → backtrack(2, [a,d]) ✓ "ad"
# │         ├── 'e' → backtrack(2, [a,e]) ✓ "ae"
# │         └── 'f' → backtrack(2, [a,f]) ✓ "af"
# ├── 'b' → backtrack(1, [b])
# │         ├── 'd' → "bd"
# │         ├── 'e' → "be"
# │         └── 'f' → "bf"
# └── 'c' → backtrack(1, [c])
#           ├── 'd' → "cd"
#           ├── 'e' → "ce"
#           └── 'f' → "cf"
# ```

# **The 3-step backtracking pattern:**
# ```
# for letter in choices:
#     current.append(letter)        # 1. CHOOSE
#     backtrack(index + 1, current) # 2. EXPLORE
#     current.pop()                 # 3. UN-CHOOSE  ← restores state