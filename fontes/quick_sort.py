import os
import sys
import time
import random

# -----------------------------------------------
# Methot that print the option screen of the system
# -----------------------------------------------
def options_screen():
  print("\n");
  print("/////////////////////////////////////////////////////////////////////");
  print("///                                                               ///");
  print("///                     = = Quick Sort = =                        ///");
  print("///                                                               ///");
  print("///             Press (1) to receive the best case                ///");
  print("///             Press (2) to receive the average case             ///");
  print("///             Press (3) to receive the worst case               ///");
  print("///             Press (0) to exit the system                      ///");
  print("///                                                               ///");
  print("/////////////////////////////////////////////////////////////////////");
  print("\n");

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

# -------------------------------------------
# Method for force the best case of quick sort
# -------------------------------------------
def quick_sort_best(array, start, end):
  if start < end:
    (array[(start+end)//2], array[start]) = (array[start], array[(start+end)//2])
    part = partition(array, start, end)
    quick_sort_best(array, start, part)
    quick_sort_best(array, part + 1, end)

sys.setrecursionlimit(10000)

# ------------------------------------------
# Calculation of the best case execution time
# ------------------------------------------
def best_case():
  for n in range(100, 10000, 100):
    t = 0
    ini = time.time()
    data = list(range(n)) # create random array
    quick_sort_best(data, 0, len(data) - 1)
    t += (time.time() - ini)
    print(n, t)

# --------------------------------------------
# Calculation of the average case execution time
# --------------------------------------------
def average_case():
  for n in range(100, 10000, 100):
    t = 0
    ini = time.time()
    data = list(range(n)) # create random array
    random.shuffle(data) # shuffles the array
    quick_sort(data, 0, len(data) - 1)
    t += (time.time() - ini)
    print(n, t)

# ------------------------------------------
# Calculation of the worst case execution time
# ------------------------------------------
def worst_case():
  for n in range(100, 10000, 100):
    t = 0
    ini = time.time()
    data = list(range(n)) # create random array
    quick_sort(data, 0, len(data) - 1)
    t += (time.time() - ini)
    print(n, t)

# --------------
# Execution start
# --------------
key = 0
while key >= 0:
  while True:
    options_screen()
    key = input('\nType the option you want: ')
    os.system('cls||clear')

    if key.isdigit():
      key = int(key)
      break
    else:
      print('\nType only numbers!')

  if key == 1:
    best_case()
  elif key == 2:
    average_case()
  elif key == 3:
    worst_case()
  elif key == 0:
    key = -1
    print('\nGoodbye.')
  else:
    print('\nInvalid option.')
  input("\nPress Enter to continue...")
