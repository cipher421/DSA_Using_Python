#Find the second largest element in an array (considering no duplicates).
# Input: [10, 5, 8, 20, 2, 15]
# Output: 15

import sys
n = [10, 5, 8, 20, 2, 15]
Max=1-sys.maxsize
Second_largest=1-sys.maxsize
# First find the largest value in the array.
for i in n:
    if i>Max:
        Max=i

# Find the greatest value that is still smaller than the maximum.
for i in n:
    if i>Second_largest and i<Max:
        Second_largest=i
print(f"Second Largest Element is {Second_largest}")