list=[1,2,3,5,2,2,1,3]
for i in list:
  count=0
for j in list:
  if i==j:
    count+=1

print(i,"=",count)
