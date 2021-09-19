import random
import math

import sys
def selection_sort(arr):
  for i in range(0, len(arr)):
    smallest = i
    for j in range(i, len(arr)):
      if arr[j] < arr[smallest]:
        smallest = j

    temp = arr[i]
    arr[i] = arr[smallest]
    arr[smallest] = temp



arr = [math.floor(random.random()* 100) for _ in range(10)]
print(arr)
selection_sort(arr)
print(arr)
