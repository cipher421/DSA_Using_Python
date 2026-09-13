def merge(nums1,nums2):
    a=len(nums1)
    b=len(nums2)
    i=j=0
    merged=[]
    
    while i<a and j<b:
        if nums1[i]<nums2[j]:
            merged.append(nums1[i])
            i+=1
        else:
            merged.append(nums2[j])
            j+=1

    while i<a:
        merged.append(nums1[i])
        i+=1

    while j<b:
        merged.append(nums2[j])
        j+=1
    return merged

nums1 =[1,2,3,4,5]
nums2 =[6,7,8,9,10,11,12,13,14,15,16,17]
print(merge(nums1,nums2))