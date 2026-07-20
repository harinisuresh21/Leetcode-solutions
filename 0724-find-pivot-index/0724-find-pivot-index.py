class Solution(object):
    def pivotIndex(self, nums):
        total_sum= sum(nums)
        left_nums=0

        for i in range(len(nums)):
            right_sum=total_sum-left_nums-nums[i]

            if left_nums == right_sum:
                return i

            left_nums+=nums[i]

        return -1