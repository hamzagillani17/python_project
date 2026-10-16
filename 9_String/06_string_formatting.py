"""
====================================================
09_Strings / 06_string_formatting.py
====================================================
Topic: String Formatting
====================================================
"""
# Program 1: Concatenation (needs str() for the number)
name = "Ali"
age = 22
print("My name is " + name + " and I am " + str(age) + " years old")

# Program 2: The same message using an f-string
print(f"My name is {name} and I am {age} years old")

# Program 3: Compare both results
msg1 = "Hello " + name + ", you are " + str(age)
msg2 = f"Hello {name}, you are {age}"
print(msg1 == msg2)     # True - same text, formatting is just easier to read


# =====================================================
# Concept 2: % Formatting (Old Style)
# =====================================================
"""
Definition:
The oldest formatting style in Python. Placeholders start with %:
%s = string, %d = integer, %f = float.
Values are given after a % sign, inside a tuple if there are several.
You will still see it in older code, but new code uses f-strings.
"""

# Program 1: Insert a string and an integer
name = "Ali"
age = 22
print("My name is %s and I am %d years old" % (name, age))

# Program 2: Control decimal places with %.2f
price = 99.5
print("Price: %.2f" % price)       # Price: 99.50

# Program 3: Use width with %d and %s
print("ID: %5d | Name: %-10s | End" % (42, "Sara"))
# %5d  -> number in a width of 5 (right aligned)
# %-10s -> text in a width of 10 (left aligned because of the minus)

# =====================================================
# Concept 3: .format() Method
# =====================================================
"""
Definition:
.format() fills the {} placeholders of a string with the values
given inside its brackets, in order.
"""

# Program 1: Basic .format() with two values
print("My name is {} and I am {} years old".format("Ali", 22))

# Program 2: Use .format() with variables
product = "Laptop"
price = 999.5
print("Product: {}, Price: {}".format(product, price))

# Program 3: Add a format specifier inside the braces
print("Price: {:.2f}".format(999.5))    # Price: 999.50

# =====================================================
# Concept 4: Positional Placeholders
# =====================================================
"""
Definition:
Numbers inside the braces, like {0} and {1}, choose which value goes
where (counting from 0). The same value can be used more than once.
"""

# Program 1: Choose values by position
print("{0} is learning {1}".format("Ali", "Python"))

# Program 2: Change the order by changing the numbers
print("{1} is learning {0}".format("Ali", "Python"))

# Program 3: Reuse one value several times
print("{0} practices daily. {0} loves {1}.".format("Ali", "Python"))

# =====================================================
# Concept 5: Keyword Placeholders
# =====================================================
"""
Definition:
Names inside the braces, like {name}, are filled by keyword arguments
in .format(). The order of the arguments does not matter.
"""
# Program 1: Fill placeholders by name
print("{name} is {age} years old".format(name="Ali", age=22))

# Program 2: The order of the arguments does not matter
print("{name} lives in {city}".format(city="Lahore", name="Ali"))

# Program 3: Fill placeholders from a dictionary using **
student = {"name": "Sara", "age": 21, "city": "Karachi"}
print("{name}, {age}, {city}".format(**student))


# =====================================================
# Concept 6: f-strings
# =====================================================
"""
Definition:
An f-string starts with the letter f before the quote. Variable names
written inside {} are replaced by their values directly.
It is the most readable and the most used formatting style today.
(Available from Python 3.6)
"""

# Program 1: Basic f-string
name = "Ali"
age = 22
print(f"My name is {name} and I am {age} years old")

# Program 2: f-string with user input
user = input("Enter your name: ")
print(f"Welcome, {user}!")

# Program 3: Print a variable together with its name (debug style, Python 3.8+)
score = 95
print(f"{score=}")              # score=95

# =====================================================
# Concept 7: Expressions Inside f-strings
# =====================================================
"""
Definition:
Anything that produces a value can be written inside {}: maths,
method calls, function calls, even a conditional expression.
Python calculates it first and then puts the result in the text.
"""
# Program 1: Do maths inside the braces
a = 5
b = 10
print(f"Sum of {a} and {b} is {a + b}")

# Program 2: Call string methods inside the braces
name = "ali khan"
print(f"Title case: {name.title()}, Length: {len(name)}")

# Program 3: Use a conditional expression inside the braces
age = 15
print(f"Status: {'Adult' if age >= 18 else 'Minor'}")

# =====================================================
# Concept 8: Number Formatting
# =====================================================
"""
Definition:
After a colon inside {} you can write a format specifier that changes
how a number is shown: comma separators, percentages, binary, hex,
scientific notation and so on.
"""

# Program 1: Thousands separator with a comma
number = 1234567
print(f"{number:,}")            # 1,234,567

# Program 2: Percentage format
ratio = 0.856
print(f"{ratio:.1%}")           # 85.6%

# Program 3: Binary, hexadecimal and scientific notation
value = 255
print(f"{value:b}")             # 11111111  (binary)
print(f"{value:x}")             # ff        (hexadecimal)
print(f"{1234.5:e}")            # 1.234500e+03 (scientific)

# =====================================================
# Concept 9: Decimal Formatting
# =====================================================
"""
Definition:
.Nf shows a float with exactly N digits after the decimal point.
The value is rounded, not cut.
"""

# Program 1: Two decimal places
price = 99.987654
print(f"{price:.2f}")           # 99.99

# Program 2: Different numbers of decimal places
pi_value = 3.14159265
print(f"{pi_value:.0f}")        # 3
print(f"{pi_value:.4f}")        # 3.1416

# Program 3: Money format with dollar sign, comma and 2 decimals
amount = 1234567.891
print(f"${amount:,.2f}")        # $1,234,567.89

# =====================================================
# Concept 10: Alignment
# =====================================================
"""
Definition:
Alignment decides where the text sits inside a fixed-width space:
< = left, > = right, ^ = center.
"""

# Program 1: Left, right and center alignment
word = "Hi"
print(f"[{word:<10}]")          # [Hi        ]
print(f"[{word:>10}]")          # [        Hi]
print(f"[{word:^10}]")          # [    Hi    ]

# Program 2: Numbers are right-aligned by default, text is left-aligned
print(f"[{42:10}]")             # [        42]
print(f"[{'abc':10}]")          # [abc       ]

# Program 3: Align a small two-column list
print(f"{'Name':<10}{'Score':>6}")
print(f"{'Ali':<10}{95:>6}")
print(f"{'Sara':<10}{88:>6}")


# =====================================================
# Concept 11: Width
# =====================================================
"""
Definition:
A number after the colon sets the minimum width of the field.
If the text is shorter, the rest is filled with spaces.
If the text is longer, it is NOT cut.
"""

# Program 1: A fixed width for text
print(f"[{'Ali':10}]")          # [Ali       ]

# Program 2: A text longer than the width is not cut
print(f"[{'Automation':5}]")    # [Automation]

# Program 3: Build a table header with widths
print(f"{'Test Name':<20}{'Status':<10}{'Time':>8}")
print(f"{'Login Test':<20}{'Passed':<10}{'2.3s':>8}")
print(f"{'Logout Test':<20}{'Failed':<10}{'1.1s':>8}")


# =====================================================
# Concept 12: Padding
# =====================================================
"""
Definition:
Padding fills the empty space with a chosen character instead of
spaces. Write the fill character right after the colon, before the
alignment symbol. A leading 0 pads numbers with zeros.
"""

# Program 1: Zero padding for numbers
number = 5
print(f"{number:05}")           # 00005

# Program 2: Custom fill characters with alignment
word = "Hi"
print(f"{word:*^10}")           # ****Hi****
print(f"{word:-<10}")           # Hi--------
print(f"{word:.>10}")           # ........Hi

# Program 3: Clock style time (always two digits)
hour = 5
minute = 9
print(f"{hour:02}:{minute:02}") # 05:09


# =====================================================
# Concept 13: Professional f-string Usage
# =====================================================
"""
Definition:
In real projects, expressions, widths, alignment and decimal
formatting are combined in one f-string to build clean reports,
logs and test summaries.
"""

# Program 1: A formatted test report
test_name = "Login Test"
status = "Passed"
execution_time = 2.34567
pass_rate = 0.95

print("=" * 40)
print("Test Report")
print("=" * 40)
print(f"Test Name:      {test_name:<20}")
print(f"Status:         {status:<20}")
print(f"Execution Time: {execution_time:.2f} seconds")
print(f"Pass Rate:      {pass_rate:.1%}")
print("=" * 40)

# Program 2: A receipt built with a loop
items = [("Pen", 2, 10.5), ("Notebook", 3, 45.0), ("Bag", 1, 1250.75)]
print(f"{'Item':<12}{'Qty':>5}{'Price':>12}")
print("-" * 29)
total = 0
for item, qty, price in items:
    line_total = qty * price
    total += line_total
    print(f"{item:<12}{qty:>5}{line_total:>12,.2f}")
print("-" * 29)
print(f"{'TOTAL':<17}{total:>12,.2f}")

# Program 3: Log lines with a test ID padded with zeros
for test_id, result in [(1, "PASS"), (12, "FAIL"), (105, "PASS")]:
    print(f"[TC_{test_id:04}] {result:<5} | executed")






















































