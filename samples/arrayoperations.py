#array possiblities
l =[1,2,5,6,22,4,4,5]
p = l[0]
for i in l:
     if i > p:
          p = i
     else:
          continue
print(p) 

k = [1,903939,49404,565,54,56,43]
l = k[0]
for i in k:
     if len(str(i)) > len(str(l)):
          l = i
     else:
          continue
print(f'{l} and {len(str((l)))}')


k =[23,56,32,21,34,55,66,3,1]
for i in k:
     print(f'{chr(i)}',end = " ")     

l = [9303,44,8585,884,994]
for i in range(len(l)):
     print(f'{chr(l[i])}\n',end = " ")


