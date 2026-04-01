class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:  # 👈 add self
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return closest