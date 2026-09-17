def partition(arr, p, q):
    x = arr[p]          
    i = p               
    for j in range(p + 1, q + 1):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]   
    return i                          

def quick_sort(arr, p, q):
    if p < q:                         
        partitionindex = partition(arr, p, q)
        quick_sort(arr, p, partitionindex - 1)
        quick_sort(arr, partitionindex + 1, q)

arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print(arr) 