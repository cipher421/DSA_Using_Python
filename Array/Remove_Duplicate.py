#Q4. Remove duplicate elements from a sorted array and return the new length.
# Input: [1, 1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5], Length = 5
#nums=[1, 1, 2, 2, 3, 4, 4, 5]
nums=[1,1,2]
#brute Force
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)-1):
        if nums[i]==nums[j]:
            nums.pop(i)
print(len(nums))
print(nums)

#Two Pointer
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Pointer for the position of unique elements
        j = 1
        
        # Iterate through the array starting from second element
        for i in range(1, len(nums)):
            # If current element is different from previous unique element
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        
        return j  # Return the length, not the array