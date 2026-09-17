"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""

def search(nums,target):
    left=0
    right=len(nums)-1

    while left<=right:
        # Binary search removes half of the possible positions each iteration.
        mid = left + (right - left) // 2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1 
        elif nums[mid]>target:
            right=mid-1

    # left is the first position where target can be inserted.
    return left

nums = [1,3,5,6,7]
target = 8
result=search(nums,target)
if result:
    print(f"The element is not found at {result}")
else:
    print(f"The element found at {result}")