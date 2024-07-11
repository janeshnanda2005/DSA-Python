def binary(arr,target):
     left = 0
     right = len(arr)-1
     while left <= right:
          mid = (left+right)//2
          if arr[mid] == target:
               print(f"found at {mid}")
               break
          elif arr[mid] < target:
               left = mid+1
          else:
               right = mid+1

binary([23,4,9,6,5,34,3],6)

def linear(arr,target):
     for i in range(len(arr)):
          if arr[i]==target:
                print(f'{(arr[i])}')
linear([23,4,9,6,5,34,3],6)

