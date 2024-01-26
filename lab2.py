# -*- coding: utf-8 -*-
"""Copy of Intro_to_Python_II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PNzAv4bwyy0sGj0Y4Z5_y5fP9VoH-1sh

# **Lab 2 - Introduction to Python programming II**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab2"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Tanner"

last_name="Child"

# Enter your Math 215 section number in between the quotation marks.

section_number="001"

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER!

BYUNetID="tchild01"

"""**Problem 1**"""

my_list=[1,2,3,4]

for i in my_list:
  i=2*i

first_elem=my_list[0]   # Replace the value of 0 with the number described in Problem 1.

"""**Problem 2**"""

def sum_list(L):
  total=0
  for i in L:
    total = total + i
  return total

"""**Problem 3**"""

def list_relu(L):
  new_list=L.copy()  # Remember to create a copy of your list.  After this lab you'll need to remember to do it on your own.

  index = 0
  for i in new_list:
    if new_list[index] < 0:
      new_list[index] = 0
    index += 1

  return new_list

print(list_relu([1,-2,17,-3.2,-15]))

"""**Problem 4**"""

import numpy as np  # Importing NumPy

my_var=((np.exp(5)-np.log(np.sqrt(5)))/(np.exp(np.cos(3))))   # Replace the value of 0 with the required value from Problem 4.

"""**Problem 5**"""

v = np.array([1, 3, -2, 4, 5])
u = np.array([1, 1, -2, 1, 1])
w = np.array([1, 0, 1, 0, 1])

vDotU = np.dot(v, u)
uDotU = np.dot(u, u)
vDotW = np.dot(v, w)
wDotW = np.dot(w, w)

scalarOne = vDotU/uDotU
scalarTwo = vDotW/wDotW

my_vect_var= (scalarOne * u) + (scalarTwo * w)

"""**Problem 6**"""

def first_rpt(M):
  new_matrix=M.copy()  # Remember to create a copy of your matrix.  After this lab you'll need to remember to do it on your own.
  firstRow = new_matrix[0]

  index = 0
  for row in new_matrix:
    new_matrix[index, :] = firstRow
    index += 1

  return new_matrix

"""**Problem 7**"""

def matrix_sum(M):
  total = 0
  for row in M:
    for col in row:
      total = total + col

  return total

"""**Problem 8**"""

long_list=[0.5**i for i in range(1, 101)]
print(long_list)

"""**Problem 9**"""



very_long_list=[b**e for e in range(1, 100) for b in range(1, 4)]
print(very_long_list)

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to [gradescope.com](https://gradescope.com) for grading.
"""