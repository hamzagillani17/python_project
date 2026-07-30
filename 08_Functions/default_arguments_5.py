print("\n-------Simple Default Argument--------")

def greet(name = "Guest"):
    print("Hello, ",name, "Welcom")

greet()  # no argument -> uses default value "Guest"
greet("ALI")    # argument given -> overrides default
greet("SARA")    # different argument -> overrides default again


print("\n-------Multiple Default Arguments--------")

def calculate_price(price, discount = 0, tax = 0):  # 'discount' and 'tax' have defaults
    final_price = price - (price * discount / 100)  # applying discount
    final_price = final_price + (final_price * tax / 100) #applying tax

    if discount > 0:
        print(f"Original: {price}, Dicount: {discount}%, Tax: {tax}%, Final: {final_price:.2f}")
    else:
        print(f"Original: {price}, No discount, Tax: {tax}%, Final: {final_price:.2f}")


calculate_price(1000)                    # uses default discount=0 and tax=5
calculate_price(1000, 10)                 # discount overridden to 10, tax still default 5
calculate_price(1000, 10, 15)              # both discount and tax overridden        


print("\n-------Default Arguments with Return and Dictionary--------")

def create_profile(name, city="Unknown", age=18, is_student=True):     # THREE default arguments
    profile = {                                                           # revising: dictionary building
        "name": name,
        "city": city,
        "age": age,
        "is_student": is_student
    }

    if profile["is_student"] and profile["age"] < 25:                     # revising: logical 'and'
        status = "Young student"
    elif profile["is_student"]:
        status = "Student"
    else:
        status = "Working professional"

    profile["status"] = status
    return profile                                                          # revising: return a dictionary

# using only the required argument, rest use defaults
profile1 = create_profile("Ali")
print(profile1)

# overriding some defaults but not all
profile2 = create_profile("Sara", city="Lahore", age=22)
print(profile2)

# overriding everything
profile3 = create_profile("Ahmed", "Karachi", 35, False)
print(profile3)


print("\n-------Default Argument Controlling a Loop--------")

def print_table(number, rows=10):          # 'rows' defaults to 10
    i = 1
    while i <= rows:                          # revising: while loop
        print(f"{number} x {i} = {number * i}")
        i += 1
    print()

print_table(5)                                # uses default rows=10, prints full table
print_table(3, 5)                              # overriding rows to only print 5 lines


print("-------Default Argument with List Processing--------")

def show_top_students(students, top_count=3):        # 'top_count' defaults to 3
    sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)   # revising: sorted() with lambda

    print(f"Top {top_count} students:")
    for i in range(top_count):                            # revising: range() based loop
        name, marks = sorted_students[i]                     # revising: tuple unpacking
        print(f"  {i+1}. {name}: {marks}")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78, "hina": 95, "bilal": 88}

show_top_students(student_marks)                # uses default top_count=3
print()
show_top_students(student_marks, 2)               # overriding to show only top 2




