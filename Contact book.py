contactbook={}
n=int(input("enter no of contacts"))
for i in range(n):
  name=input("enter contact name")
  phone=input("enter contact no")
  contactbook[name]=phone
  
print("\ncontactbook")

for name  in contactbook:
  print(name,":",contactbook[name])
