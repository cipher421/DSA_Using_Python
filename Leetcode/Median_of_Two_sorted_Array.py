"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
"""
def merge(nums1,nums2):
    a=len(nums1)
    b=len(nums2)
    i=j=k=0
    merged=[0]*(a+b)

    while i<a and j<b:
        if nums1[i]<nums2[j]:
            merged[k]=nums1[i]
            i+=1
        else:
            merged[k]=nums2[j]
            j+=1
        k+=1

    while i<a:
        merged[k]=nums1[i]
        i+=1
        k+=1

    while j<b:
        merged[k]=nums2[j]
        j+=1
        k+=1

    n = a + b
    mid = n // 2
    if n % 2 == 0:      
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


nums1 =[1,2,3,4,5]
nums2 =[6,7,8,9,10,11,12,13,14,15,16,17]
print(merge(nums1,nums2))