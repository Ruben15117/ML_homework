set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union = set1 | set2 
inters = set1 & set2
sym_diff = union - inters

print("Set 1:", set1)
print("Set 2:", set2)
print("Symmetric Difference:", sym_diff)


dict1 = {}
for i in range(1, 16):
    dict1[i] = i ** 2

print("dict1:", dict1)

dict2 = {i: i ** 2 for i in range(1, 16)}

print("dict2:",  dict2)
