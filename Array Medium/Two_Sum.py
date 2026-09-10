#Given an array and a target sum, find two numbers in the array that add up to the target. Return their indices (or the pair itself)

nums=[2,7,8,6]
target=9

for i in range(0,len(nums)):
    if nums[i]+nums[i-1]==target:
        print([i,i-1])