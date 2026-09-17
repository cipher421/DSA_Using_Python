def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        # Insert the current value into the already sorted left portion.
        key=arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key



arr=[65,25,32,20,40,15]
insertion_sort(arr)
print(arr)