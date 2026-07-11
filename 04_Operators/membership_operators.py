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


print("\n======= NOT IN==========")
'''The 'not in' Operator
The "not in" operator is used to check a sequence with the given value
is not present in the object like string, list, tuple, etc.'''

print(name," in ", Statment_ver, ": ",name not in Statment_ver)
print(country, " in ", Statment_ver, ": ", country not in Statment_ver)
print(city, "in ", Statment_ver,": ",city not in Statment_ver)
print(age,"in ",Statment_ver,": ",str(age) not in Statment_ver)

print("\n---------Membership Operator with Lists----------")

student = ["Ali", "Ahmad", "Gillani", "Zain","Sara"]
x = "Zain"
y = "Mubeen"
print("Zain is in student list: ",x in student)
print("Zain is in student list: ","zain" in student)
print("Mubeen is in student list: ",y in student)
print("Zain is in student list: ","Sara" not in student)

number = [10,20,30,40,50,[89,90]]
print([89,90] in number)
print(25 not in number)
a = 50
b = 40
c = a-b
print(c in number)

print("\n----------Membership Operator with Tuples---------")

color = ("Red","Black","Orang","Green",["green,rot"],34,12,90,(30,60))
print(color)

print(10 in color) #False
print("Red in this color tuples: ", "Red" in color) #True
print("green,rot is in color tuples: ",["green,rot"] in color) #True
print("(30,60) in in color tuples:", (30,60) in color ) #True
print("Black" not in color) #False

print("---------Membership Operator with Sets----------")

languages = {"Python","Java","C++","JavaScript",45,78,98,(34,12,"Ruby")}
print(languages)
print("Python" in languages)
print("Ruby" not in languages)
print(34 not in languages)
print((34,12,"Ruby") in languages)

print("\n---------Membership Operator with Dictionaries-------------")

personal_info = {"name":"Ali", "age":22,"roll_no":"12432", "City":"Hamburg", "mobile":"12121212"}

print("name" in personal_info)


# Use values functiom
print("Ali" in personal_info) #False because in work only Key
print("Ali" in personal_info.values()) #we can chk use values() function
print("age : ",22 in personal_info.values())

#Use item() function
print("use item function: ",("name","Ali") in personal_info) #False
print("key + value using items() function: ",("name","Ali") in personal_info.items()) #for hole item  #True
print("key + value using items() function: ",("age",22) in personal_info.items())


print("Salary ","salary" in personal_info) #False
print("Salary ","salary" not in personal_info) #True

print("\n------Membership Operator with Range-------")

range_numbers = range(1,11)
print(range_numbers)  #as is it print (1,11)
print(list(range_numbers))  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in range_numbers) #True  because above 5 is exist.

range_numbers_1 = range(0,21,2)
print(list(range_numbers_1)) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(14 in range_numbers_1)    #True
print(7 in range_numbers_1) #False

print("\n-----------Membership with Bytes--------------")

data = bytes([10,20,30,40])
print(data) #b'\n\x14\x1e('

print(20 in data) #True
print(20 not in data) #False

print("\n-----------Membership with Bytearray-------------")

bytearray_ver = bytearray([10,20,30,40])

print(30 in bytearray_ver) #True
print(0 not in bytearray_ver) #True

print("\n------Selenium Real Examples-------")

title = "Google Login Page"
print("Login" in title) #Ture

url = "https://amazon.de/login"
print("login" in url) #True


message = "Password changed successfully"
print("Error" not in message) #True


available_buttons = ["Login","Register","Logout"]
print("Login" in available_buttons) #True

supported_browsers = {"Chrome","Edge","Firefox"}
print("Chrome" in supported_browsers) #True


