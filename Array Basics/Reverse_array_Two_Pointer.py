#Reverse the elements of an array in-place.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

n=[1, 2, 3, 4, 5]
j=len(n)-1
for i in range(len(n)//2):
    if n[j]>n[i]:
        n[i], n[j] = n[j], n[i]
        j=j-1

print(n)