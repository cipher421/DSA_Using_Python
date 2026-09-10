#Given an array and a target value, find whether the target exists in the array. Return its index if found, otherwise return -1.

def linear_search(arr,element):
    for i in range(0,len(arr)):
        if arr[i]==element:
            return i
    return -1

num=[1, 1, 2, 2, 3, 4, 4, 5]
element=int(input("Enter Number to be search for:-"))
result=linear_search(num,element)
if not result:
    print("The element is not found")
else:
    print(f"The element is found at {result}")