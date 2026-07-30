print("\n-------Passing String and Number Arguments--------")

def greet(name):
    print("Hello", name)

greet("ALi")    

print("\n-------Passing String and Number Arguments--------")

def show_profile(name, age, city):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")

show_profile("ALi",25, "Karachi")
print()
show_profile("Sara", 32, "Lahore")

print("\n-------Passing a List as an Argument--------")

def calculate_total(prices):
    total = 0
    for price in prices:
        total += price
    print("Total Items:", prices)
    print("Total Price: ", total)

cart1 = [455,87,90,45,23,45]  
calculate_total(cart1)
calculate_total([45,67,67,11])

print("\n-------Passing an Expression as an Argument--------")

def show_square(number):
    print(f"Square of {number} is {number ** 2}") 

x = 5
y = 3

show_square(x + y)
show_square(10)
show_square(x * 2)


print("\n -------Multiple Arguments with Dictionary Logic--------")

def grade_checker(student_name, subject, marks):     # three arguments expected
    grade_scale = {                                     # revising: dictionary
        "A": 90,
        "B": 75,
        "C": 50
    }

    if marks >= grade_scale["A"]:                        # revising: if-elif-else
        grade = "A"
    elif marks >= grade_scale["B"]:
        grade = "B"
    elif marks >= grade_scale["C"]:
        grade = "C"
    else:
        grade = "F"

    print(f"{student_name} scored {marks} in {subject} -> Grade {grade}")

grade_checker("Ahmed", "Math", 92)
grade_checker("Hina", "Science", 68)
grade_checker("Bilal", "English", 40)

print("\n-------Passing Variables Holding Complex Data--------")

def compare_two_lists(list_a, list_b):           # two arguments, both expected to be lists
    common_items = []                               # revising: empty list (basket pattern)

    for item_a in list_a:                             # revising: nested for loop
        for item_b in list_b:
            if item_a == item_b:                         # revising: comparison + logical check
                common_items.append(item_a)                # revising: .append()
                break                                        # revising: break — stop inner loop once matched

    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Common items: {common_items}")

class_a_students = ["Ali", "Sara", "Ahmed", "Hina"]
class_b_students = ["Ahmed", "Bilal", "Hina", "Zara"]

compare_two_lists(class_a_students, class_b_students)    # passing two existing variables as arguments








































