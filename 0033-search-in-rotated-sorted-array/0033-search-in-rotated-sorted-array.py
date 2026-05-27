class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Condition 1: Found the target
            if nums[mid] == target:
                return mid
            
            # Condition 2: Check if the left half is sorted
            if nums[left] <= nums[mid]:
                # Check if target lies within the sorted left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Search left
                else:
                    left = mid + 1   # Search right
            
            # Condition 3: Otherwise, the right half must be sorted
            else:
                # Check if target lies within the sorted right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Search right
                else:
                    right = mid - 1  # Search left
                    
        return -1