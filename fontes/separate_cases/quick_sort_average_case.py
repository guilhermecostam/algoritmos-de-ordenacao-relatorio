import sys
import time
import random

# -----------------------------------------------
# Method that partitions an array based on its edges
# -----------------------------------------------
def partition(array, start, end):
  pivot = array[start]
  while 1:
    while array[start] < pivot:
      start = start + 1

    while array[end] > pivot:
      end = end - 1

    if start >= end:
      return end

    (array[start], array[end]) = (array[end], array[start])

    start = start + 1
    end = end - 1

# -----------------------------------------------------------
# Method that sorting array of integers using division and conquest
# -----------------------------------------------------------
def quick_sort(array, start, end):
  if start < end:
    part = partition(array, start, end)
    quick_sort(array, start, part)
    quick_sort(array, part + 1, end)

sys.setrecursionlimit(10000)

# --------------------------------------------
# Calculation of the average case execution time
# --------------------------------------------
for n in range(100, 10000, 100):
  t = 0
  ini = time.time()
  data = list(range(n)) # create random array
  random.shuffle(data) # shuffles the array
  quick_sort(data, 0, len(data) - 1)
  t += (time.time() - ini)
  print(n, t)
