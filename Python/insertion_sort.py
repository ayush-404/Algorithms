import random
import math

def insertion_sort(arr):
  for j in range(1, len(arr)):
    for k in range(j, 0, -1):
      if(arr[k-1] >= arr[k]):
        temp = arr[k]
        arr[k] = arr[k-1]
        arr[k-1] = temp
      else:
        break


arr = [math.floor(random.random()* 100) for _ in range(10)]
print(arr)
insertion_sort(arr)
print(arr)
