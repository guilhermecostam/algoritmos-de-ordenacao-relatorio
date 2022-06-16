import os
import time
import random

# -----------------------------------------------
# Methot that print the option screen of the system
# -----------------------------------------------
def options_screen():
  print("\n");
  print("/////////////////////////////////////////////////////////////////////");
  print("///                                                               ///");
  print("///                   = = Insertion Sort = =                      ///");
  print("///                                                               ///");
  print("///             Press (1) to receive the best case                ///");
  print("///             Press (2) to receive the average case             ///");
  print("///             Press (3) to receive the worst case               ///");
  print("///             Press (0) to exit the system                      ///");
  print("///                                                               ///");
  print("/////////////////////////////////////////////////////////////////////");
  print("\n");

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
# Calculation of the best case execution time
# ------------------------------------------
def best_case():
  for n in range(100, 10000, 100):
    t = 0
    ini = time.time()
    data = list(range(n)) # create random array
    insertion_sort(data)
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
    insertion_sort(data)
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
    data.sort(reverse=True) # sorts the array in descending order
    insertion_sort(data)
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
