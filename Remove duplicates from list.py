list=[12,23,23 34,12,23]
new_list=[]
for i in list:
  if i not in new_list:
    new_list.append(i)

print("list after removing duplicates ",new_list)
