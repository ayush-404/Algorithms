class Solution(object):
  done = set()

  def bin_search(self, arr, x):
      low = 0
      high = len(arr) - 1
      mid = 0

      while low <= high:
          mid = (high + low) // 2
          if arr[mid] < x:
              low = mid + 1
          elif arr[mid] > x:
              high = mid - 1
          else:
            return True
      return False

  def findPairsWithZero(self, nums):
    ans = 0
    hist = set()
    for val in nums:
      if val in self.done and val not in hist:
        ans += 1
        hist.add(val)
      else:
        self.done.add(val)
    return ans

  def findPairs(self, nums, k):
    if k == 0:
      return self.findPairsWithZero(nums)
    ans = 0
    nums.sort()
    if(len(nums) == 1):
      return 0
    for val in nums:
      if self.bin_search(nums, val - k) == True and (val not in self.done or val - k not in self.done):
        ans += 1
        self.done.add(val)
        self.done.add(val -k)
    return ans


nums = [1,2,3,4,5]
k = 1
print(nums)
print(k)
sol = Solution()
print(sol.findPairs(nums, k))