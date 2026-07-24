print("\n===========basics Function============")

'''Basics of function in python A function is a reusable block of code 
   that performs a specific task.

In Python, you define a function with def
It can accept inputs called parameters
It can return a result with return
It helps organize code, avoid repetition, and make programs easier to read'''


print("\n-------Basics Function-------")

def  first_function():
    print("This is my First Function")
first_function()

print("\n------------add function----with out return -------")

def add_function(a,b):
    z= a + b
    print(z)
res = add_function(5,5)

print("\n--------Function with Parameter, No Return (Print-based)---------")
'''Functions can accept parameters, which are values passed into the function when it is called.
These parameters allow you to customize the behavior of the function based on the input provided.'''

def show_name(name):
    print("Hello",name)

show_name("Gillani")

result_show = show_name("Syed")
print(result_show)

print("------Function with Parameter AND Return (Return-based)-------")
'''Functions can also return values using the return statement.
This allows you to capture the result of a function call and use it later in your program.'''

def get_greeting(name):
    return "Hello " + name


print(get_greeting("Ali"))

message = get_greeting("Bilal")
print(message)

print("------Multiple Parameters Function (Positional)--------")
'''In Python, you can define functions that accept multiple parameters.
These parameters can be passed in a specific order (positional arguments) or 
by explicitly naming them (keyword arguments).'''

def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(60, 80)  # Positional arguments
print("Area of rectangle:", result)
print(calculate_area(10, 5))



def subtract(a, b):
    return a - b
print(subtract(10, 3))    # a=10, b=3  -> Output: 7
print(subtract(3, 10))    # a=3, b=10  -> Output: -7  (result badal gaya, kyunke position badli)
print(subtract(b=10, a=3))  # a=3, b=10  -> Output: -7  (keyword arguments, position matter nahi karti)

print("------Keyword Arguments-------------")
'''Keyword arguments allow you to specify the values of parameters by name when calling a function.
This can make your code more readable and allows you to provide arguments in any order.'''

def introduce_person(name, age, city):
    print(f"My name is {name}, I am {age} years old, and I live in {city}.")

introduce_person("karachi", 25, "Karachi")  # Positional arguments
introduce_person(name="Ali", age=25, city="Karachi")
introduce_person(city="Lahore", name="Sara", age=30)# Keyword arguments allow you to specify the values of parameters by name when calling a function.

def student_info(name, age, grade):
    return f"Student Name: {name}, Age: {age}, Grade: {grade}"

print(student_info(name="Ahmed", age=25, grade="A"))
print(student_info(grade="B", name="Sara", age=30))  # Keyword arguments allow you to specify the values of parameters by name when calling a function.


print("\n------Default Parameters-------------")
'''Default parameters allow you to specify default values for function parameters.
If a caller does not provide a value for a parameter with a default, the default value is used.'''

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
print(greet("Ali"))  # Uses default greeting
print(greet("Sara", "Hi"))  # Overrides default greeting
print(greet("Bilal", greeting="Hi"))  # Overrides default greeting


print("\n------Arbitrary Arguments--Variable-length Arguments (*args)-------------")
'''In Python, you can define functions that accept an arbitrary number of arguments using *args.
This allows you to pass a variable number of positional arguments to the function.'''

def multiply_all(*numbers):        # '*numbers' - koi bhi ginti ke arguments le sakta hai
    result = 1
    for num in numbers:          # 'numbers' andar ek TUPLE ban jata hai
        result *= num
    return result

print(multiply_all(2, 3))               # Output: 6
print(multiply_all(2, 3, 4, 5))       # Output: 120 - jitne bhi do, sab handle ho jayenge

print("\n------Arbitrary Arguments--Variable-length Arguments (*args)-------------")

def add_all(*numbers):        # '*numbers' - koi bhi ginti ke arguments le sakta hai
    total = 0
    for num in numbers:          # 'numbers' andar ek TUPLE ban jata hai
        total += num
    return total

print(add_all(1, 2))               # Output: 3
print(add_all(1, 2, 3, 4, 5))       # Output: 15 - jitne bhi do, sab handle ho jayenge

print("\n------Arbitrary Keyword Arguments--Variable-length Keyword Arguments (**kwargs)-------------")
'''In Python, you can define functions that accept an arbitrary number of keyword arguments using **kwargs.
This allows you to pass a variable number of named arguments to the function.'''

def print_student_info(**kwargs):  # '**kwargs' - koi bhi ginti ke keyword arguments le sakta hai
    for key, value in kwargs.items():  # 'kwargs' andar ek DICTIONARY ban jata hai
        print(f"{key}: {value}")

print_student_info(name="Ali", age=20, grade="A")
print_student_info(name="Sara", age=22, grade="B", city="Karachi")  # Additional keyword argument 'city'



print("\n------Function Annotations-------------")
'''Function annotations are a way to attach metadata to function parameters and return values.
They can be used for documentation, type hints, or other purposes.'''

def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age} years old."
print(greet("Ali", 25))



def add_numbers(a: int, b: int) -> int:    
    # a: int  -> hint ke 'a' integer hona chahiye
    # b: int  -> hint ke 'b' integer hona chahiye
    # -> int   -> hint ke function ka return integer hoga
    return a + b

print(add_numbers(5, 10))         # Output: 15 - theek kaam karta hai
print(add_numbers("5", "10"))     # Output: 510 - koi ERROR nahi aayi! (strings mil gayin)



def get_full_name(first: str, last: str) -> str:
    return first + " " + last

print(get_full_name("Ali", "Gillani"))  # Output: "Ali Gillani"


# Ise dekh kar aage kaam karne wala turant samajh jayega - "first aur last strings honi chahiye, return bhi string hoga"





print("\n------Nested Functions-------------")
'''Nested functions are functions defined inside other functions.
They can be useful for encapsulating functionality and creating closures.'''

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function
plus_five = outer_function(5)
print(plus_five(10))  # Output: 15




def outer_function(name):
    print("Outer function shuru")
    
    def inner_function():          # ye function 'outer_function' ke ANDAR define hua hai
        print("Inner function chal raha hai, name hai:", name)   # outer ka 'name' bhi dikh raha hai
    
    inner_function()      # inner function ko outer ke ANDAR hi call kiya
    print("Outer function khatam")

outer_function("Ali")



print("--------Positional-Only Arguments----------")
'''positonal-only argument '''

def calculate_power(base, exponent, /):    # '/' ke pehle wale sab positional-only hain
    return base ** exponent

print(calculate_power(2, 3))          # ✅ Sahi - positional tareeqe se diya, Output: 8
#print(calculate_power(base=2, exponent=3))   # ❌ ERROR! naam se dena allowed nahi


print("----------Keyword-Only Arguments (*)------------")

def create_account(username, *, role="user", active=True):    
# '*' ke baad wale sab (role, active) sirf keyword se dene honge
    return f"{username} - Role: {role}, Active: {active}"

print(create_account("Ali", role="admin", active=False))   # ✅ Sahi - naam se diya
#print(create_account("Ali", "admin", False))                  # ❌ ERROR! position se nahi de sakte



#combine (Positional-only + Normal + Keyword-only)
def process_order(order_id, /, item, *, discount=0):
    # order_id -> SIRF position se
    # item -> position YA keyword dono se
    # discount -> SIRF keyword se
    return f"Order {order_id}: {item}, Discount: {discount}%"

print(process_order(101, "Laptop", discount=10))       # ✅ Sahi
print(process_order(101, item="Laptop", discount=10))   # ✅ Sahi (item keyword se bhi de sakte)
#print(process_order(order_id=101, item="Laptop"))          # ❌ ERROR - order_id keyword se nahi de sakte


print("\n----------------Variable Scope-----Local Scop---Global Scop----------")
'''Scope The scope of a variable in Python is defined as the specific area or
region where the variable is accessible to the user.
The scope of a variable depends on where and how it is defined. '''

print("----------global variables--------------")

#global variables
name = "Ali Murtaza"
marks = 50
def myfunction():
   # accessing inside the function
   print("name:", name)
   print("marks:", marks)
# function call   
myfunction()

x = 100    # ye GLOBAL scope mein hai - poore program mein dikhega
def my_function():
    y = 50    # ye LOCAL scope mein hai - sirf is function ke andar dikhega
    print("Function ke andar x (global):", x)   # global 'x' ko function ke andar bhi access kar sakte hain
    print("Function ke andar y (local):", y)

my_function()
print("Function ke bahar x (global):", x)
#print("Function ke bahar y (local):", y)     # ❌ ERROR! - 'y' function ke bahar exist nahi karta



counter = 0    # global variable
def increase_counter():
    global counter     # ye batata hai "main global wala 'counter' use/change karunga, naya local mat banao"
    counter += 1

increase_counter()
increase_counter()
print(counter)     # Output: 2 - global 'counter' actually change hua

'''counter = 0
def increase_counter_wrong():
    counter += 1    # ❌ ERROR! - Python isay naya LOCAL variable samajhta hai, aur += se pehle uski value nahi milti

increase_counter_wrong()'''

print("\n---------Nonlocal Variables-------------")
'''The Python variables that are not defined in either local or global scope are called nonlocal variables.
They are used in nested functions."
'''

def yourfunction():
   a = 5
   b = 6 
   # nested function
   def myfunction():
      # nonlocal function 
      nonlocal a
      nonlocal b
      a = 10
      b = 20 
      print("variable a:", a)
      print("variable b:", b)
      return a+b

   print (myfunction())
yourfunction()

print("\n-------------Lambda (Anonymous Function)------------")

# Normal function
def square(x):
    return x * x

# Same kaam, lambda se
square_lambda = lambda x: x * x

print(square(5))            # Output: 25
print(square_lambda(5))      # Output: 25




add = lambda a, b: a + b
print(add(5, 10))    # Output: 15



students = [("Ali", 85), ("Sara", 92), ("Ahmed", 78)]

# List ko marks (doosra element) ke hisaab se sort karna
sorted_students = sorted(students, key=lambda student: student[1])
print(sorted_students)


