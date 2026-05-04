class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        # If no pivot is found, the array is in descending order.
        # We skip to Step 3 to reverse the whole thing.
        if pivot != -1:
            # Step 2: Find the number to swap with the pivot
            for j in range(n - 1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
        
        # Step 3: Reverse the suffix starting from pivot + 1
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1