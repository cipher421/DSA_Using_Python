#Given an array nums, return an array output where output[i] is the product of all elements of nums except nums[i].

def productExceptSelf(nums):
    n = len(nums)
    left = [1] * n
    right = [1] * n
    output = [1] * n
    
    for i in range(1, n):
        left[i] = left[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * nums[i+1]
    
    for i in range(n):
        output[i] = left[i] * right[i]
    
    return output

print(productExceptSelf([1, 2, 3, 4]))