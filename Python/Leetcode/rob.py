#https://leetcode.com/problems/house-robber/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Breaking into the first and second houses, base Case
        if len(nums) == 1:
          return nums[0]
        elif len(nums) == 2:
          return max(nums[0], nums[1])
        dp = [nums[0] , nums[1]]
        for i in range(2, len(nums)):
          ans = -1
          for j in range(i-2, -1, -1):
            ans = max(dp[j] + nums[i], ans)
          dp.append(max(dp[i-1], ans))
        return dp[len(nums) -1]
