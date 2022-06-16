import sys
import time

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

# -------------------------------------------
# Method for force the best case of quick sort
# -------------------------------------------
def quick_sort(array, start, end):
  if start < end:
    (array[(start+end)//2], array[start]) = (array[start], array[(start+end)//2])
    part = partition(array, start, end)
    quick_sort(array, start, part)
    quick_sort(array, part + 1, end)

sys.setrecursionlimit(10000)

# ------------------------------------------
# Calculation of the best case execution time
# ------------------------------------------
for n in range(100, 10000, 100):
  t = 0
  ini = time.time()
  data = list(range(n)) # create random array
  quick_sort(data, 0, len(data) - 1)
  t += (time.time() - ini)
  print(n, t)
