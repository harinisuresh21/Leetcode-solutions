class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Initialize lists of sets for rows, columns, and 3x3 boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == '.':
                    continue
                
                # Determine the index of the 3x3 box
                # Mapping formula: (r // 3) * 3 + (c // 3)
                box_idx = (r // 3) * 3 + (c // 3)
                
                # Check if the number already exists in the current row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                    return False
                
                # Add the number to the respective sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_idx].add(val)
                
        return True