class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Cyclic Sort: Put each number in its right place if possible
        for i in range(n):
            # Keep swapping until the current element is in the right slot,
            # out of bounds, or a duplicate.
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # 2. Find the first mismatch
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # 3. If all positions are correct, the missing number is n + 1
        return n + 1