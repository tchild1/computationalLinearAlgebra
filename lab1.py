# -*- coding: utf-8 -*-
"""Copy of Intro_to_Python_I.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eGaxuY6h8h_GDrQ-FqVQ7tIaoPVOW9IE

# **Lab 1 - Introduction to Python programming I**

Enter your code in the spaces provided.  Do not change any of the variable names or function names that are already provided for you.  In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab1"

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

my_first_var=(118+(11*2))/(9-2)  # Replace the value of 0 with the required expression from Problem 1.

"""**Problem 2**"""

def arithmetic2(i):
  return (((i+2)*3)-5) # Put your return value here.  Your shouldn't need to add any more lines of code to this function.

"""**Problem 3**"""

def triple(y):
  return y*3 # Put your return value here.

def avg(x,y):
  return (x+y)/2 # Put your return value here.

def combine(x,y):
  # Put your code here.  Remember that this function should call both of the functions triple(y) and avg(x,y) from above.
  return avg(triple(y), x) # Put your return value here.

"""**Problem 4**"""

def first(c):
  # Put your code here.
  return c[0] # Put your return value here.

def first_last(c):
  # Put your code here.
  return c[0], c[-1] # Put your return values here.  Remember a function can return two values (you will format your return statement as "return value1, value2").

def middle(c):
  c.pop(0)
  c.pop(-1)
  return c # Put your return value here.

"""**Problem 5**"""

def swap(c):
  new_list=c.copy() # This creates a copy of the list c, which is called new_list.  Your function should work with this list instead of the list c which is passed to the function.
  first = new_list[0]
  new_list[0] = new_list[-1]
  new_list[-1] = first
  return new_list

"""**Problem 6**"""

def absolute_value(x):
  return abs(x)

"""**Problem 7**"""

def indicator(lower,upper,n):
  if lower <= n and n <= upper:
    return 1
  else:
    return 0

"""**Problem 8**"""

def trunc_max(x,y):
  if x > y:
    big = x
  else:
    big = y

  if big > 0:
    return big
  else:
    return 0 # Put your return value here.

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""