#https://leetcode.com/problems/move-zeroes/submissions/
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        last_idx = len(nums) - 1
        z_count = 0
        i = 0
        for j in range(len(nums)):
          if nums[j] == 0:
            z_count += 1
          else:
            nums[i] = nums[j]
            i += 1
        for t in range(len(nums) - z_count, len(nums)):
          nums[t] = 0
