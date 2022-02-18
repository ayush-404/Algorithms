# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sq_sorted = []
        pos_start = len(nums)
        for i in range(len(nums)):
          if nums[i] >= 0:
            pos_start = i
            break
        neg_end = pos_start - 1
        while neg_end >= 0 or pos_start < len(nums):
          if neg_end >= 0 and pos_start < len(nums) and \
            abs(nums[neg_end]) <= nums[pos_start]:
            sq_sorted.append(nums[neg_end] ** 2)
            neg_end -= 1
          if neg_end >= 0 and pos_start < len(nums) and \
            abs(nums[neg_end]) > nums[pos_start]:
            sq_sorted.append(nums[pos_start]**2)
            pos_start += 1
          if neg_end >= 0 and pos_start == len(nums):
            sq_sorted.append(nums[neg_end]**2)
            neg_end -= 1
          if pos_start < len(nums) and neg_end < 0:
            sq_sorted.append(nums[pos_start]**2)
            pos_start += 1
        return sq_sorted
print(Solution().sortedSquares([-4,-1, 2,3,10]))