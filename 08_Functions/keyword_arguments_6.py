print("-------Basic Keyword Arguments--------")

def show_profile(name, age, city):        # three normal parameters
    print(f"Name: {name}, Age: {age}, City: {city}")

# positional way — order MUST match
show_profile("Ali", 25, "Karachi")

# keyword way — order does NOT matter, names decide where value goes
show_profile(age=25, city="Karachi", name="Ali")

# keyword way with different order again — still correct!
show_profile(city="Lahore", name="Sara", age=30)

print("-------Mixing Positional and Keyword Arguments--------")

def check_result(name, marks, subject):        # three parameters
    if marks >= 50:                              # revising: if-else
        print(f"{name} passed {subject} with {marks} marks")
    else:
        print(f"{name} failed {subject} with {marks} marks")

# first argument positional, rest keyword — this is ALLOWED
check_result("Ahmed", marks=75, subject="Math")

# first two positional, last keyword
check_result("Hina", 40, subject="Science")

print("-------Keyword Arguments with Defaults--------")

def create_account(username, email, country="Pakistan", is_active=True):    # two defaults
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Country: {country}")
    print(f"Active: {is_active}")
    print()

# using keyword arguments to skip the middle one and only set 'is_active'
create_account(username="ali123", email="ali@example.com", is_active=False)

# overriding country but keeping is_active default, using keywords in random order
create_account(email="sara@example.com", country="UK", username="sara_k")


print("-------Keyword Arguments in a Practical Function--------")

def generate_report(title, items, show_count=True, separator="-"):     # two defaults
    print(title)
    print(separator * len(title))                                        # revising: string repetition

    for item in items:                                                     # revising: for loop over list
        print(f"  {item}")

    if show_count:                                                          # revising: if condition
        print(f"Total items: {len(items)}")                                   # revising: len()
    print()

fruits = ["apple", "banana", "cherry"]

# calling with some keyword arguments, changing the separator
generate_report(title="Fruit List", items=fruits, separator="=")

# calling with show_count turned off using keyword
generate_report(title="Simple List", items=["a", "b"], show_count=False)




print("-------Keyword Arguments for Building a Complex Profile--------")

def build_employee(name, salary, department="General", experience=0, is_manager=False):   # 3 defaults
    employee = {                                                    # revising: dictionary building
        "name": name,
        "salary": salary,
        "department": department,
        "experience": experience,
        "is_manager": is_manager
    }

    # revising: logical operators (and/or) for bonus calculation
    if employee["is_manager"] and employee["experience"] >= 5:
        bonus = employee["salary"] * 0.20
    elif employee["is_manager"] or employee["experience"] >= 5:
        bonus = employee["salary"] * 0.10
    else:
        bonus = employee["salary"] * 0.05

    employee["bonus"] = bonus
    return employee                                                  # revising: returning a dictionary

# using keyword arguments to set specific fields in different orders
emp1 = build_employee(name="Ali", salary=50000, is_manager=True, experience=6)
emp2 = build_employee(salary=40000, name="Sara", department="IT")
emp3 = build_employee(name="Ahmed", salary=30000)

for emp in [emp1, emp2, emp3]:                                          # revising: for loop over a list
    print(f"{emp['name']}: Department={emp['department']}, Bonus={emp['bonus']:.0f}")





