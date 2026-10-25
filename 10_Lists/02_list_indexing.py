"""
====================================================
10_Lists / 02_list_indexing.py
====================================================
Topic: List Indexing (accessing items by position)
====================================================
Notes before you run this file:
1) Indexing works exactly like string indexing, so most of this will
   feel familiar. The big difference: a list is MUTABLE, so you can
   also CHANGE an item through its index (Concept 6).
2) Slicing (my_list[1:3]) is in the next file, 03_list_slicing.py.
3) Every program uses plain code, no functions.
"""


# =====================================================
# Concept 1: What is Indexing?
# =====================================================
"""
Definition:
Every item of a list has a position number called an INDEX.
my_list[index] gives you the item at that position.
Counting starts at 0, not at 1.
"""


# Program 1: Get one item by its index
letters = ["a", "b", "c", "d", "e"]
print(letters[0])                       # a
print(letters[2])                       # c


# Program 2: Every index with its item
#   index:    0    1    2    3    4
#   item:   "a"  "b"  "c"  "d"  "e"
for i in range(len(letters)):
    print("Index", i, "->", letters[i])


# Program 3: The result of indexing is the item itself, not a list
fruits = ["apple", "banana", "mango"]
print(fruits[1], type(fruits[1]))       # banana <class 'str'>



# =====================================================
# Concept 2: Positive Indexing
# =====================================================
"""
Definition:
Positive indexes count from the LEFT, starting at 0.
For a list of length n the valid positive indexes are 0 to n - 1.
"""

# Program 1: Items from the left
colors = ["red", "green", "blue", "yellow"]
print(colors[0], colors[1], colors[2], colors[3])       # red green blue yellow
print(colors)

# Program 2: The last valid positive index is len - 1
print(len(colors))                      # 4
print(colors[len(colors)-1])

# Program 3: Items of different types
record = ["Ali", 22, True, 3.5]
print(record[0], record[1], record[2], record[3])       # Ali 22 True 3.5


# =====================================================
# Concept 3: Negative Indexing
# =====================================================
"""
Definition:
Negative indexes count from the RIGHT, starting at -1 (the last item).
Rule: a negative index n means the same as len(list) + n.
"""

# Program 1: Items from the right
letters = ["a", "b", "c", "d", "e"]
print(letters[-1], letters[-2], letters[-5])            # e d a

# Program 2: Each negative index has a positive twin
#   positive:   0    1    2    3    4
#   negative:  -5   -4   -3   -2   -1
print(letters[1] == letters[-4])        # True  (-4 + 5 = 1)
print(letters[-4] == letters[len(letters) - 4])         # True

# Program 3: The valid negative range is -len to -1
try:
    print(letters[-6])
except IndexError as e:
    print("Error:", e)                  # list index out of range

# =====================================================
# Concept 4: First and Last Item
# =====================================================
"""
Definition:
The first item is my_list[0] and the last item is my_list[-1].
[-1] is better than [len(my_list) - 1] because it is shorter and
needs no calculation. Both fail on an EMPTY list.
"""

# Program 1: First and last
scores = [55, 72, 90, 64]
print("First:", scores[0])              # 55
print("Last:", scores[-1])              # 64

# Program 2: Works the same for lists of any size
print(["only"][0], ["only"][-1])        # only only
print([1, 2][0], [1, 2][-1])            # 1 2

# Program 3: An empty list has no first or last item
items = []
if items:
    print(items[0], items[-1])
else:
    print("The list is empty, nothing to read")
try:
    print(items[0])
except IndexError as e:
    print("Error:", e)                  # list index out of range
# =====================================================
# Concept 5: Index Out of Range
# =====================================================
"""
Definition:
Reading an index that does not exist raises an IndexError.
The most common cause is the "off by one" mistake: using len(list)
as an index. The last valid index is len(list) - 1.
"""

# Program 1: An index that is too large
numbers = [10, 20, 30]
try:
    print(numbers[3])
except IndexError as e:
    print("Error:", e)                  # list index out of range

# Program 2: The off by one mistake
try:
    print(numbers[len(numbers)])
except IndexError as e:
    print("Error:", e)
print(numbers[len(numbers) - 1])        # 30 (correct)

# Program 3: Assignment gives a slightly different message
try:
    numbers[10] = 99
except IndexError as e:
    print("Error:", e)                  # list assignment index out of range

# Program 4: Check the index first (a safe way, no error)
index = 7
if -len(numbers) <= index < len(numbers):
    print(numbers[index])
else:
    print("Index", index, "is not valid for a list of length", len(numbers))


# =====================================================
# Concept 6: Changing an Item by Index
# =====================================================
"""
Definition:
Because a list is mutable, my_list[index] = new_value replaces the
item at that position. The list changes in place (same object).
The index must already exist, you cannot create a new item this way.
"""

# Program 1: Replace one item
fruits = ["apple", "banana", "mango"]
fruits[1] = "orange"
print(fruits)                           # ['apple', 'orange', 'mango']

# Program 2: Replace using a negative index
fruits[-1] = "grapes"
print(fruits)                           # ['apple', 'orange', 'grapes']

# Program 3: Change a value using its old value
numbers = [1, 2, 3]
numbers[0] = numbers[0] + 100
numbers[2] += 5
print(numbers)                          # [101, 2, 8]

# Program 4: The same list object is changed
before = id(fruits)
fruits[0] = "kiwi"
print(before == id(fruits))             # True

# Program 5: A string cannot be changed this way
text = "abc"
try:
    text[0] = "x"
except TypeError as e:
    print("Error:", e)                  # 'str' object does not support item assignment


# =====================================================
# Concept 7: Using Variables and Calculations as Index
# =====================================================
"""
Definition:
The index can be any expression that gives an integer: a variable,
a calculation, len(), or a value typed by the user.
A float (even 1.0) or a string is NOT allowed as an index.
"""

# Program 1: A variable as index
names = ["Ali", "Sara", "Bilal", "Hina"]
position = 2
print(names[position])                  # Bilal

# Program 2: A calculation as index
print(names[position - 1])              # Sara
print(names[len(names) // 2])           # Bilal (the item in the middle, 4 // 2 = 2)

# Program 3: An index typed by the user (input always gives text, so convert it)
user_index = int(input("Enter an index from 0 to 3: "))
if 0 <= user_index < len(names):
    print("Item:", names[user_index])
else:
    print("That index does not exist")

# Program 4: A float or a string is not a valid index
for bad_index in (1.0, "1"):
    try:
        print(names[bad_index])
    except TypeError as e:
        print("Error:", e)               # list indices must be integers or slices, not ...


# =====================================================
# Concept 8: The Middle Item
# =====================================================
"""
Definition:
The middle index is len(my_list) // 2.
For a list with an ODD length there is exactly one middle item.
For an EVEN length there are two, and // 2 gives the second one.
"""

# Program 1: Odd length
odd = [10, 20, 30, 40, 50]
print(odd[len(odd) // 2])               # 30

# Program 2: Even length (two middle items)
even = [1, 2, 3, 4]
middle_index = len(even) // 2
print(even[middle_index - 1], even[middle_index])       # 2 3

# Program 3: First, middle and last together
print(odd[0], odd[len(odd) // 2], odd[-1])              # 10 30 50


# =====================================================
# Concept 9: Swapping Items by Index
# =====================================================
"""
Definition:
Python can swap two items in ONE line, without a temporary variable:
my_list[i], my_list[j] = my_list[j], my_list[i]
(This is the same trick used in bubble sort.)
"""

# Program 1: Swap the first and the last item
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)                          # [5, 2, 3, 4, 1]

# Program 2: Swap two items at any positions
letters = ["a", "b", "c", "d"]
i, j = 1, 2
letters[i], letters[j] = letters[j], letters[i]
print(letters)                          # ['a', 'c', 'b', 'd']

# Program 3: The classic way with a temporary variable (same result)
colors = ["red", "green", "blue"]
temp = colors[0]
colors[0] = colors[2]
colors[2] = temp
print(colors)                           # ['blue', 'green', 'red']


# =====================================================
# Concept 10: Indexing and Loops
# =====================================================
"""
Definition:
Three ways to go through a list:
for item in my_list:                  gives the ITEM only
for i in range(len(my_list)):         gives the INDEX, the item is my_list[i]
for i, item in enumerate(my_list):    gives BOTH (the cleanest way)
To CHANGE items you need the index. Changing the loop variable does
not change the list.
"""

# Program 1: Items only, and index with item
names = ["Ali", "Sara", "Bilal"]
for name in names:
    print(name)
for i in range(len(names)):
    print(i, names[i])

# Program 2: enumerate() gives both
for i, name in enumerate(names):
    print(f"Index {i}: {name}")
for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")          # numbering that starts at 1

# Program 3: Changing the loop variable does NOT change the list
numbers = [1, 2, 3]
for n in numbers:
    n = n * 2
print(numbers)                          # [1, 2, 3] (unchanged)

# Program 4: Changing through the index DOES change the list
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)                          # [2, 4, 6]

# Program 5: Compare each item with the next one using two indexes
values = [3, 5, 4, 8]
for i in range(len(values) - 1):
    print(values[i], "->", values[i + 1], "increase" if values[i + 1] > values[i] else "decrease")




# =====================================================
# Concept 11: Indexing Inside an Item (Nested Preview)
# =====================================================
"""
Definition:
If an item is itself a list or a string, you can index it again by
adding a second pair of brackets: my_list[i][j].
Read it from left to right: first the outer item, then the inner one.
(Nested lists have their own file, 09_nested_lists.py.)
"""

# Program 1: A list inside a list
matrix = [[1, 2, 3], [4, 5, 6]]
print(matrix[0])                        # [1, 2, 3]
print(matrix[1][0])                     # 4
print(matrix[0][-1])                    # 3

# Program 2: A string inside a list
names = ["ali", "sara"]
print(names[0][0], names[1][-1])        # a a
print(names[1][1:3])                    # ar (slicing a string item)

# Program 3: Modify an inner item
matrix[1][2] = 60
print(matrix)                           # [[1, 2, 3], [4, 5, 60]]


# =====================================================
# Concept 12: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with list indexing:
1) thinking the first item has index 1
2) using len(my_list) as the last index
3) reading from an empty list
4) confusing the index with the item value
5) True and False work as index 1 and 0, which can hide a bug
"""

# Program 1: The first item is index 0, not 1
items = ["first", "second", "third"]
print(items[0])                         # first
print(items[1])                         # second (not the first!)

# Program 2: Index and value are different things
numbers = [10, 20, 30]
print(numbers[1])                       # 20 (the item at index 1)
print(numbers[20] if len(numbers) > 20 else "There is no index 20")

# Program 3: A boolean works as an index
print(items[True], items[False])        # second first

# Program 4: Asking for the last item of a list that may be empty
results = []
last = results[-1] if results else None
print(last)                             # None (no crash)

# Program 5: A wrong guess about the length
data = [1, 2, 3]
guess_last_index = 3
if guess_last_index >= len(data):
    print("Index", guess_last_index, "is out of range, the last index is", len(data) - 1)


# =====================================================
# Concept 13: Indexing in SQA Automation
# =====================================================
"""
Definition:
Test code reads items by position all the time: the first search
result, the last table row, the header cell, the id at the end of a
URL, the status word in a log line. Always protect the access when
the list can be empty, because a missing element is also a test result.
"""

# Program 1: First and last test result
test_results = ["PASS", "FAIL", "PASS", "PASS"]
print("First test:", test_results[0])                  # PASS
print("Last test:", test_results[-1])                   # PASS
print("Second failed?", test_results[1] == "FAIL")      # True

# Program 2: Texts from a page (Playwright's all_inner_texts() returns a list like this)
item_texts = ["Pen", "Notebook", "Bag"]
print("First item on the page:", item_texts[0])         # Pen
print("Number of items:", len(item_texts))              # 3

# Program 3: The id at the end of a URL
url = "https://example.com/shop/item/42"
parts = url.split("/")
print(parts)                            # ['https:', '', 'example.com', 'shop', 'item', '42']
print("Item id:", parts[-1])            # 42
print("Section:", parts[-2])            # item

# Program 4: Pick fields out of a log line by position
line = "2026-10-17 10:30:15 [ERROR] Login failed"
parts = line.split()
print("Date:", parts[0], "| Time:", parts[1], "| Level:", parts[2])
print("Last word:", parts[-1])          # failed

# Program 5: The header row of a table
header = ["Name", "Email", "Status"]
row = ["Ali", "ali@example.com", "Active"]
print(header[0] == "Name", header[-1] == "Status")      # True True
print(f"{header[2]} of {row[0]} is {row[2]}")           # Status of Ali is Active

# Program 6: A search returned no results, the safe way and the crash
search_results = []
if not search_results:
    print("FAIL: the search returned no results")
try:
    print(search_results[0])
except IndexError:
    print("This is the IndexError a test would hit without the check above")




























































































