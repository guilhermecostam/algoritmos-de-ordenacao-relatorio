import time

# -----------------------------------------------------------
# Method that combines two ordered arrays into one ordered array
# -----------------------------------------------------------
def merge(array, left_array, right_array):
  left_index, right_index, array_index = 0, 0, 0

  while left_index < len(left_array) and right_index < len(right_array):
    if left_array[left_index] < right_array[right_index]:
      array[array_index] = left_array[left_index]
      left_index += 1
    else:
      array[array_index] = right_array[right_index]
      right_index += 1
    array_index += 1

  while left_index < len(left_array):
    array[array_index] = left_array[left_index]
    left_index += 1
    array_index += 1

  while right_index < len(right_array):
    array[array_index] = right_array[right_index]
    right_index += 1
    array_index += 1

# -----------------------------------------------------------
# Method that sorting array of integers using division and conquest
# -----------------------------------------------------------
def merge_sort(array):
  if len(array) > 1:
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]

    merge_sort(left_array)
    merge_sort(right_array)
    merge(array, left_array, right_array)

# ---------------------------------------------------
# Calculating method runtime with different input arrays
# ---------------------------------------------------
for n in range(100, 10000, 100):
  t = 0
  ini = time.time()
  data = list(range(n)) # create random array
  merge_sort(data)
  t += (time.time() - ini)
  print(n, t)
