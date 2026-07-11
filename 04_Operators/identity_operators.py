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