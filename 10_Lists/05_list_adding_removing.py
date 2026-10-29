"""
====================================================
10_Lists / 05_list_adding_removing.py
====================================================
Topic: Adding and Removing Items
====================================================
Notes before you run this file:
1) Methods for ADDING:    append, insert, extend  (and + and +=)
   Methods for REMOVING:  remove, pop, clear      (and the del statement)
2) The most important sentence of this file:
   Every one of these changes the list IN PLACE and returns None
   (only pop() returns something: the removed item).
   So never write  nums = nums.append(4).
3) Error messages are shown as Python prints them. They can be
   worded a little differently in other Python versions.
4) Plain programs only, no functions.
"""


# =====================================================
# Concept 1: Overview, Adding vs Removing
# =====================================================
"""
Definition:
ADD:
  append(x)        one item at the END
  insert(i, x)     one item at position i
  extend(items)    MANY items at the end (from any iterable)
REMOVE:
  remove(x)        the first item EQUAL to x (by value)
  pop(i)           the item at position i, and gives it back
  del my_list[i]   the item or slice at that position (a statement)
  clear()          everything
"""

# Program 1: A tour with a running list
nums = [2, 3]
nums.append(4)                          # [2, 3, 4]
nums.insert(0, 1)                       # [1, 2, 3, 4]
nums.extend([5, 6])                     # [1, 2, 3, 4, 5, 6]
print(nums)                             # [1, 2, 3, 4, 5, 6]


# Program 2: Removing
nums.remove(3)                          # remove by value
print(nums)
last = nums.pop()                       # remove the last item, we get 6 back
print(last)
del nums[0]                             # remove by position
print(nums, last)                       # [2, 4, 5] 6



# =====================================================
# Concept 2: append()
# =====================================================
"""
Definition:
append(x) adds ONE item at the end of the list. If x is a list, it
is added as ONE inner list, it is not opened up. append() takes
exactly one argument and returns None.
"""

# Program 1: Add items one by one
fruits = ["apple"]
fruits.append("banana")
fruits.append("mango")
print(fruits)                           # ['apple', 'banana', 'mango']


# Program 2: The return value is None
result = fruits.append("kiwi")
print(result)      # None
print(fruits)      # ['apple', 'banana', 'mango', 'kiwi']


# Program 3: Build a list in a loop
squares = []
for n in range(1, 6):
    squares.append(n * n)
print(squares)        # [1, 4, 9, 16, 25]


# Program 4: Appending a list adds ONE inner list
nums = [1, 2]
nums.append([3, 4])
print(nums, len(nums))                  # [1, 2, [3, 4]] 3


# Program 5: Only one argument is allowed
try:
    nums.append(5, 6)
except TypeError as e:
    print("Error:", e)                  # list.append() takes exactly one argument (2 given)

# Program 6: Appending the SAME list twice adds the same object twice
row = [0, 0]
grid = []
grid.append(row)
grid.append(row)
row[0] = 9
print(grid)                             # [[9, 0], [9, 0]] (both rows changed!)
print(grid[0] is grid[1])               # True



# =====================================================
# Concept 3: insert()
# =====================================================
"""
Definition:
insert(index, x) puts x at position 'index' and moves the items from
there one place to the right. The INDEX comes FIRST, the value second.
An index bigger than the length adds at the end. A negative index
inserts BEFORE that item. It returns None.
"""

# Program 1: Insert at the start and in the middle
nums = [2, 3]
nums.insert(0, 1)
print(nums)                             # [1, 2, 3]
nums = [1, 3, 4]
nums.insert(1, 2)
print(nums)                             # [1, 2, 3, 4]

# Program 2: An index that is too large or too small never fails
nums = [1, 2]
nums.insert(100, 3)                     # added at the end
nums.insert(-100, 0)                    # added at the start
print(nums)                             # [0, 1, 2, 3]

# Program 3: A negative index inserts before that item
nums = [1, 2, 3]
nums.insert(-1, 99)
print(nums)                             # [1, 2, 99, 3]

# Program 4: insert(len(list), x) is the same as append(x)
a = [1, 2]
b = [1, 2]
a.insert(len(a), 3)
b.append(3)
print(a == b)                           # True

# Program 5: insert() returns None
print([1].insert(0, 0))                 # None


# =====================================================
# Concept 4: extend()
# =====================================================
"""
Definition:
extend(iterable) adds EVERY item of the iterable at the end.
It accepts a list, tuple, string, range, dict (its keys), set and so on.
A string is split into characters. A number is not iterable and fails.
It returns None.
"""

# Program 1: Extend with a list
nums = [1, 2]
nums.extend([3, 4])
print(nums)                             # [1, 2, 3, 4]

# Program 2: Extend with other iterables
items = []
items.extend((1, 2))                    # a tuple
items.extend(range(3, 5))               # a range
items.extend("ab")                      # a string, split into characters
print(items)                            # [1, 2, 3, 4, 'a', 'b']

# Program 3: A dictionary gives its keys
keys = ["x"]
keys.extend({"a": 1, "b": 2})
print(keys)                             # ['x', 'a', 'b']

# Program 4: A number is not iterable
try:
    [1].extend(5)
except TypeError as e:
    print("Error:", e)                  # 'int' object is not iterable

# Program 5: Extending with nothing changes nothing
nums = [1]
print(nums.extend([]), nums)            # None [1]


# =====================================================
# Concept 5: append() vs extend()
# =====================================================
"""
Definition:
append(x)  -> x becomes ONE new item (the length grows by 1)
extend(x)  -> EACH item of x becomes a new item (the length grows by len(x))
Mixing them up is the most common mistake in this file.
"""

# Program 1: A list as argument
a = [1, 2]
b = [1, 2]
a.append([3, 4])
b.extend([3, 4])
print(a, len(a))                        # [1, 2, [3, 4]] 3
print(b, len(b))                        # [1, 2, 3, 4] 4

# Program 2: A string as argument
a = ["x"]
b = ["x"]
a.append("abc")
b.extend("abc")
print(a)                                # ['x', 'abc']
print(b)                                # ['x', 'a', 'b', 'c']

# Program 3: A loop of append() does the same as one extend()
a = [1]
b = [1]
for item in [2, 3, 4]:
    a.append(item)
b.extend([2, 3, 4])
print(a == b)                           # True


# =====================================================
# Concept 6: + vs +=
# =====================================================
"""
Definition:
a + b   creates a NEW list (a and b stay the same).
a += b  works like a.extend(b): it changes a IN PLACE.
+ needs two lists. += accepts any iterable (like extend).
This matters when two names point to the same list.
"""

# Program 1: + creates a new list
a = [1, 2]
b = a + [3]
print(a, b, a is b)                     # [1, 2] [1, 2, 3] False

# Program 2: += changes the same list, so a second name sees it
a = [1, 2]
alias = a
a += [3]
print(alias, a is alias)                # [1, 2, 3] True

# Program 3: a = a + [3] creates a new list and breaks the link
a = [1, 2]
alias = a
a = a + [3]
print(alias, a)                         # [1, 2] [1, 2, 3]
print(a is alias)                       # False

# Program 4: += accepts any iterable, + does not
a = [1]
a += "ab"                               # like extend("ab")
a += (5,)                               # like extend((5,))
print(a)                                # [1, 'a', 'b', 5]
try:
    [1] + "ab"
except TypeError as e:
    print("Error:", e)                  # can only concatenate list (not "str") to list


# =====================================================
# Concept 7: remove()
# =====================================================
"""
Definition:
remove(x) deletes the FIRST item that is equal (==) to x.
It works by VALUE, not by position. If x is not in the list it
raises ValueError. It returns None and removes only one item.
"""

# Program 1: Remove by value
fruits = ["apple", "banana", "mango"]
fruits.remove("banana")
print(fruits)                           # ['apple', 'mango']

# Program 2: Only the first match is removed
data = [1, 2, 1, 1]
data.remove(1)
print(data)                             # [2, 1, 1]

# Program 3: A missing value raises ValueError
try:
    fruits.remove("pear")
except ValueError as e:
    print("Error:", e)                  # list.remove(x): x not in list

# Program 4: Check first, then remove
if "pear" in fruits:
    fruits.remove("pear")
else:
    print("pear is not in the list, nothing to remove")

# Program 5: remove() takes a VALUE, not an index
nums = [10, 20, 30]
nums.remove(20)
print(nums)                             # [10, 30]
try:
    nums.remove(1)                      # 1 is not a value in the list (index 1 is not used)
except ValueError as e:
    print("Error:", e)

# Program 6: Equal values are removed, even of another type
mixed = [1, 1.0, 2]
mixed.remove(1.0)                       # 1 == 1.0, so the first one (the int 1) goes
print(mixed)                            # [1.0, 2]


# =====================================================
# Concept 8: pop()
# =====================================================
"""
Definition:
pop() removes the LAST item and returns it.
pop(i) removes the item at position i and returns it.
Negative positions work. pop() on an empty list, or with a bad
index, raises IndexError.
"""

# Program 1: Remove the last item and keep it
stack = [1, 2, 3]
last = stack.pop()
print(last, stack)                      # 3 [1, 2]

# Program 2: Remove by position
letters = ["a", "b", "c", "d"]
second = letters.pop(1)
print(second, letters)                  # b ['a', 'c', 'd']

# Program 3: A negative position
print(letters.pop(-2), letters)         # c ['a', 'd']

# Program 4: Errors
try:
    [].pop()
except IndexError as e:
    print("Error:", e)                  # pop from empty list
try:
    [1, 2].pop(5)
except IndexError as e:
    print("Error:", e)                  # pop index out of range

# Program 5: Use the returned item
tasks = ["write", "test", "deploy"]
current = tasks.pop(0)
print("Doing:", current, "| left:", tasks)     # Doing: write | left: ['test', 'deploy']


# =====================================================
# Concept 9: del Statement
# =====================================================
"""
Definition:
del is a STATEMENT, not a method, so there are no brackets after it.
del my_list[i]      removes one item
del my_list[a:b]    removes a slice
del my_list[::2]    removes every second item
del my_list         deletes the NAME (the list itself is freed
                    when no other name points to it)
"""

# Program 1: Delete one item
nums = [10, 20, 30, 40]
del nums[1]
print(nums)                             # [10, 30, 40]

# Program 2: Delete a slice and a step slice
nums = [1, 2, 3, 4, 5, 6]
del nums[1:3]
print(nums)                             # [1, 4, 5, 6]
del nums[::2]
print(nums)                             # [4, 6]

# Program 3: Delete the whole name
temp = [1, 2, 3]
del temp
try:
    print(temp)
except NameError as e:
    print("Error:", e)                  # name 'temp' is not defined

# Program 4: Delete a position that does not exist
try:
    del [1, 2][5]
except IndexError as e:
    print("Error:", e)                  # list assignment index out of range


# =====================================================
# Concept 10: remove() vs pop() vs del
# =====================================================
"""
Definition:
remove(x)  you know the VALUE            -> removes the first match, gives nothing back
pop(i)     you know the POSITION         -> removes it AND gives the item back
del l[i]   you know the position or a range -> no item back, works on slices
"""

# Program 1: The same result in three ways
a = [10, 20, 30, 40]
b = [10, 20, 30, 40]
c = [10, 20, 30, 40]
a.remove(30)                            # by value
item = b.pop(2)                         # by position, we get 30 back
del c[2]                                # by position
print(a, b, c)                          # [10, 20, 40] [10, 20, 40] [10, 20, 40]
print(item)                             # 30

# Program 2: Only pop() gives the item back
print([1, 2, 3].remove(2))              # None
print([1, 2, 3].pop(1))                 # 2

# Program 3: Only del can remove a slice in one step
nums = [1, 2, 3, 4, 5]
del nums[1:4]
print(nums)                             # [1, 5]


# =====================================================
# Concept 11: clear() vs = []
# =====================================================
"""
Definition:
clear() empties the SAME list object, so every name pointing to it
sees an empty list.
my_list = [] makes a NEW empty list and moves ONLY that name. Other
names still point to the old list with its items.
"""

# Program 1: clear() empties the list
nums = [1, 2, 3]
nums.clear()
print(nums, len(nums))                  # [] 0

# Program 2: clear() and an alias
a = [1, 2, 3]
alias = a
a.clear()
print(alias)                            # [] (same object, also empty)

# Program 3: = [] and an alias
a = [1, 2, 3]
alias = a
a = []
print(a, alias)                         # [] [1, 2, 3] (alias keeps the old list)

# Program 4: clear() keeps the same object, return value is None
a = [1, 2]
before = id(a)
print(a.clear())                        # None
print(before == id(a))                  # True


# =====================================================
# Concept 12: Removing Items While Looping (a Trap)
# =====================================================
"""
Definition:
If you remove items from a list WHILE a for loop goes through it, the
items move one place to the left and the loop skips the next one.
Safe ways: loop over a COPY, build a NEW list, walk from the END,
or use a while loop.
"""

# Program 1: The trap (a 2 is left in the list)
data = [1, 2, 2, 3, 2, 4]
for x in data:
    if x == 2:
        data.remove(x)
print(data)                             # [1, 3, 2, 4]  (wrong)

# Program 2: Safe way 1, loop over a copy
data = [1, 2, 2, 3, 2, 4]
for x in data[:]:
    if x == 2:
        data.remove(x)
print(data)                             # [1, 3, 4]

# Program 3: Safe way 2, build a new list with the items you keep
data = [1, 2, 2, 3, 2, 4]
kept = []
for x in data:
    if x != 2:
        kept.append(x)
print(kept)                             # [1, 3, 4]

# Program 4: Safe way 3, walk from the end by index
data = [1, 2, 2, 3, 2, 4]
for i in range(len(data) - 1, -1, -1):
    if data[i] == 2:
        del data[i]
print(data)                             # [1, 3, 4]

# Program 5: Safe way 4, a while loop
data = [1, 2, 2, 3, 2, 4]
while 2 in data:
    data.remove(2)
print(data)                             # [1, 3, 4]

# Program 6: Same list object kept, filled again with the kept items
data = [1, 2, 3, 4, 5, 6]
alias = data
data[:] = [x for x in data if x % 2 != 0]       # comprehensions: file 08
print(data, alias)                      # [1, 3, 5] [1, 3, 5]


# =====================================================
# Concept 13: Removing Duplicates and Unwanted Items
# =====================================================
"""
Definition:
Common clean-up jobs:
1) remove duplicates but KEEP the order
2) remove ALL copies of a value
3) remove empty strings
list(set(x)) also removes duplicates but loses the order.
list(dict.fromkeys(x)) removes duplicates and keeps the order.
"""

# Program 1: Remove duplicates with a loop (order kept)
names = ["ali", "sara", "ali", "bilal", "sara"]
unique = []
for name in names:
    if name not in unique:
        unique.append(name)
print(unique)                           # ['ali', 'sara', 'bilal']

# Program 2: The short way that also keeps the order
print(list(dict.fromkeys(names)))       # ['ali', 'sara', 'bilal']
print(len(set(names)))                  # 3 (a set has no order, so we only use it to count)

# Program 3: Remove all copies of a value
data = [5, 1, 5, 2, 5]
while 5 in data:
    data.remove(5)
print(data)                             # [1, 2]

# Program 4: Remove empty strings after a split
parts = "a,,b,,c".split(",")
print(parts)                            # ['a', '', 'b', '', 'c']
parts = [p for p in parts if p]
print(parts)                            # ['a', 'b', 'c']


# =====================================================
# Concept 14: Stack and Queue with a List
# =====================================================
"""
Definition:
Stack (LIFO, last in first out): append() to add, pop() to take.
Queue (FIFO, first in first out): append() to add, pop(0) to take.
pop(0) and insert(0, x) shift every other item, so they are slow for
very big lists. For big queues collections.deque is better (later file).
"""

# Program 1: A stack
stack = []
stack.append("page 1")
stack.append("page 2")
stack.append("page 3")
print("Top:", stack[-1])                # page 3 (look at it without removing)
print(stack.pop())                      # page 3
print(stack.pop())                      # page 2
print(stack)                            # ['page 1']

# Program 2: A queue
queue = ["test_a", "test_b", "test_c"]
queue.append("test_d")
print(queue.pop(0))                     # test_a (the first one in is the first one out)
print(queue)                            # ['test_b', 'test_c', 'test_d']

# Program 3: Work until a list is empty
tasks = ["one", "two", "three"]
while tasks:
    print("Processing", tasks.pop(0), "| left:", len(tasks))

# Program 4: An undo history
history = []
for action in ["type A", "type B", "type C"]:
    history.append(action)
undo = history.pop()
print("Undo:", undo, "| history:", history)    # Undo: type C | history: ['type A', 'type B']


# =====================================================
# Concept 15: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often in this file:
1) nums = nums.append(4)         -> nums becomes None
2) append() instead of extend()  -> a list inside the list
3) insert(value, index)          -> the arguments are swapped
4) remove() of a missing value   -> ValueError
5) list + something that is not a list -> TypeError
6) pop() on an empty list        -> IndexError
"""

# Program 1: Storing the result of append()
nums = [1, 2, 3]
nums = nums.append(4)
print(nums)                             # None (the list is lost)

# Program 2: append() instead of extend()
nums = [1, 2]
nums.append([3, 4])
print(nums)                             # [1, 2, [3, 4]]
nums = [1, 2]
nums.extend([3, 4])
print(nums)                             # [1, 2, 3, 4]

# Program 3: insert() needs the INDEX first
nums = [1, 2, 3]
nums.insert(99, 0)                      # "put 99 at position 0" was the idea, but the meaning is
print(nums)                             # [1, 2, 3, 0]  (value 0 added at the end, index 99 is too big)
try:
    ["a"].insert("b", 0)
except TypeError as e:
    print("Error:", e)                  # 'str' object cannot be interpreted as an integer

# Program 4: Removing something that is not there
try:
    [1, 2].remove(9)
except ValueError as e:
    print("Error:", e)

# Program 5: + needs a list on both sides
try:
    [1, 2] + (3,)
except TypeError as e:
    print("Error:", e)                  # can only concatenate list (not "tuple") to list
print([1, 2] + [3])                     # [1, 2, 3]
print([1, 2] + list((3,)))              # [1, 2, 3]

# Program 6: Using pop() safely
tasks = []
if tasks:
    print(tasks.pop())
else:
    print("Nothing to pop")


# =====================================================
# Concept 16: Adding and Removing in SQA Automation
# =====================================================
"""
Definition:
Test code builds lists while it runs (failures, created data,
screenshots), prepares a run list from the full list, and cleans up
what it created. Cleaning up in REVERSE order (with pop()) is the
usual way to delete data that depends on other data.
"""

# Program 1: Collect the failed tests while running
results = [("login", "PASS"), ("cart", "FAIL"), ("search", "PASS"), ("payment", "FAIL")]
failed = []
for name, status in results:
    if status == "FAIL":
        failed.append(name)
print("Failed:", failed)                # ['cart', 'payment']

# Program 2: Combine the results of two runs with extend()
run1 = ["PASS", "FAIL"]
run2 = ["PASS", "PASS", "FAIL"]
all_results = []
all_results.extend(run1)
all_results.extend(run2)
print(all_results, all_results.count("FAIL"))   # ['PASS', 'FAIL', 'PASS', 'PASS', 'FAIL'] 2

# Program 3: Skip some tests, but keep the full list safe
all_tests = ["login", "cart", "checkout", "payment"]
skipped = ["cart"]
run_list = all_tests.copy()
for test in skipped:
    run_list.remove(test)
print(run_list)                         # ['login', 'checkout', 'payment']
print(all_tests)                        # ['login', 'cart', 'checkout', 'payment'] (unchanged)

# Program 4: Add a setup step at the start and a teardown step at the end
steps = ["open page", "login", "checkout"]
steps.insert(0, "start browser")
steps.append("close browser")
print(steps)

# Program 5: Delete created test data in reverse order
created_users = []
for n in range(1, 4):
    created_users.append(f"user_{n}")
while created_users:
    print("Deleting", created_users.pop())      # user_3, user_2, user_1

# Program 6: Unique test ids with the order kept
ids = ["TC_001", "TC_002", "TC_001", "TC_003", "TC_002"]
print(list(dict.fromkeys(ids)))         # ['TC_001', 'TC_002', 'TC_003']

# Program 7: Remove blank lines from a log
lines = ["[PASS] login", "", "   ", "[FAIL] cart"]
kept = []
for line in lines:
    if line.strip():
        kept.append(line)
print(kept)                             # ['[PASS] login', '[FAIL] cart']

# Program 8: A retry queue, a failed test is added to the end once
queue = ["test_a", "test_b", "test_c"]
fails_once = {"test_b"}
retried = []
while queue:
    test = queue.pop(0)
    if test in fails_once:
        fails_once.discard(test)
        print(test, "FAILED, will retry")
        queue.append(test)
        retried.append(test)
    else:
        print(test, "PASSED")
print("Retried:", retried)              # ['test_b']







































































































































