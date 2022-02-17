from collections import defaultdict
class Solution(object):
  def checkInclusion(self, s1:str, s2:str):
    s1_dict = defaultdict(lambda: 0)
    for char in s1:
      s1_dict[char] += 1
    for i in range(len(s2)):
      s2_dict = defaultdict(lambda: 0)
      for j in range(len(s2)):
        for char in s2[i:j]:
          s2_dict[char] += 1
        for key,val in s1_dict:
          # Not Completed
          pass
    return False
    
s1 = "ab"
s2 = "eidbaooo"

sol = Solution()
print("true" if sol.checkInclusion(s1, s2) else "false")