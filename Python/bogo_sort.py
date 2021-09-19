import random
import math


def isSort(arr):
  for i in range(len(arr) - 1):
    if(arr[i] > arr[i+1]):
      return False
    return True
def bogo_sort(arr):
  copy = arr[:]
  while isSort(arr):
    for i in range(0, len(arr)):
      if random.random() < 0.5:
        index = math.floor(random.random()*len(arr))
        index2 = math.floor(random.random()*len(arr))
        temp = copy[index]
        copy[index] = copy[index2]
        copy[index2] = temp
  arr = copy


arr = [math.floor(random.random()* 100) for _ in range(4)]
print(arr)
bogo_sort(arr)
print(arr)
  
