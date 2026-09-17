#Given an array and an integer K, rotate the array to the right by K positions.

def rotate(nums,k):
    n=len(nums)
    # Rotating by the array length returns the original array.
    k%=n
    def reverse(l,r):
        # Reversing three sections performs the rotation in place.
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
    reverse(0,n-1)
    reverse(0,k-1)
    reverse(k,n-1)

num=[1,2,3,4,5]
rotate(num,2)
print(num)