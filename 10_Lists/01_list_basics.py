"""
====================================================
10_Lists / 01_list_basics.py
====================================================
Topic: List Basics
====================================================
Notes before you run this file:
1) Everything here uses plain programs, no functions.
2) A list is written with square brackets [ ].
   A tuple uses round brackets ( ). A string uses quotes " ".
   Keep these three apart, beginners mix them up a lot.
3) Indexing, slicing, adding and removing items have their own files
   (02, 03, 05). Here we only build the base.
"""

# =====================================================
# Concept 1: What is a List?
# =====================================================
"""
Definition:
A list is an ORDERED and CHANGEABLE (mutable) collection of items,
written inside square brackets and separated by commas.
Ordered   -> every item has a fixed position (index 0, 1, 2 ...).
Changeable -> you can add, remove and replace items after creating it.
"""


# Program 1: Create a list of strings and look at its type
fruits = ["apple", "banana", "mango"]    # ['apple', 'banana', 'mango']
print(fruits)
print(type(fruits))          # <class 'list'>

# Program 2: Create a list of numbers
number = [10,20,30,40]
print(number)    # [10, 20, 30, 40]

# Program 3: Confirm that an object is a list
print(isinstance(number, list))        # True
print(isinstance("abc", list))          # False

# =====================================================
# Concept 2: Why Do We Need Lists?
# =====================================================
"""
Definition:
Without a list you need one variable for every value. A list keeps
many values under ONE name, so you can loop over them, count them,
sort them and pass them around together.
"""
# Program 1: Without a list (many variables, hard to handle)
student1 = "Ali"
student2 = "Sara"
student3 = "Bilal"
print(student1, student2, student3)

# Program 2: With a list (one variable, easy to handle)
students = ["Ali", "Sara", "Bilal"]
print(students)

# Program 3: One loop works for 3 items or 3000 items
for student in students:
    print("Hello,", student)


# =====================================================
# Concept 3: Creating a List with Square Brackets
# =====================================================
"""
Definition:
The most common way to create a list is a list literal:
square brackets with items separated by commas.
A comma after the last item is allowed and is ignored.
A list can be written over several lines.
"""

# Program 1: A list of strings and a list of floats
cities = ["Lahore", "Karachi", "Islamabad"]
prices = [9.99, 19.5, 4.25]
print(cities)                           # ['Lahore', 'Karachi', 'Islamabad']
print(prices)                           # [9.99, 19.5, 4.25]

# Program 2: A trailing comma changes nothing
numbers = [1, 2, 3,]
print(numbers)                          # [1, 2, 3]
print(numbers == [1, 2, 3])             # True

# Program 3: A long list written over several lines
browsers = [
    "chromium",
    "firefox",
    "webkit",
]
print(browsers)                         # ['chromium', 'firefox', 'webkit']


# =====================================================
# Concept 4: Creating a List with list()
# =====================================================
"""
Definition:
list(iterable) builds a new list from anything you can loop over:
a string, a range, a tuple, a dictionary (its keys) and so on.
list() with no argument gives an empty list.
The argument must be iterable, so list(5) is an error.
"""


# Program 1: From a string (every character becomes an item)
print(list("hello"))                    # ['h', 'e', 'l', 'l', 'o']

# Program 2: From a range and from a tuple
print(list(range(5)))                   # [0, 1, 2, 3, 4]
print(list((1, 2, 3)))                  # [1, 2, 3]


















