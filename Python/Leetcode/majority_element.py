class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maps = {}
        for val in nums:
          if val in maps.keys():
            maps[val] += 1
          else:
            maps[val] = 0
        high_key = maps.keys()[0]
        for key in maps.keys():
          if maps[key] > maps[high_key]:
            high_key = key
        return high_key