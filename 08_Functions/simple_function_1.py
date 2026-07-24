print("\n-------Simple Function: Greeting--------")

def say_hello():    # defining a simple function with no parameters
    print("Hello! welcom to python function")

say_hello() # calling the function once
say_hello() # calling it again — reusability in action


print("\n-------Simple Function with a Loop--------")

def print_number():
    for i in range(1,6):
        print("Number", i)
print_number() # calling the function runs the entire loop

print("\n-------Simple Function with If-Else--------")

def check_day():
    day = "Sunday"
    if day == "Sunday" or day == "Saturday":
        print(day, "is a weekend")
    else:
        print(day, "is a weekday")
check_day() # calling the function runs the if-else check

print("\n-------Simple Function with List and Loop--------")

def show_fruits():
    fruites = ["Apple", "Banana", "cherry", "Mango"]

    for fruit in fruites:
        print("Fruit:",fruit)
    print("Total Fruits:", len(fruites))  

show_fruits()      

print("\n-------Simple Function with Dictionary and While Loop--------")

def show_student_marks():
    student_marks = {"Ali" : 85 , "Sara" : 92, "Ahmad" : 76 }
    names = list(student_marks.keys()) #converting dict keys to a list
    i = 0

    while i < len(names):
        current_name = names[i]
        current_marks = student_marks[current_name]
        print(current_name, "scorde", current_marks)
        i += 1

show_student_marks() #calling the function 





