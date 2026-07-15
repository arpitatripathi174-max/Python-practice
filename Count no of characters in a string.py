str=input("enter a str")
count=0
for i in str:
  if i.isalnum():
    count+=1
print("total characters in a str",count)
