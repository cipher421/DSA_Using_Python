#Given an array of integers, calculate and return the sum of all its elements.

num=[1, 1, 2, 2, 3, 4, 4, 5]
sum=0
# Keep a running total as each array value is visited.
for i in num:
    sum+=i
print(f"The sum of Array is {sum}")