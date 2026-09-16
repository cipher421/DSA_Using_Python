def selection_sort(arr):
    n=len(arr)
    for i in range(0,n-1):
        indexmin=i
        for j in range(i+1,n):
            if(arr[j]<arr[indexmin]):
                indexmin=j
        arr[i],arr[indexmin]=arr[indexmin],arr[i]


arr=[65,25,32,20,40,15]
selection_sort(arr)
print(arr)