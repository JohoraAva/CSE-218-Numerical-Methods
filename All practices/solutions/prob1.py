list1 = [1,2,3,3,4]
list2 = [3,4,5,6,7]
output = []
for elem in list1:
    if elem not in list2:
        output.append(elem)

for elem in list2:
    if elem not in list1:
        output.append(elem)
    
print(output)
