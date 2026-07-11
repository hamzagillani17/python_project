print("=========Identity Operators===========")

'''The identity operators compare the objects to determine whether they share the same memory
and refer to the same object type (data type).'''

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
c = a
print(a is b, id(a))
print(a == b, id(b))
print(a is c, id(c))

element = None

print(element is None, id(element))
print(element == None,id(element))

str = "abc"
str1 = "abc"

print(str is str1,id(str))
print(str == str1,id(str1))

a = 10
b = 10
c = b

print(a is b)
print(a is c)

list1 = [1, 2, 3]
list2 = list1          # reference (same object)
list3 = list1.copy()   # naya object (alag memory)

print(list1 is list2)   # True
print(list1 is list3)   # False
print(list1 == list3)   # True (values same hain)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a

# Comparing and printing return values
print(a is not c)
print(a is not b)

# Printing IDs of a, b, and c
print("id(a) : ", id(a))
print("id(b) : ", id(b))
print("id(c) : ", id(c))

a=[1,2,3]
b=[1,2,3]
print ("id(a), id(b):", id(a), id(b))
print ("a is b:", a is b)
print ("b is not a:", b is not a)

print (id(a[0]), id(a[1]), id(a[2]))
print (id(b[0]), id(b[1]), id(b[2]))

a = [[10], [20]]
b = [[10], [20]]

print(id(a) == id(b))
print(id(a[0]) == id(b[0]))
print(id(a[0][0]) == id(b[0][0]))

x = [[100], [200]]
y = [[100], [200]]

print(id(x[0][0]) == id(y[0][0]))   # 100 chota integer nahi hai (256 se zyada)... predict karein!