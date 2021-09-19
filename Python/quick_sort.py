import random
import math

# Divide and Conquer: Similar to megre sort but with a random pivot instead of the middle element.
def quick_sort(arr):
  if len(arr) > 1:
    partition = math.floor(random.random() * len(arr))
    left = arr[: partition]
    right = arr[partition:]
    quick_sort(left)
    quick_sort(right)

    (i,j,k) = (0 for i in range(3))
    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        arr[k] = left[i]
        i += 1
        k += 1
      else: 
        arr[k] = right[j]
        j += 1 
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1 
        k += 1

arr = [math.floor(random.random()* 100) for _ in range(10)]
print(arr)
quick_sort(arr)
print(arr)


