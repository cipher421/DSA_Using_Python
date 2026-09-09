#Q3. Find the second largest element in an array (considering no duplicates).
# Input: [10, 5, 8, 20, 2, 15]
# Output: 15

import sys
n = [10, 5, 8, 20, 2, 15]
Max=1-sys.maxsize
Second_largest=1-sys.maxsize
for i in n:
    if i>Max:
        Max=i

for i in n:
    if i>Second_largest and i<Max:
        Second_largest=i
print(f"Second Largest Element is {Second_largest}")