#Given an array of integers (may contain negative numbers), find the contiguous subarray with the largest sum and return that sum.
nums=[-2,1,-3,4,-1,2,1,-5,4]

current=best=nums[0]
# At each value, either extend the current subarray or start a new one.
for i in nums:
    current=max(i,current+i)
    # Store the largest subarray sum seen so far.
    best=max(best,current)
print(best)