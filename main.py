#NUMPY TASKS ---

# IMPORT NUMPY ---
import numpy as np

# Task 1: Print a 1D array of numbers from 0 to 9 ---
print("Task 01")
array = np.arange(0,10)
print(array)

print("\n")
# ---------------------------------------------------------------------------
# Task 2: Print a 3×3 NumPy array of all Trues ---
print("Task 02")
trueArray = np.ones((3,3),  dtype=bool)
print(trueArray)

print("\n")
# ---------------------------------------------------------------------------
# Task 3: Extract all odd numbers from array of 1-10 ---
print("Task 03")
oddArray = np.arange(1,10,2)
print(oddArray)

print("\n")
# ---------------------------------------------------------------------------
# Task 4: Subtract 1 from each of the numbers in the above array ---
print("Task 04")
print(oddArray-1)

print("\n")
# ---------------------------------------------------------------------------
# Task 5: Convert a 1D array to a 2D array with 2 rows ---
print("Task 05")
xArray = np.arange(1,7)
print(xArray)
xArray = np.reshape(xArray, (2,3))
print(xArray)

print("\n")
# ---------------------------------------------------------------------------
# Task 6: Create two arrays (a and b) - stack these two arrays vertically use the np.dot and np.sum to calculate totals --
print("Task 06")

# ARRAY A and B --- STACK VERTICALLY ---
arrayA = np.arange(1,5).reshape(4,1)
arrayB = np.arange(10,14).reshape(4,1)
print(arrayA)
print(arrayB)

# RESHAPE FOR .DOT ---
arrayB = np.reshape(arrayB, (1,4))
c = np.dot(arrayA,arrayB)
print(c)

# SUM ---
d = np.sum(c)
print(d)

print("\n")
# ---------------------------------------------------------------------------
# Task 7: Create the following pattern without hardcoding: array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3,1,2,3]) ---
print("Task 07")
mainArray = np.array([1,2,3])
mainArray = np.r_[np.repeat(mainArray, 3), np.tile(mainArray, 3)]
print(mainArray)

print("\n")
# ---------------------------------------------------------------------------
# Task 8: In two arrays a ( 1,2,3,4,5) and b ( 4,5,6,7,8,9) – remove all repeating items present in array b ---
print("Task 08")
arrayA = np.array([1,2,3,4,5])
arrayB = np.array([4,5,6,7,8,9])
print(f"A {arrayA}")
print(f"B {arrayB}")
listA = list(arrayA)
listB = list(arrayB)
for a in listB:
  for b in listA:
    if a == b:
      listB.remove(a)
      listA.remove(b)
print(listA)
print(listB)
# 5 is duplicate but still prints - unsure why??

print("\n")
# ---------------------------------------------------------------------------
# Task 9: Get all integers between 5 and 10 from arrays a and b and sum them together ---
print("Task 09")
print(f"A {arrayA}")
print(f"B {arrayB}")
arrayC = np.r_[arrayA, arrayB]
print(f"C {arrayC}")
listC = list(arrayC)

# INTEGERS BETWEEN 5 AND 10
for i in listC:
  if i < 5 or i > 10:
    listC.remove(i)
print(listC)

# SUM OF LIST C
sum = np.sum(listC)
print(sum)
