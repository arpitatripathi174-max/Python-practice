n=[12,23,34]
largest=second=n[0]
for i in n:
  if i>largest:
    largest=i
  elif i>second and i!=largest:
    second=i

print("the second no is",second)
