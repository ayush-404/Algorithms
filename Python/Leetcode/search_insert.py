class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0
        while high >= low:
          print(f"high: {high}, low: {low}")
          mid = (high + low) // 2
          if target > nums[mid]:
            low = mid + 1
          elif target < nums[mid]:
            high = mid - 1
          else:
            return mid
        return low

print(Solution().searchInsert([1,3,5,6], 5))