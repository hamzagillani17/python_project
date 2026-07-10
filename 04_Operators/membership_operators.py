print("===========Membership Operators==========\n")

'''The membership operators in Python help us determine whether an item is present in a given container type object,
or in other words, whether an item is a member of the given container type object.

Types of Python Membership Operators
Python has two membership operators: in and not in. Both return a Boolean result.
The result of in operator is opposite to that of not in operator.'''

'''The 'in' Operator
The "in" operator is used to check whether a substring is present in a bigger string,
any item is present in a list or tuple, or a sub-list or sub-tuple is included in a list or tuple.'''

print("\n=======IN==========")

Statment_ver = "ich bin Gillani und ich komme aus pakistan, ich bin 22  jahre alt"

name = "Gillani"
country = "pakistan"
city =  "Lahore"
age = 22

print(name," in ", Statment_ver, ": ",name in Statment_ver)
print(country, " in ", Statment_ver, ": ", country in Statment_ver)
print(city, "in ", Statment_ver,": ",city in Statment_ver)
print(age,"in ",Statment_ver,": ",str(age) in Statment_ver)




'''The 'not in' Operator
The "not in" operator is used to check a sequence with the given value
is not present in the object like string, list, tuple, etc.'''