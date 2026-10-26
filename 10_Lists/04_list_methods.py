"""
====================================================
10_Lists / 04_list_methods.py
====================================================
Topic: List Methods (overview + count, index, copy)
====================================================
Notes before you run this file:
1) A list has exactly 11 public methods:
   append, clear, copy, count, extend, index, insert, pop,
   remove, reverse, sort
2) This file gives the BIG PICTURE of all methods and explains in
   detail count(), index() and copy().
   Adding and removing (append, extend, insert, remove, pop, clear)
   -> file 05_list_adding_removing.py
   Ordering (sort, reverse)
   -> file 06_list_sorting_reversing.py
   Here we only take a short first look at them (Concept 8).
3) The biggest idea of this file: a method that CHANGES the list
   returns None. A method that GIVES information returns a value.
4) Plain programs only, no functions.
"""


# =====================================================
# Concept 1: What is a List Method?
# =====================================================
"""
Definition:
A method is a function that belongs to an object. It is called with
a dot: my_list.method(arguments).
A method belongs to ONE type: list methods work only on lists,
string methods only on strings.
"""

# Program 1: Call a method
nums = [3, 1, 2]
nums.append(4)
print(nums)                             # [3, 1, 2, 4]

# Program 2: A function and a method side by side
print(len(nums))                        # 4  (len is a FUNCTION: len(list))
print(nums.count(1))                    # 1  (count is a METHOD: list.count(x))

# Program 3: A method works only on its own type
try:
    "abc".append("d")
except AttributeError as e:
    print("Error:", e)                  # 'str' object has no attribute 'append'
try:
    [1, 2].upper()
except AttributeError as e:
    print("Error:", e)                  # 'list' object has no attribute 'upper'


# =====================================================
# Concept 2: Finding Out What Methods a List Has
# =====================================================
"""
Definition:
dir(list) lists everything a list can do. Names that start with
two underscores (like __len__) are internal, so we skip them.
help(list.count) or list.count.__doc__ explains one method.
You can use this yourself whenever you forget a method name.
"""

# Program 1: The public methods of a list
methods = []
for name in dir(list):
    if not name.startswith("_"):
        methods.append(name)
print(methods)
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
print(len(methods))                     # 11

# Program 2: Read the short description of a method
print(list.count.__doc__)               # Return number of occurrences of value.
print(list.copy.__doc__)                # Return a shallow copy of the list.

# Program 3: Check that a method exists before using it
print(hasattr([], "append"))            # True
print(hasattr([], "add"))               # False (add belongs to sets, not lists)


# =====================================================
# Concept 3: Four Kinds of List Methods
# =====================================================
"""
Definition:
1) Change the list IN PLACE and return None:
      append, extend, insert, remove, clear, sort, reverse
2) Change the list AND return the removed item:
      pop
3) Only give INFORMATION, the list stays the same:
      count, index
4) Make a NEW list:
      copy
Knowing the kind tells you if you must store the result or not.
"""

# Program 1: Information methods do not change the list
nums = [1, 2, 3, 2]
before = nums[:]
print(nums.count(2))                    # 2
print(nums.index(3))                    # 2
print(nums == before)                   # True (nothing changed)

# Program 2: Changing methods modify the list
nums = [3, 1, 2]
nums.append(4)
nums.sort()
print(nums)                             # [1, 2, 3, 4]

# Program 3: pop changes the list AND returns the removed item
stack = [1, 2, 3]
last = stack.pop()
print(last, stack)                      # 3 [1, 2]

# Program 4: copy returns a new list
original = [1, 2, 3]
duplicate = original.copy()
print(duplicate == original, duplicate is original)     # True False


# =====================================================
# Concept 4: Methods That Change the List Return None
# =====================================================
"""
Definition:
append, extend, insert, remove, clear, sort and reverse change the
list itself and return None. So these lines are classic bugs:
    nums = nums.sort()       # nums becomes None
    nums.sort().reverse()    # None has no reverse()
To get a NEW sorted list use the FUNCTION sorted(nums).
"""

# Program 1: Look at what the methods return
nums = [3, 1, 2]
print(nums.append(4))                   # None
print(nums.sort())                      # None
print(nums.reverse())                   # None
print(nums)                             # [4, 3, 2, 1]

# Program 2: The classic bug
nums = [3, 1, 2]
nums = nums.sort()
print(nums)                             # None  (the list is lost!)
try:
    print(len(nums))
except TypeError as e:
    print("Error:", e)                  # object of type 'NoneType' has no len()

# Program 3: Chaining fails on None
try:
    [3, 1, 2].sort().reverse()
except AttributeError as e:
    print("Error:", e)                  # 'NoneType' object has no attribute 'reverse'

# Program 4: Two correct ways
nums = [3, 1, 2]
nums.sort()                             # way 1: change the list, do not store anything
print(nums)                             # [1, 2, 3]
nums = [3, 1, 2]
new_list = sorted(nums)                 # way 2: a new list from the function sorted()
print(new_list, nums)                   # [1, 2, 3] [3, 1, 2]


# =====================================================
# Concept 5: count()
# =====================================================
"""
Definition:
my_list.count(value) returns how many items are EQUAL (==) to value.
It returns 0 if there is none (no error). It checks whole items,
it does not look inside items.
"""

# Program 1: Count items
data = [1, 2, 2, 3, 2]
print(data.count(2))                    # 3
print(data.count(9))                    # 0

# Program 2: Strings are compared with ==, so the case matters
names = ["ali", "Ali", "sara", "ali"]
print(names.count("ali"))               # 2
print(names.count("Ali"))               # 1

# Program 3: Counting uses ==, so 1, 1.0 and True are all "1"
print([1, 1.0, True, "1"].count(1))     # 3 ("1" is text, not equal)

# Program 4: count() counts whole items, a string method counts text inside
print(["apple pie", "apple"].count("apple"))    # 1 (only the second item equals "apple")
print("apple pie apple".count("apple"))         # 2 (the string method counts inside the text)

# Program 5: Count lists inside a list
pairs = [[1, 2], [1, 2], [3]]
print(pairs.count([1, 2]))              # 2

# Program 6: Find the most frequent item (a first idea, Counter comes in a later file)
colors = ["red", "blue", "red", "green", "red", "blue"]
best = colors[0]
for color in colors:
    if colors.count(color) > colors.count(best):
        best = color
print(best, colors.count(best))         # red 3


# =====================================================
# Concept 6: index()
# =====================================================
"""
Definition:
my_list.index(value, start, stop) returns the position of the FIRST
item equal to value. start and stop are optional and limit the search.
If the value is not found it raises ValueError (it does NOT return -1
like find() on strings).
"""

# Program 1: First position only
letters = ["a", "b", "c", "b", "a"]
print(letters.index("b"))               # 1 (not 3)
print(letters.index("a"))               # 0

# Program 2: Search from a position onwards
print(letters.index("b", 2))            # 3
print(letters.index("a", 1, 5))         # 4

# Program 3: A missing value raises ValueError
try:
    print(letters.index("z"))
except ValueError as e:
    print("Error:", e)                  # 'z' is not in list

# Program 4: Check first, then ask for the position (a safe way)
value = "z"
if value in letters:
    print("Found at", letters.index(value))
else:
    print(value, "is not in the list")

# Program 5: All positions of a value
data = [5, 7, 5, 9, 5]
positions = []
for i, item in enumerate(data):
    if item == 5:
        positions.append(i)
print(positions)                        # [0, 2, 4]

# Program 6: The same with index() and a moving start position
positions = []
start = 0
while 5 in data[start:]:
    pos = data.index(5, start)
    positions.append(pos)
    start = pos + 1
print(positions)                        # [0, 2, 4]


# =====================================================
# Concept 7: copy()
# =====================================================
"""
Definition:
my_list.copy() returns a NEW list with the same items.
It is a shallow copy, so a list inside the list is still shared.
my_list.copy(), my_list[:] and list(my_list) do the same thing.
(The full story with deep copy is in 10_list_copying_references.py.)
"""

# Program 1: Alias vs copy
a = [1, 2, 3]
alias = a
duplicate = a.copy()
a.append(4)
print(alias)                            # [1, 2, 3, 4]
print(duplicate)                        # [1, 2, 3]

# Program 2: Three ways, three separate lists
x = [1, 2, 3]
for c in (x.copy(), x[:], list(x)):
    print(c == x, c is x)               # True False (three times)

# Program 3: The inner list is shared
nested = [[1, 2], [3]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)                           # [[1, 2, 99], [3]]
print(shallow[0] is nested[0])          # True


# =====================================================
# Concept 8: A First Look at the Changing Methods
# =====================================================
"""
Definition:
A very short tour. Each of these has its own detailed file:
05 -> append, extend, insert, remove, pop, clear
06 -> sort, reverse
"""

# Program 1: Add items
nums = [1, 2]
nums.append(3)                          # one item at the end
nums.extend([4, 5])                     # many items at the end
nums.insert(0, 0)                       # one item at a given position
print(nums)                             # [0, 1, 2, 3, 4, 5]

# Program 2: Remove items
nums.remove(3)                          # remove the first item equal to 3
last = nums.pop()                       # remove and return the last item
first = nums.pop(0)                     # remove and return the item at index 0
print(nums, last, first)                # [1, 2, 4] 5 0

# Program 3: Change the order
words = ["pear", "apple", "fig"]
words.sort()
print(words)                            # ['apple', 'fig', 'pear']
words.reverse()
print(words)                            # ['pear', 'fig', 'apple']

# Program 4: Empty the list
words.clear()
print(words)                            # []


# =====================================================
# Concept 9: Methods Change the Same Object
# =====================================================
"""
Definition:
A changing method modifies the list object itself. Its id stays the
same, and every name that points to this list sees the change.
"""

# Program 1: Two names, one list
a = [1, 2]
b = a
a.append(3)
print(b)                                # [1, 2, 3]

# Program 2: The id does not change
before = id(a)
a.extend([4])
a.insert(0, 0)
print(before == id(a))                  # True

# Program 3: A method on an inner list changes the outer list too
matrix = [[1], [2]]
matrix[0].append(9)
print(matrix)                           # [[1, 9], [2]]


# =====================================================
# Concept 10: Calling Methods on the Items of a List
# =====================================================
"""
Definition:
my_list.method() works on the LIST. To use a string method on the
items, call it on one item (names[0].strip()) or on each item in a loop.
The list itself has no string methods.
"""

# Program 1: A string method on one item
names = ["  ali ", "SARA", "bilal  "]
print(repr(names[0].strip()))           # 'ali'
print(names[1].lower())                 # sara

# Program 2: A string method on every item
cleaned = []
for name in names:
    cleaned.append(name.strip().title())
print(cleaned)                          # ['Ali', 'Sara', 'Bilal']

# Program 3: The list itself has no string methods
try:
    names.strip()
except AttributeError as e:
    print("Error:", e)                  # 'list' object has no attribute 'strip'


# =====================================================
# Concept 11: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with list methods:
1) forgetting the brackets () when calling a method
2) storing the result of a method that returns None
3) index() and remove() raise ValueError if the value is missing
4) remove() removes only the FIRST match
5) count() on a list counts whole items, not text inside them
"""

# Program 1: Without brackets nothing happens
nums = [1, 2]
nums.append                             # this does NOT call the method
print(nums)                             # [1, 2]
print(type(nums.append).__name__)       # builtin_function_or_method
nums.append(3)                          # with brackets it works
print(nums)                             # [1, 2, 3]

# Program 2: The result of sort() is None
data = [3, 1, 2]
result = data.sort()
print(result, data)                     # None [1, 2, 3]

# Program 3: A missing value raises ValueError
for action in ("index", "remove"):
    try:
        if action == "index":
            [1, 2].index(5)
        else:
            [1, 2].remove(5)
    except ValueError as e:
        print(action, "->", e)          # index -> 5 is not in list / remove -> list.remove(x): x not in list

# Program 4: remove() removes only the first match
data = [1, 2, 1, 1]
data.remove(1)
print(data)                             # [2, 1, 1]

# Program 5: count() and a string's count() are different tools
print(["apple pie"].count("apple"))     # 0
print("apple pie".count("apple"))       # 1


# =====================================================
# Concept 12: List Methods in SQA Automation
# =====================================================
"""
Definition:
In test code, count() summarizes results, index() finds the first
failure, copy() protects the original test data, and the changing
methods build and consume queues of tests.
Remember: results from a page (like Playwright's all_inner_texts())
are normal lists, so the same methods work on them.
"""

# Program 1: Summarize results with count()
results = ["PASS", "FAIL", "PASS", "PASS", "FAIL"]
passed = results.count("PASS")
failed = results.count("FAIL")
print(f"Passed {passed}/{len(results)} = {passed / len(results):.1%}")      # Passed 3/5 = 60.0%
print("Failed:", failed)                # 2

# Program 2: Find the first failed test
if "FAIL" in results:
    position = results.index("FAIL")
    print(f"First failure is test number {position + 1}")       # 2

# Program 3: Find duplicated test ids
ids = ["TC_001", "TC_002", "TC_001", "TC_003", "TC_002"]
duplicates = []
for tid in ids:
    if ids.count(tid) > 1 and tid not in duplicates:
        duplicates.append(tid)
print("Duplicated ids:", duplicates)    # ['TC_001', 'TC_002']

# Program 4: Change a copy, keep the original test data safe
browsers = ["chromium", "firefox", "webkit"]
run_list = browsers.copy()
run_list.remove("webkit")
print(browsers)                         # ['chromium', 'firefox', 'webkit']
print(run_list)                         # ['chromium', 'firefox']

# Program 5: Is an item shown the correct number of times on the page?
item_texts = ["Pen", "Notebook", "Bag", "Pen"]
if item_texts.count("Pen") != 1:
    print(f"FAIL: 'Pen' is shown {item_texts.count('Pen')} times, expected 1")

# Program 6: A queue of tests, processed one by one
tests = ["test_login", "test_cart", "test_logout"]
while tests:
    current = tests.pop(0)              # take the first test out of the queue
    print("Running", current, "| left:", len(tests))