def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]

a=[80,10,90,60,500,500000,7000]
bubble_sort(a)
print(a)