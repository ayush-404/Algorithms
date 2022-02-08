import math
class Solution(object):
  def addDigits(self, num):
    if num%9 ==0 and num!=0:
      return 9
    else:
      return num%9

sol = Solution()
print(sol.addDigits(10000))