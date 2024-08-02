def sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    res = []
    i,j =0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print(sort([23,542,4,432,443]))

def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
print(insertion([23,1,5,2,3,6]))


def quick(arr):
    if len(arr)<=1:
        return arr
    left ,right,middle = [],[],[]
    pivot = arr[len(arr)//2]
    for i in arr:
        if pivot == i:
            middle.append(i)
        elif pivot > i:
            left.append(i)
        else:
            right.append(i)

    return quick(left)+middle+quick(right)
print(quick([23,1,5,2,3,6]))

def selection(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i] ,arr[min] = arr[min], arr[i]
    return arr
print(selection([23,1,5,2,3,6]))

def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j+1] > arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    return arr
print(bubble([23,1,5,2,3,6]))

def insertion(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr
print(insertion([23,1,5,2,3,6]))


def binary_search(arr,tar):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = len(arr)//2

        if arr[mid] == tar:
            print(f'The value is found in {arr.index(arr[mid])} position')
            break
        elif arr[mid] < tar:
            left = mid+1
        else:
            right = mid-1

binary_search([1,23,45,67,89,100],67)
        
        
