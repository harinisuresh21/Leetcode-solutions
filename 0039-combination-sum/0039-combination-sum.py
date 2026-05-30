class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(index, current_combination, current_sum):
            # Base Case 1: If we found a combination that matches the target
            if current_sum == target:
                result.append(list(current_combination))
                return
            
            # Base Case 2: If the sum exceeds the target or we run out of candidates
            if current_sum > target or index >= len(candidates):
                return
            
            # Choice 1: Include candidates[index]
            # We keep the index the same because we can reuse the same number
            current_combination.append(candidates[index])
            backtrack(index, current_combination, current_sum + candidates[index])
            
            # Backtrack: Remove the number we just added before trying the next choice
            current_combination.pop()
            
            # Choice 2: Exclude candidates[index] and move to the next number
            backtrack(index + 1, current_combination, current_sum)
            
        # Start the recursion from index 0, with an empty combination and 0 sum
        backtrack(0, [], 0)
        return result