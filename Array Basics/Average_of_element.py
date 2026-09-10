#Given an array of integers, compute the average (mean) of its elements.

num=[1, 1, 2, 2, 3, 4, 4, 5]
sum=0
for i in num:
    sum+=i
print(f"Avarage of element in an array is {sum/len(num)}")