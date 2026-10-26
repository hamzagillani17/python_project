"""
====================================================
10_Lists / 03_list_slicing.py
====================================================
Topic: List Slicing
====================================================
Notes before you run this file:
1) Slicing works exactly like string slicing: my_list[start:stop:step].
   Two differences from strings:
   a) a slice of a list is a NEW LIST
   b) a list is mutable, so you can also ASSIGN to a slice (Concept 9)
2) Rule to remember: 'start' is INCLUDED, 'stop' is EXCLUDED.
3) Plain programs only, no functions.
"""

numbers = [10, 20, 30, 40, 50, 60]
#  index:   0   1   2   3   4   5
#  negative: -6  -5  -4  -3  -2  -1
# This list is used again and again below. Programs that change a list
# make their own list first, so numbers always stays the same.

# =====================================================
# Concept 1: Basic Slicing [start:stop]
# =====================================================
"""
Definition:
my_list[start:stop] returns a NEW list with the items from index
'start' up to, but NOT including, index 'stop'.
The original list is not changed.
"""

# Program 1: Items from index 1 up to index 3
print(numbers[1:4])                     # [20, 30, 40]

# Program 2: The first two items, and a slice with one item
print(numbers[0:2])                     # [10, 20]
print(numbers[2:3])                     # [30] (still a list)

# Program 3: A slice is a new list, the original stays the same
part = numbers[1:4]
part[0] = 999
print(part)                             # [999, 30, 40]
print(numbers)                          # [10, 20, 30, 40, 50, 60]
print(part is numbers)                  # False


# =====================================================
# Concept 2: Start Omitted [:stop]
# =====================================================
"""
Definition:
If 'start' is left out, Python starts at index 0.
my_list[:n] gives the FIRST n items.
"""

# Program 1: The first three items
print(numbers[:3])                      # [10, 20, 30]

# Program 2: [:3] is the same as [0:3]
print(numbers[:3] == numbers[0:3])      # True

# Program 3: The first n items for any n
n = 2
print(numbers[:n])                      # [10, 20]



# =====================================================
# Concept 3: Stop Omitted [start:]
# =====================================================
"""
Definition:
If 'stop' is left out, Python goes to the very end of the list.
my_list[n:] gives everything EXCEPT the first n items.
"""

# Program 1: Everything from index 3
print(numbers[3:])                      # [40, 50, 60]

# Program 2: Skip the first item
print(numbers[1:])                      # [20, 30, 40, 50, 60]

# Program 3: Cut a list in two parts and join them again
left = numbers[:3]
right = numbers[3:]
print(left, right)                      # [10, 20, 30] [40, 50, 60]
print(left + right == numbers)          # True


# =====================================================
# Concept 3: Stop Omitted [start:]
# =====================================================
"""
Definition:
If 'stop' is left out, Python goes to the very end of the list.
my_list[n:] gives everything EXCEPT the first n items.
"""

# Program 1: Everything from index 3
print(numbers[3:])                      # [40, 50, 60]

# Program 2: Skip the first item
print(numbers[1:])                      # [20, 30, 40, 50, 60]

# Program 3: Cut a list in two parts and join them again
left = numbers[:3]
right = numbers[3:]
print(left, right)                      # [10, 20, 30] [40, 50, 60]
print(left + right == numbers)          # True



# =====================================================
# Concept 4: Negative Slicing
# =====================================================
"""
Definition:
Negative indexes work in slices too and count from the RIGHT.
my_list[-n:]   gives the LAST n items
my_list[:-n]   gives everything EXCEPT the last n items
my_list[1:-1]  removes the first and the last item
"""

# Program 1: The last three items
print(numbers[-3:])                     # [40, 50, 60]

# Program 2: Everything except the last two
print(numbers[:-2])                     # [10, 20, 30, 40]

# Program 3: Negative start and negative stop
print(numbers[-4:-1])                   # [30, 40, 50]

# Program 4: Remove the first and the last item
print(numbers[1:-1])                    # [20, 30, 40, 50]


# =====================================================
# Concept 5: Step [start:stop:step]
# =====================================================
"""
Definition:
The third number is the 'step': how many positions to move after
each item. The default is 1. A step of 0 is an error.
"""

# Program 1: Every second item
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[::2])                     # ['a', 'c', 'e', 'g']


# Program 2: Start at index 1 to get the other half
print(letters[1::2])                    # ['b', 'd', 'f']

# Program 3: Step together with start and stop
print(letters[1:6:2])                   # ['b', 'd', 'f']
print(letters[::3])                     # ['a', 'd', 'g']

# Program 4: Items at even and odd positions
print(numbers[::2], numbers[1::2])      # [10, 30, 50] [20, 40, 60]

# Program 5: A step of 0 is not allowed
try:
    print(numbers[::0])
except ValueError as e:
    print("Error:", e)                  # slice step cannot be zero



# =====================================================
# Concept 6: Reverse a List
# =====================================================
"""
Definition:
A negative step walks from right to left. my_list[::-1] gives a
reversed COPY and leaves the original untouched.
my_list.reverse() reverses the list IN PLACE and returns None.
(reverse() has its own file, 06_list_sorting_reversing.py.)
With a negative step, 'start' must be bigger than 'stop'.
"""

# Program 1: A reversed copy
print(numbers[::-1])                    # [60, 50, 40, 30, 20, 10]
print(numbers)                          # [10, 20, 30, 40, 50, 60]

# Program 2: Negative step with start and stop
print(numbers[4:1:-1])                  # [50, 40, 30]
print(numbers[-1:-4:-1])                # [60, 50, 40] (the last three, reversed)
print(numbers[::-2])                    # [60, 40, 20]

# Program 3: Palindrome check for a list
data = [1, 2, 3, 2, 1]
print(data == data[::-1])               # True
print([1, 2, 3] == [1, 2, 3][::-1])     # False

# Program 4: reverse() works in place and returns None
mine = [1, 2, 3]
result = mine.reverse()
print(mine, result)                     # [3, 2, 1] None




# =====================================================
# Concept 7: Copying a List with a Slice
# =====================================================
"""
Definition:
my_list[:] creates a NEW list with the same items (a "shallow copy").
Without it, b = a only gives the SAME list a second name.
Shallow means: the inner objects are shared, so a list inside a
list is NOT copied (full copying: file 10_list_copying_references.py).
Other ways to copy: list(a) and a.copy().
"""

# Program 1: Two names for one list vs a real copy
a = [1, 2, 3]
alias = a                               # same list, second name
copy = a[:]                             # new list
a.append(4)
print(alias)                            # [1, 2, 3, 4] (changed too)
print(copy)                             # [1, 2, 3] (not affected)

# Program 2: Check with is
print(alias is a, copy is a)            # True False

# Program 3: Three ways to copy give equal but separate lists
x = [1, 2, 3]
copies = [x[:], list(x), x.copy()]
for c in copies:
    print(c == x, c is x)               # True False (three times)

# Program 4: A shallow copy still shares the inner list
nested = [[1, 2], [3, 4]]
shallow = nested[:]
shallow[0].append(99)
print(nested)                           # [[1, 2, 99], [3, 4]] (changed!)
print(shallow is nested, shallow[0] is nested[0])       # False True


# =====================================================
# Concept 8: A Slice Never Fails
# =====================================================
"""
Definition:
Indexing a missing position raises IndexError, but slicing is
forgiving: a range that goes outside the list is cut to fit, and a
range with nothing in it gives an empty list [].
A slice ALWAYS returns a list, even for one item.
"""

# Program 1: Out of range slices
print(numbers[2:100])                   # [30, 40, 50, 60]
print(numbers[-100:2])                  # [10, 20]
print(numbers[10:20])                   # []

# Program 2: Indexing fails, slicing does not
try:
    print(numbers[10])
except IndexError as e:
    print("Index error:", e)
print(numbers[10:11])                   # []

# Program 3: Empty results
print(numbers[3:3])                     # [] (start equals stop)
print(numbers[4:1])                     # [] (start is after stop, positive step)

# Program 4: One item as an index vs as a slice
print(numbers[1], numbers[1:2])         # 20 [20]



# =====================================================
# Concept 9: Assigning to a Slice
# =====================================================
"""
Definition:
Since a list is mutable, my_list[a:b] = other replaces that part
with the items of 'other'. The new part may have a DIFFERENT length,
so the list can grow or shrink. 'other' must be iterable.
An extended slice (with a step) needs the SAME length.
"""

# Program 1: Replace with the same number of items
nums = [1, 2, 3, 4, 5]
nums[1:3] = [20, 30]
print(nums)                             # [1, 20, 30, 4, 5]

# Program 2: Replace with fewer items (the list shrinks)
nums = [1, 2, 3, 4, 5]
nums[1:3] = [99]
print(nums)                             # [1, 99, 4, 5]

# Program 3: Replace with more items (the list grows)
nums = [1, 2, 3]
nums[0:1] = [7, 8, 9]
print(nums)                             # [7, 8, 9, 2, 3]

# Program 4: Insert without removing anything
nums = [1, 2, 3]
nums[1:1] = [10, 20]
print(nums)                             # [1, 10, 20, 2, 3]

# Program 5: A string is iterable, so it is split into characters
nums = [1, 2, 3]
nums[1:2] = "ab"
print(nums)                             # [1, 'a', 'b', 3]
try:
    nums[0:2] = 5
except TypeError as e:
    print("Error:", e)                  # can only assign an iterable

# Program 6: An extended slice needs the same size
nums = [1, 2, 3, 4, 5, 6]
nums[::2] = [0, 0, 0]
print(nums)                             # [0, 2, 0, 4, 0, 6]
try:
    nums[::2] = [0, 0]
except ValueError as e:
    print("Error:", e)                  # attempt to assign sequence of size 2 to extended slice of size 3

# Program 7: nums[:] = ... replaces everything but keeps the SAME list object
nums = [1, 2, 3]
before = id(nums)
nums[:] = [9, 9]
print(nums, before == id(nums))         # [9, 9] True



# =====================================================
# Concept 10: Deleting a Slice
# =====================================================
"""
Definition:
del my_list[a:b] removes that part of the list.
Assigning an empty list to a slice does the same.
nums[:] = [] (or del nums[:]) empties the whole list in place.
"""

# Program 1: Delete a range
nums = [10, 20, 30, 40, 50]
del nums[1:3]
print(nums)                             # [10, 40, 50]

# Program 2: Delete with a step
nums = [1, 2, 3, 4, 5, 6]
del nums[::2]
print(nums)                             # [2, 4, 6]

# Program 3: An empty list as the replacement removes the part
nums = [10, 20, 30, 40]
nums[:2] = []
print(nums)                             # [30, 40]

# Program 4: Empty the whole list in place
nums = [1, 2, 3]
alias = nums
nums[:] = []
print(nums, alias)                      # [] [] (both names see the change)

# =====================================================
# Concept 11: The slice() Object
# =====================================================
"""
Definition:
slice(start, stop, step) creates a slice object that you can store in
a variable and reuse. my_list[slice(1, 4)] is the same as
my_list[1:4]. It helps when the same positions are used again and
again, and gives them a meaningful name.
"""

# Program 1: A slice object is the same as the short form
s = slice(1, 4)
print(numbers[s])                       # [20, 30, 40]
print(numbers[s] == numbers[1:4])       # True
print(s.start, s.stop, s.step)          # 1 4 None

# Program 2: Reuse one slice on several lists
first_three = slice(0, 3)
print(["a", "b", "c", "d"][first_three])        # ['a', 'b', 'c']
print([1, 2, 3, 4, 5][first_three])             # [1, 2, 3]

# Program 3: Name positions of a fixed record layout
record = ["TC_001", "Login", "PASS", "2.3s", "chromium"]
IDENTITY = slice(0, 2)
OUTCOME = slice(2, 4)
print(record[IDENTITY], record[OUTCOME])        # ['TC_001', 'Login'] ['PASS', '2.3s']


# =====================================================
# Concept 11: The slice() Object
# =====================================================
"""
Definition:
slice(start, stop, step) creates a slice object that you can store in
a variable and reuse. my_list[slice(1, 4)] is the same as
my_list[1:4]. It helps when the same positions are used again and
again, and gives them a meaningful name.
"""

# Program 1: A slice object is the same as the short form
s = slice(1, 4)
print(numbers[s])                       # [20, 30, 40]
print(numbers[s] == numbers[1:4])       # True
print(s.start, s.stop, s.step)          # 1 4 None

# Program 2: Reuse one slice on several lists
first_three = slice(0, 3)
print(["a", "b", "c", "d"][first_three])        # ['a', 'b', 'c']
print([1, 2, 3, 4, 5][first_three])             # [1, 2, 3]

# Program 3: Name positions of a fixed record layout
record = ["TC_001", "Login", "PASS", "2.3s", "chromium"]
IDENTITY = slice(0, 2)
OUTCOME = slice(2, 4)
print(record[IDENTITY], record[OUTCOME])        # ['TC_001', 'Login'] ['PASS', '2.3s']


# =====================================================
# Concept 12: Common Slicing Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with slicing:
1) thinking 'stop' is included
2) forgetting that a slice returns a LIST, not an item
3) start after stop without a negative step gives []
4) expecting a slice to change the original list
5) thinking b = a[:] copies nested lists too
"""

# Program 1: 'stop' is excluded
print(numbers[0:3])                     # [10, 20, 30] (3 items, not 4)

# Program 2: A slice is a list, an index is an item
letters = ["a", "b", "c"]
print(letters[1], letters[1:2])         # b ['b']
print(letters[1] == letters[1:2])       # False

# Program 3: start after stop
print(numbers[4:1])                     # []
print(numbers[4:1:-1])                  # [50, 40, 30] (fixed with a negative step)

# Program 4: A slice does not change the original
data = [1, 2, 3, 4]
data[1:3]
print(data)                             # [1, 2, 3, 4] (nothing happened)
data = data[1:3]                        # you must store the new list
print(data)                             # [2, 3]

# Program 5: Reversing in two different ways
data = [1, 2, 3]
wrong = data.reverse()                  # reverse() returns None
print(wrong, data)                      # None [3, 2, 1]
data = [1, 2, 3]
right = data[::-1]
print(right, data)                      # [3, 2, 1] [1, 2, 3]



# =====================================================
# Concept 13: Slicing in SQA Automation
# =====================================================
"""
Definition:
Slicing is used in test code to look at the first or last results,
split pages of data, drop headers and footers, and share tests between
parallel workers. Because a slice never raises IndexError, it is also
a safe way to take "up to n" items from a list that may be short.
"""

# Program 1: First and last results
results = ["PASS", "PASS", "FAIL", "PASS", "FAIL"]
first_three = results[:3]
last_two = results[-2:]
print(first_three, first_three.count("FAIL"))   # ['PASS', 'PASS', 'FAIL'] 1
print(last_two, last_two.count("FAIL"))         # ['PASS', 'FAIL'] 1

# Program 2: Pagination (the last page is shorter and gives no error)
items = list(range(1, 11))
page_size = 4
for page in range(3):
    start = page * page_size
    print("Page", page + 1, items[start:start + page_size])
# Page 1 [1, 2, 3, 4]   Page 2 [5, 6, 7, 8]   Page 3 [9, 10]

# Program 3: Split a table into header and rows
table = [["Name", "Status"], ["Ali", "Active"], ["Sara", "Inactive"]]
header = table[0]
rows = table[1:]
print(header, len(rows))                # ['Name', 'Status'] 2
for row in rows:
    print(f"{row[0]:<6}{row[1]}")

# Program 4: Is the expected product among the top 3 search results?
search_results = ["Laptop X", "Laptop Y", "Phone Z", "Laptop W"]
top3 = search_results[:3]
print("Phone Z" in top3, "Laptop W" in top3)    # True False

# Program 5: Remove the header and footer lines of a log
lines = ["--- LOG START ---", "[PASS] login", "[FAIL] cart", "--- LOG END ---"]
body = lines[1:-1]
print(body)                             # ['[PASS] login', '[FAIL] cart']

# Program 6: Did the last three runs all fail? (safe even for a short list)
history = ["PASS", "FAIL", "FAIL", "FAIL"]
print(history[-3:] == ["FAIL"] * 3)     # True (consistent failure)
short_history = ["FAIL", "FAIL"]
print(short_history[-3:])               # ['FAIL', 'FAIL'] (only 2 items, no error)
print(short_history[-3:] == ["FAIL"] * 3)       # False (not enough runs yet)

# Program 7: Share tests between two parallel workers
tests = list(range(1, 9))
half = len(tests) // 2
print(tests[:half], tests[half:])       # [1, 2, 3, 4] [5, 6, 7, 8]
print(tests[0::2], tests[1::2])         # [1, 3, 5, 7] [2, 4, 6, 8] (alternate tests)



























































