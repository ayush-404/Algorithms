from typing import AnyStr


class Solution(object):
    def fourSum(self, nums:list, target:int):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[List[int]]
      """
      end = len(nums) - 1
      fixed1 = 0
      fixed2 = 1
      ans = []
      for _ in range(0, len(nums) - 3):
        for i in range(fixed2 + 1, len(nums)):
          for j in range(i + 1, len(nums)):
            if nums[fixed1] + nums[fixed2] + nums[i] + nums[j] == target:
              ans.append([nums[fixed1] , nums[fixed2] , nums[i] , nums[j]])
        fixed1 += 1
        fixed2 += 1
      return ans
ans = Solution()
print(ans.fourSum([1,0,-1,0,-2,2], 0))
