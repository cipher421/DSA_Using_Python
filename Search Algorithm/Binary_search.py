def search(nums,target):
    left=0
    right=len(nums)-1

    mid = left + (right - left) // 2

    while left<=right:
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1

    return -1

nums = [1,3,5,6,7]
target = 5
result=search(nums,target)
if not result:
    print(f"The element is not found at {result}")
else:
    print(f"The element found at {result}")