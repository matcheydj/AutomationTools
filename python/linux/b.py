import os,sys

def func(num):
  if num == 2:
    raise ValueError("num is 2")

try:
   func(2)
except ValueError as e:
   print("The 显示值 2")
