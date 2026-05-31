class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # 1. Sort the candidates to handle duplicates easily
        candidates.sort()
        
        def backtrack(start: int, target: int, path: List[int]):
            # Base Case 1: Target reached
            if target == 0:
                res.append(list(path))
                return
            # Base Case 2: Exceeded target
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same decision level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Optimization: If the current number is greater than the remaining target,
                # since the array is sorted, all subsequent numbers will also be too large.
                if candidates[i] > target:
                    break
                
                # Include the candidate and move to the next index (i + 1)
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                # Backtrack
                path.pop()
                
        backtrack(0, target, [])
        return res