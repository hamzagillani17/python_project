square = lambda x: x * x     # normal function jesa hi kaam karta hai
print(square(5))               # Output: 25

def square(x):          # normal function — 2 lines
    return x * x

square = lambda x: x * x    # lambda — 1 line, same kaam

print("-------Basic Lambda--------")

add = lambda a, b: a + b        # lambda with two parameters

print(add(5, 3))
print(add(10, 20))

print("-------Lambda with Condition--------")

check_even = lambda num: "Even" if num % 2 == 0 else "Odd"     # conditional expression inside lambda

print(check_even(10))
print(check_even(7))


print("-------Lambda with sorted()--------")

students = [("Ali", 85), ("Sara", 92), ("Ahmed", 78)]

sorted_students = sorted(students, key=lambda x: x[1])     # sort by marks (2nd item of each tuple)

print(sorted_students)


