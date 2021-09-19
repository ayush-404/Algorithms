import random
import math


def merge_sort(array):
  if len(array) > 1:
    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]
    merge_sort(left)
    merge_sort(right)
    (i , j, k) = (0, 0, 0)
    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        array[k] = left[i]
        i+= 1
      else:
        array[k] = right[j]
        j+= 1
      k+=1

    while i < len(left):
      array[k] = left[i]
      i+= 1
      k+=1
    
    while j < len(right):
      array[k] = right[j]
      j+= 1
      k += 1


arr = [math.floor(random.random()* 100) for _ in range(10)]
print(arr)
merge_sort(arr)
print(arr)


