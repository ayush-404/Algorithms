import typing
def rem_dup(nums: typing.List):
  idx1 = 0; idx2 = 1
  curr_dup = 1
  while idx2 < len(nums):
    if nums[idx1] != nums[idx2]:
      curr_dup = 1
      idx1 += 1
      nums[idx1] = nums[idx2]
    else:
      if(curr_dup < 2):
        idx1 += 1
        nums[idx1] = nums[idx2]
        curr_dup += 1
    idx2 += 1
  return idx1 + 1



nums = [0,1,2,3,3,3,3,3]
print("\n")
for i in range(rem_dup(nums)):
  print(nums[i])