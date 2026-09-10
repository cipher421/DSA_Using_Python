#Reverse the elements of an array using stack

n=[1, 2, 3, 4, 5]
stack=[]
reversed_stack=[]

for i in n:
    stack.append(i)

for j in n:
    reversed_stack.append(stack.pop())

print(f"The reversed array is {reversed_stack}")