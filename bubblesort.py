def bubble_sort(arr):
    for n in range(len(arr)-1,0,-1):
        for i in range(n):
            if arr[i]>arr[i+1]:
                swapped=True
                arr[i],arr[i+1]=arr[i+1],arr[i]

arr=[22,9,11,5,18,6,12,1,14,2]
print("Unsorted list:")
print(arr)

bubble_sort(arr)
print("Sorted list")
print(arr)
