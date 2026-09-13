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
    return merged

nums1 =[1,2,3,4,5]
nums2 =[6,7,8,9,10,11,12,13,14,15,16,17]
print(merge(nums1,nums2))