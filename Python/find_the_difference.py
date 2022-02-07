from gettext import find
import typing
from collections import defaultdict
class Solution(object):
  def find_diff(self, s, t):
    ds = {}
    dt = {}
    for c in s:
      if ds.get(c) == None:
        ds[c] = 1
      else:
        ds[c] += 1
    for c in t:
      if dt.get(c) == None:
        dt[c] = 1
      else:
        dt[c] += 1
    for key in dt.keys():
      if ds.get(key) == None:
        return key
      if ds.get(key) != dt.get(key):
        return key

s = "abcd"
t = "abcde"

sol = Solution()
print(sol.find_diff(s, t))