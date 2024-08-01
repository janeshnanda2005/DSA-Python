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

binary([10,20,30,40,50,60],60)

def linear(arr,target):
     for i in range(len(arr)):
          if arr[i]==target:
                print(f'{(arr[i])} found in {arr.index(arr[i])}')
linear([23,4,9,6,5,34,3],6)

