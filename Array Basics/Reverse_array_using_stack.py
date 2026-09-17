#Reverse the elements of an array using stack

n=[1, 2, 3, 4, 5]
stack=[]
reversed_stack=[]

# Push values in their original order so the last value is on top.
for i in n:
    stack.append(i)

# Popping reverses the order because a stack is last-in, first-out.
for j in n:
    reversed_stack.append(stack.pop())

print(f"The reversed array is {reversed_stack}")