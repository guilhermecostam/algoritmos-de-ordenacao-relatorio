import time

# -----------------------------------------------------------
# Method that sorting array of integers using ordered insertion
# -----------------------------------------------------------
def insertion_sort(array):
  for i in range(len(array)):
    key_item = array[i]
    j = i - 1
    while j >= 0 and array[j] > key_item:
      array[j+1] = array[j]
      j -= 1
    array[j+1] = key_item

# ------------------------------------------
# Calculation of the worst case execution time
# ------------------------------------------
for n in range(100, 10000, 100):
  t = 0
  ini = time.time()
  data = list(range(n)) # create random array
  data.sort(reverse=True) # sorts the array in descending order
  insertion_sort(data)
  t += (time.time() - ini)
  print(n, t)
