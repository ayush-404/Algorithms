import random
import math

def bubble_sort(arr):
  swap = True
  while swap:
    swap = False
    for i in range(0, len(arr) - 1):
      if arr[i] > arr[i +1]:
        temp = arr[i]
        arr[i] = arr[i+1]
        arr[i+1] = temp
        swap = True
  
arr = [math.floor(random.random()* 100) for _ in range(10)]
print(arr)
bubble_sort(arr)
print(arr)
