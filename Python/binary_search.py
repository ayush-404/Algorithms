def binary_search(arr, key):
  p = 0 
  q = len(arr) - 1
  mid = 0
  while q >= p:
    mid = (p+q) // 2
    if key < arr[mid]:
      q = mid
    else:
      p = mid
  return p if arr[mid] == key else -1

arr = [2,4,6,8,10]
print(binary_search(arr, 5))