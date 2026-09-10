#Find the maximum and minimum elements in an array.
import sys
n=[5, 2, 9, 1, 7, 3]
min=sys.maxsize
max=1-sys.maxsize

for i in n:
    if i<min:
        min=i
    if i>max:
        max=i
print("Max=",max)
print("Min=",min)