class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(find_left):
            left, right = 0, len(nums) - 1
            index = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    index = mid  # Found the target, but keep searching
                    if find_left:
                        right = mid - 1  # Look to the left for the starting position
                    else:
                        left = mid + 1   # Look to the right for the ending position
                        
            return index

        # Find the first and last positions using the helper function
        start = binarySearch(find_left=True)
        end = binarySearch(find_left=False)
        
        return [start, end]   