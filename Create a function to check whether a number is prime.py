def prime(n):
  if n<=1:
    return false
  else:
    for i in range(2,n):
      if n%i==0:
        return false
      return true

n=int(input("enter no")
if prime(n):
      print("prime no")
      else:
      print("Not prime")
        
