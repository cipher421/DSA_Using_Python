#Given an array of integers, count how many elements are even and how many are odd.
num=[1, 1, 2, 2, 3, 4, 4, 5]
even=0
odd=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1

print(f"The number of even element is {even}")
print(f"The number of odd element is {odd}")