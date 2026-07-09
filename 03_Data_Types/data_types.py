
# what is data type in python?
''' data type is a classification that specifies which type of value a variable has and 
    what type of operations can be performed on it. 
    In Python, data types are used to define the type of data that can be stored in a variable.'''
    
# There are 14 data types in python which are as follows:
# There are two types of datatypes user defined datatypes and built-in datatypes.
'''1- User defined datatypes are those which are created by the user,
   2- while built-in datatypes are those which are provided by python.'''
   
#    There are also further two types of datatypes mutable and immutable.
'''mutable means that the value of the variable can be changed after creation,
while immutable means that the value of the variable cannot be changed after creation.'''
     
# user-defined datatypes array, class, object, etc.

'''Built-in datatypes are those which are provided by python.'''  
#   1. Numaric datatypes: int, float, complex 
#   2. Boolean datatype: bool
#   3. None datatype: NoneType
#   4. Sequence datatypes: list, tuple, range
#   5. Text Sequence datatype: str
#   6. Set datatypes: set, frozenset
#   7. Mapping datatype: dict
#   8. Binary datatypes: bytes, bytearray, memoryview

'''mutable data types: list, set, dict, bytearray
   immutable data types: int, float, complex, bool, NoneType, tuple, frozenset, str, bytes, memoryview'''

# Type conversion in python
'''Type conversion is the process of converting one data type to another data type.
   There are two types of type conversion in python: implicit type conversion and explicit type conversion.'''
   
#    implicit type conversion

# 1. Numaric datatypes: int, float, complex 


int_a = 10 # int
float_b = 10.5 # float
complex_c = 3 + 4j # complex

int_plus_float = int_a + float_b #float
print("Integer + float value: ",int_plus_float,"datatype",type(int_plus_float))
int_complex = int_a + complex_c  #complex
float_plus_int = float_b + int_a #float
complex_plus_float = complex_c + float_b # complex
all_numeric_plues = int_a + float_b + complex_c #complex

print("Integer value",int_a,"datatype",type(int_a))
print("float value",float_b, "datatype",type(float_b))
print("complex value",complex_c,"datatype",type(complex_c))
print("----------------------------------------------------")
print("Integer + float value: ",int_plus_float,"datatype",type(int_plus_float))
print("Integer + complex value",int_complex,"datatype",type(int_complex))
print("float + Integer value",float_plus_int,"datatype",type(float_plus_int))
print("complex + float value",complex_plus_float,"datatype",type(complex_plus_float))
print("All numeric values",all_numeric_plues,"datatype",type(all_numeric_plues))
print("=--------------------------------------------------------")

#explicit type conversion

int_casting= 100
flot_casting = 50.55
complex_casting = 2 + 3j

int_to_float = float(int_casting) #float
int_to_complex = complex(int_casting) 

float_to_int = int(flot_casting)  #int
flot_to_complex = complex(complex_casting)

complex_to_int = int(int_casting)
complex_to_flot = float(flot_casting)

print("----------------------------------------------------")
print("Integer to float value: ",int_to_float, "datatype: ", type(int_to_float))
print("Interger to complex: ",int_to_complex, "datatpe: ",type(int_to_complex))

print("Flot to interger value: ",float_to_int, "datadype: ",type(float_to_int))
print("Flot to complex: ",flot_to_complex, "datatype: ",type(flot_to_complex))

print("Complex to integer value: ",complex_to_int,"datatype: ",type(complex_to_int))
print("Complex to float value",complex_to_flot,"datatype: ", type(complex_to_flot))
print("\n==========================bool========================")


#   2. Boolean datatype: bool

boolen_a_true = True # 1
print("when True refer in a variable: ",boolen_a_true, "datatype: ", type(boolen_a_true))

boolen_a_true = boolen_a_true + 2

# when add an integer in boolen then datatype result is also int
print("when boolen_a + any interger like 2 : ", boolen_a_true, "datatype: ", type(boolen_a_true))

boolen_to_int = int(boolen_a_true)
print("when boolen to interger convert: ",boolen_to_int, "datatype: ", type(boolen_to_int))


boolen_to_float= float(boolen_a_true)
print("when boolen to flot convert: ",boolen_to_float, "datatype: ", type(boolen_to_float))
# when add an float in boolen then datatype result is also float
boolen_to_float = boolen_to_float + 2.3
print("when add in boolen float to any float value 2.3 ",boolen_to_float, "datatype", type(boolen_to_float))

boolen_to_complex = True
boolen_to_complex= complex(boolen_to_complex)
print("when boolen to complex: ",boolen_to_complex, "datatype",type(boolen_to_complex))

boolen_b_false = False
boolen_a_true= True

add_boolen_true_and_false = boolen_b_false + boolen_a_true

print("when 2 boolen add: ", add_boolen_true_and_false, "datatype:", type(add_boolen_true_and_false)) 
value= True + 3+3j
print(value, type(value))
print("\n======================NoneType===============================")
# 3. None datatype: NoneType

''''Python also offers a special data type, known as NoneType. 
    This data type consists of only one value - None. It is used to represent the missing values, function return values, 
    and placeholders in Python.In order to create an object of NoneType class, 
    we can simply initialize a variable with None as the value.
    the nonetype represents the null type of values or absence of a value.'''


none_a = None

print(bool(none_a))
print(none_a is None)
print("None value",none_a,"datatype",type(none_a))
print("\n=====================LIST================================")


#   4. Sequence datatypes: list, tuple, range

#1-List

'''' List is one of the built-in data types in Python. 
     A Python list is a sequence of comma separated items, enclosed in square brackets [ ].
     The items in a Python list need not be of the same data type.
     
     A Python list is mutable. Any item from the list can be accessed using its index, and can be modified.
     One or more objects from the list can be removed or added. 
     A list may have same item at more than one index positions.
     append(), remove(), pop(), insert()'''

list_mix = ["Gillani",True+1, False ,None, 45, 23.45, 45+4j,[34,34,23,"Ali"]]
list_empty = []
print("Empty list :", list_empty) 
print(list_mix, type(list_mix))
print(list_mix)
list1 = ["Rohan", "Physics", 21, 69.75]
print(list1)

list_lenght= len(list_mix)
print("Lenght of List using function len():",list_lenght)

#indexing
print("Nested List: ", list_mix[7])
print(list_mix[0:4])
print(list_mix[4])
print(list_mix[-4])


print("\n====================Tupel===========================")
#2- Tupel

'''Tuple is one of the built-in data types in Python. A Python tuple is a sequence of comma separated items, 
   enclosed in parentheses ().
   The items in a Python tuple need not be of same data type.
   In Python, tuple is a sequence data type. It is an ordered collection of items.
   Each item in the tuple has a unique position index, starting from 0.

   In C/C++/Java array, the array elements must be of same type. On the other hand, 
   Python tuple may have objects of different data types.
   Python tuple and list both are sequences. One major difference between the two is,
   Python list is mutable, whereas tuple is immutable.
   Although any item from the tuple can be accessed using its index, 
   and cannot be modified, removed or added.
   
   Tuple is a built-in data structure in Python for storing a collection of objects.
   A tuple is quite similar to a Python list in terms of indexing, nested objects, and repetition;
   however, the main difference between both is that the tuples in Python are immutable,
   unlike the Python list which is mutable.
   count(), index()
   '''
tuple_mix = (56, "jhon", True, False, 45+3j, 45.344, [345,"Mola",34+4j])

tuple_empty = ()

tuple_comma = (50,)
print(tuple_comma)

print("Tuple mix: ",tuple_mix)
print("Empty tuple: ",tuple_empty)

tuple_lenght= len(tuple_mix)
print("Lenght of tuple using function len():",tuple_lenght)

#indexing 
print(tuple_mix[4])
print(tuple_comma[0]) # tuple index 1 occour error
#type
print("Type mix: ",type(tuple_mix),"tuple with comma:",type(tuple_comma),"Empty tuple",type(tuple_empty))

#Singel value will show in tuple others datatype like  INT or Float not tuple

single_integer = (20) #int type
print(single_integer,type(single_integer))

single_flot = (5654.6565)
print(single_flot,type(single_flot)) #float type


#3- Rang
''''The range data type is an immutable, ordered, indexed,
and memory-efficient sequence in Python that generates integer values using start,
stop, and step. It is mainly used for looping and counting operations.'''

range_ver = range(45,43,34)
print("Rang: ",range_ver, "datatype: ", type(range_ver))

range_empty = range(4,6)
print("Empty range: ",range_empty)

range_index = range(56+45,45)
print(list(range_index))

range_lenght = range(67,78,9)
print("Range lenght: ",len(range_lenght)) 

range_zero = range(0)
print(range_zero)

range_list = range(10,30)
make_list=list(range_list)
print("datatype: ",type(make_list),make_list)
#index
print("Index of value 7: ",make_list[7])
print("-index of -3",make_list[-3])

#value in -
range_list_minus = range(-20,-10)
make_list_minus=list(range_list_minus)
print("datatype: ",type(make_list_minus),make_list_minus)
#index
print("Index range of value 7: ",make_list_minus[7])
print("-index range of value -6: ",make_list_minus[-6])

print("\n=============5. Text Sequence datatype: str============")

#   5. Text Sequence datatype: str

''''A string in Python is a sequence of characters enclosed within quotation marks.
It can include letters, numbers, symbols, and even whitespace characters.
Python does not have a separate character data type, so even a single character is treated as a string of length 1.
For example, "welcome" is a string consisting of a sequence of characters such as 'w', 'e', 'l', 'c', 'o', 'm', 'e'.'''

str_ver = "My Name is Khan"
print("Lenght of Str: ",len(str_ver))
print("string use: ",str_ver, "datatype", type(str_ver))

#casting
str_int = "30"
str_to_int=int(str_int)
print("Casting str to int: ",str_to_int+20, "datatype: ", type(str_to_int))

str_float = "20.20"
str_to_float = float(str_float)
print("Casting str to float: ",str_to_float+20.8, "datatype: ", type(str_to_float))

# multiline string

str_multiline = '''Hallo! ich heisse Gillani,
ich komme aus pakistan,
ich bin 22 jahre alt.'''
print(str_multiline)

# index

print("index of 7: ", str_multiline[7])
print("index 0:15: ",str_multiline[0:25])
print("-indexi -25:-1: ",str_multiline[-20:-1])


# 6. Set datatypes: set, frozenset

print("\n===================set==========================")

#SET
'''In Python, a set is an unordered collection of unique elements.
Unlike lists or tuples, sets do not allow duplicate values i.e.
each element in a set must be unique. Sets are mutable,
meaning you can add or remove items after a set has been created.

Sets are defined using curly braces {} or the built-in set() function.
They are particularly useful for membership testing, removing duplicates from a sequence,
and performing common mathematical set operations like union, intersection, and difference.


'''
set_ver={1,2,3,4,5,6}
print(set_ver,type(set_ver))

set_function = set([6,5,4,3,2,1])
print(set_function,type(set_function))

set_mix = {1,1,3,2,43,1,0,"Ali ahmad",3.43,34+3j,(345+343+34,"WAH JI WAH")}
print(set_mix)

set_adding = {1,2,3,4}
set_adding.add(5)
print(set_adding) #{1,2,3,4,5}
set_adding.remove(1)
print(set_adding) #remove 1

set_str = {"Ali", "Ahmad", "Jhon", "wanda"}
print(set_str)
set_str.add("pappi")
print("add pappi: ", set_str)
set_str.remove("wanda")
print("Remove wanda:" ,set_str)

set_of_fruits = {'apple', 'mango', 'banana', 'orange', 'guava'}  
# printing the set  
print("Set of Fruits:", set_of_fruits)    
    
# using the add() method    
set_of_fruits.add('grapes')  
    
# printing the updated set    
print("Updated Set of Fruits:", set_of_fruits)

# simple example to show how to remove elements from the set  
# given set  
subjects = {'physics', 'chemistry', 'english', 'biology', 'computer', 'maths'}  
print("Given Set:", subjects)  
  
# removing a specified element from the set  
subjects.remove('maths')      # using remove()  
print("Updated Set (Removed 'maths'):", subjects)  
  
# removing a specified element from the set  
subjects.discard('chemistry')      # using discard()  
print("Updated Set (Removed 'chemistry'):", subjects)  
  
# removing a random element from the set  
subjects.pop()      # using pop()  
print("Updated Set (Removed a random element'):", subjects)  
  
# removing all elements from the set  
subjects.clear()      # using clear()  
print("Updated Set (Removed all elements):", subjects)  

# simple example on union of sets  
  
set_A = {1, 2, 3}     # set A  
print("Set A:", set_A)  
  
set_B = {2, 3, 4, 5}  # set B  
print("Set B:", set_B)  

#1. Union of Sets
'''In mathematical terms, union of sets A and B is defined as the set of all those elements
which belongs to A or B or both and is denoted by A∪B.
A∪B = {x: x ∈ A or x ∈ B}
'''

print("\nUnion of Sets A and B:")       # union of sets  
print("Method 1:", set_A | set_B)       # using |  
print("Method 2:", set_A.union(set_B))  # using union()  

# 2. Intersection of Sets
'''In mathematical terms, intersection of two sets A and B is defined as the set of all those elements
which belongs to both A and B and is denoted by A∩B.
A∩B = {x: x ∈ A and x ∈ B}
'''  
# simple example on intersection of sets  
  
set_A = {1, 2, 3}     # set A  
print("Set A:", set_A)  
  
set_B = {2, 3, 4, 5}  # set B  
print("Set B:", set_B)  
  
print("\nIntersection of Sets A and B:")       # intersection of sets  
print("Method 1:", set_A & set_B)              # using &  
print("Method 2:", set_A.intersection(set_B))  # using intersection()  

#3. Difference of Sets
'''In mathematical terms, difference of two sets A and B is defined as the set of all those elements
which belongs to A, but do not belong to B and is denoted by A-B.

A-B = {x: x ∈ A and x ∉ B}
'''
# simple example on difference of sets  
  
set_A = {1, 2, 3}     # set A  
print("Set A:", set_A)  
  
set_B = {2, 3, 4, 5}  # set B  
print("Set B:", set_B)  
  
print("\nA - B:")       # difference of sets  
print("Method 1:", set_A - set_B)       # using -  
print("Method 2:", set_A.difference(set_B))  # using difference()  
  
print("\nB - A:")  
print("Method 1:", set_B - set_A)       # using -  
print("Method 2:", set_B.difference(set_A))  # using difference()

print("\n-----------------------Frozenset in Python--------------------")

#- 2 Frozenset in Python
'''A frozenset is an immutable version of a set, 
which means we cannot add or remove elements after it is created.
It is created using the built-in frozenset() function.

Explanation:
we have used the frozenset() function to return the frozenset object of the passed iterable.
Frozensets are hashable objects that can be used as keys in dictionaries or elements of other sets.
'''
# simple example to create a frozenset  
  # using the frozenset() function  

frozen_set = frozenset(['one', 'two', 'three', 'four', 'five'])  
  
# printing results  
print(frozen_set)  
print(type(frozen_set))  # returning type  

print("\n=============7. Mapping datatype: dict=============")

#   7. Mapping datatype: dict
#dict

'''Python dictionary is used to store data in key-value pairs.
A dictionary is an unordered and mutable collection of data stored in key-value pairs.
Each key is unique and is used to access its corresponding value.
Each key-value pair is separated by a comma and enclosed within curly braces {}.
The key and value within each pair are separated by a 
colon (:), forming the structure key:value.
'''

dict_ver = {"0" : "Ali", "1" : "Ahmad", "2" : "Waqas"}
print("Dict value", dict_ver, "datatype: ", type(dict_ver))

# using empty {dict}
dict_empty = {}
print("empty dict", dict_empty)

# finding length of the dictionary  
print("Size of Data:", len(dict_ver)) # using len()  

# using dict function dict()
dict_fun = dict(Name = "Amhad", age = 22, city = "Lahore")
print("dict function",dict_fun, "datatype: ", type(dict_fun))
city1 = dict_fun["city"]
print("Accessing value from dict function: ",city1)
# accessing value with get() function
age0 = dict_fun.get("age")
print("Accessing value from get(): ",age0)

'''You can assign a value to more than one keys in a dictionary, 
but a key cannot appear more than once in a dictionary.'''

personal_info = {"name":"Ali", "age":"21", "roll_no":"12432", "City":"Hamburg",
                  "mobile":"12121212"}
print(personal_info)
personal_info_1 = {"name":"Ali","name" : "waqas","age":"22", "age":"21", "roll_no":"12432", "City":"Hamburg",
                  "mobile":"12121212"} #using duble key
print(personal_info_1) #using duble key
# simple example to check membership   
 
print("Is Name of Student exisit in Personal_infomation: '?:", "name" in personal_info)  
print("Is Graduation year of Student exisit in Personal_infomation: '?:", 'Graduation year' in personal_info)
# using 'in' and 'not in' operators  
print("Is Roll number of Student not exisit in Personal_infomation: '?:", 'roll_no' not in personal_info) 
print("Is Roll number of Student exisit in Personal_infomation: '?:", 'roll_no'  in personal_info) 

# Accessing Dictionary Items
#You can access the value associated with a specific key using square brackets [].
#or the get() method 

student_info = {
   "Name": "Gillani",
   "age": 23,
   "major": "Computer Science"}
# Accessing values using square brackets
name = student_info["Name"]
age = student_info["age"]
print("Accesing Dictionary with []",name,age)

# Accessing values using the get() method
name1 = student_info.get("major")
print(name1)

# Modifying an existing key-value pair

student_info["age"] = 25
print("age modify pervious age was 23 now updated age is: ",student_info)

# Adding a new key-value pair
student_info["graduation year"] = 2020
print("Add key and value: ",student_info)

# Removing Dictionary Items
# You can remove items using the del statement, the pop() method, or the popitem() method −

del student_info["age"]
print("Removing with del ",student_info)

pop_value = student_info.pop("graduation year") #using pop() 
print("Poped value: ",pop_value,"after removing", student_info)

popped_item = student_info.popitem()  # using popitem()  
print("Updated Dictionary (Removed last item using popitem):", student_info)  
print("Popped Item:", popped_item)  
  
student_info.clear()  # using clear()  
print("Update Dictionary (Removed all items):", student_info)  

print("\n==========8.Binary datatypes: bytes, bytearray, memoryview ==========")

#bytes
'''bytes is an immutable sequence data type that stores binary data as a sequence of integers ranging from 0 to 255.
It is mainly used for handling binary files, network communication, APIs, images, audio, video, and data encoding/decoding.
We can create bytes in Python using the built-in bytes() function or by prefixing a sequence of numbers with b.'''

# Using bytes() function to create bytes
bytes_obj = bytes([65, 66, 67, 68, 69])  
print(bytes_obj,"Index: ",bytes_obj[4],"Negative Index",bytes_obj[-4],"Slicing: ",bytes_obj[0:4],"Length",len(bytes_obj), "datatype: ",type(bytes_obj),bytes_obj)  
bytes_obj=bytes_obj.decode()
print("bytes_obj convert",bytes_obj)
print("bytes_obj encode",bytes_obj.encode())
bytes_obj_b = b"65, 66, 67, 68, 69" # Using prefix 'b' to create bytes
print(bytes_obj_b, "datatype: ","Index:",bytes_obj_b[3],"Negative Index: ",bytes_obj_b[-3], type(bytes_obj_b))

#From string
bytes_str_text = "python"
bytes_str_text = bytes(bytes_str_text, "utf-8")
print(bytes_str_text,type(bytes_str_text))
x = chr(65)
print(x)

#bytearray

'''bytearray is a mutable, ordered, indexed sequence data type that stores binary data as integers from 0 to 255.
   It is used when binary data needs to be modified efficiently'''

# using bytearry() function to create byteaeey()

bytearray_obj = bytearray([72, 101, 108, 108, 111])

print("bytearray_obj",bytearray_obj, "datatype", type(bytearray_obj))

# Creating a bytearray by encoding a string
val = bytearray("Hello", 'utf-8')  
print(val) 

bytearray_obj[0] = 67
print(bytearray_obj)

x = bytearray(b"python")
print(x[0])

print(chr(65))

print("\n===============Python Memoryview Data Type===============")

# Python Memoryview Data Type
data = bytearray(b'Hello, world!')
view = memoryview(data)
print(view)

import array
arr = array.array('i', [1, 2, 3, 4, 5])
view = memoryview(arr)
print(view)

data = b'Hello, world!'
# Creating a view of the last part of the data
view = memoryview(data[7:])  
print(view)