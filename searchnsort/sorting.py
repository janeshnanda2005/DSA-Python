def bubble_sort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1],arr[j]

  return arr

ad = bubble_sort([10,7,5,4,3])
print(ad)

def selection_sort(arr):
  for i in range(len(arr)):
    min = i
    for j in range(i+1,len(arr)):
      if arr[j] < arr[min]:
        min = j
    arr[i],arr[min] = arr[min],arr[i]
  return arr

ad = selection_sort([10,7,5,4,3])
print(ad)

def quick_sort(arr):
  if len(arr) <=1:
    return arr
  pivot = arr[len(arr)//2]
  left,right,middle = [],[],[]
  for i in arr:
    if i < pivot:
      left.append(i)
    elif i == pivot:
      middle.append(i)
    else:
      right.append(i)
  return quick_sort(left) + middle + quick_sort(right)

a = [1,3,4,7,2,6]
print(quick_sort(a))

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
print(insertion_sort([23,1,5,2,3,6]))

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[mid:])
    right = merge_sort(arr[:mid])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge_sort([7,5,1,8,6,2,4,44]))