n=int(input("enter a no"))
rev=0
while i>0:
  rev=(rev*10)+i%10
  i=i//10
print("The reverse of a number is", rev)
