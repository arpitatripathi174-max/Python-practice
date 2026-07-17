n=int(input("enter no")
if n<=1:
      print("Not prime")
else:
      for i in range (2,n):
      if n%i==0:
         print("Not prime")
      else:
         print("prime no")
