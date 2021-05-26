list1 = [1,3,5,7,9]
list2 = [0,2,4,6,8]

for num in list2:
    list1.append(num)

list2.clear()

for num in list1:
    list2.append(num*2)

for num in list2:
    print(type(num))