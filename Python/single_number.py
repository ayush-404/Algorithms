class Solution(object):
  def singleNumber(self, nums):
    ans = 0
    for val in nums:
      ans = ans ^ val
    return ans

sol = Solution()

nums = [4,1,2,1,2]
print(sol.singleNumber(nums))