"""
====================================================
10_Lists / 07_list_looping.py
====================================================
Topic: Looping Over Lists
====================================================
Notes before you run this file:
1) Ways to go through a list:
   for item in my_list                 -> the ITEM only
   for i in range(len(my_list))        -> the INDEX (item = my_list[i])
   for i, item in enumerate(my_list)   -> INDEX and ITEM together
   while i < len(my_list)              -> you control the index yourself
   zip(list_a, list_b)                 -> several lists at the same time
2) The loop variable is only a NAME that points to the current item.
   Changing the name does not change the list (Concept 11).
3) Never add or remove items of the list you are looping over (Concept 12).
4) zip(strict=True) needs Python 3.10 or newer.
5) Plain programs only, no functions.
"""

import time
from itertools import zip_longest


# =====================================================
# Concept 1: Overview of the Ways to Loop
# =====================================================
"""
Definition:
Python gives you several loops for the same list. Pick the simplest one
that gives you what you need:
only the items            -> for item in my_list
the position as well      -> enumerate()
you must CHANGE items     -> index (range(len()) or enumerate())
stop depends on a result  -> while
two lists together        -> zip()
"""

fruits = ["apple", "banana", "mango"]

# Program 1: for item in list
for fruit in fruits:
    print(fruit)

# Program 2: range(len())
for i in range(len(fruits)):
    print(i, fruits[i])

# Program 3: enumerate()
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Program 4: while with an index
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1


# =====================================================
# Concept 2: for item in my_list
# =====================================================
"""
Definition:
for item in my_list: runs the body once for every item, from the
first to the last. 'item' is a name that points to the current item.
This is the simplest and the most readable loop.
"""

# Program 1: Use every item
names = ["ali", "sara", "bilal"]
for name in names:
    print("Hello,", name.title())

# Program 2: Add all numbers
numbers = [10, 20, 30]
total = 0
for n in numbers:
    total += n
print(total)                            # 60

# Program 3: The loop works for any length, even an empty list
for item in []:
    print("this line never runs")
print("the empty list was skipped without an error")

# Program 4: A list of lists, every item is itself a list
pairs = [[1, 2], [3, 4]]
for pair in pairs:
    print(pair, "has", len(pair), "items")


# =====================================================
# Concept 3: for i in range(len(my_list))
# =====================================================
"""
Definition:
range(len(my_list)) gives the numbers 0 to len - 1, which are all the
valid indexes. Use it when you need the position, when you must
CHANGE items in place, or when you look at neighbours.
"""

# Program 1: Index and item
letters = ["a", "b", "c"]
for i in range(len(letters)):
    print(i, letters[i])

# Program 2: Change every item in place
nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 10
print(nums)                             # [10, 20, 30]

# Program 3: Look at the next item (stop one early, otherwise IndexError)
values = [3, 5, 4, 8]
for i in range(len(values) - 1):
    print(values[i], "->", values[i + 1])

# Program 4: start and step of range()
letters = ["a", "b", "c", "d", "e"]
for i in range(0, len(letters), 2):
    print("every second:", i, letters[i])         # 0 a, 2 c, 4 e
for i in range(1, len(letters)):
    print("without the first:", letters[i])       # b c d e

# Program 5: An empty list gives range(0), so nothing happens
for i in range(len([])):
    print("never runs")
print(list(range(0)))                   # []


# =====================================================
# Concept 4: enumerate()
# =====================================================
"""
Definition:
enumerate(my_list, start=0) gives (index, item) pairs, so you get
both in one loop without range(len()). The start value only changes
the numbers you get, not the items.
"""

# Program 1: Default numbering from 0
for i, color in enumerate(["red", "green", "blue"]):
    print(i, color)

# Program 2: Numbering that starts at 1
for number, color in enumerate(["red", "green", "blue"], start=1):
    print(f"{number}. {color}")

# Program 3: All positions of a value
data = [5, 7, 5, 9, 5]
positions = []
for i, value in enumerate(data):
    if value == 5:
        positions.append(i)
print(positions)                        # [0, 2, 4]

# Program 4: enumerate() gives tuples
print(list(enumerate(["a", "b"])))      # [(0, 'a'), (1, 'b')]

# Program 5: Change items safely with enumerate()
nums = [1, 2, 3]
for i, n in enumerate(nums):
    nums[i] = n * 2
print(nums)                             # [2, 4, 6]


# =====================================================
# Concept 5: while Loops over a List
# =====================================================
"""
Definition:
A while loop repeats as long as its condition is True. With lists you
use it when you control the position yourself, when the list changes
during the loop, or when you work until the list is empty.
Always change something inside the loop that makes the condition
False one day, otherwise it never stops.
"""

# Program 1: Walk with an index
items = ["a", "b", "c"]
i = 0
while i < len(items):
    print(items[i])
    i += 1

# Program 2: Work until the list is empty
tasks = ["one", "two", "three"]
while tasks:
    print("Doing", tasks.pop(0), "| left:", len(tasks))

# Program 3: Stop at the first negative number
numbers = [4, 8, -2, 9]
i = 0
while i < len(numbers) and numbers[i] >= 0:
    i += 1
if i < len(numbers):
    print("First negative number is", numbers[i], "at index", i)     # -2 at index 2
else:
    print("No negative number")

# Program 4: Walk backwards
i = len(items) - 1
while i >= 0:
    print(items[i])                     # c b a
    i -= 1

# Program 5: Stop at a marker, and never run past the end of the list
tokens = ["a", "b", "STOP", "c"]
i = 0
while i < len(tokens):
    if tokens[i] == "STOP":
        break
    print("token:", tokens[i])
    i += 1


# =====================================================
# Concept 6: Unpacking Inside a Loop
# =====================================================
"""
Definition:
If every item is a tuple or a list of the same size, you can unpack
it right in the for line: for a, b in my_list.
The number of names must match the size of the item. A name with a *
collects the rest.
"""

# Program 1: A list of tuples
scores = [("Ali", 90), ("Sara", 85)]
for name, score in scores:
    print(name, score)

# Program 2: A list of lists
rows = [["Ali", "Active"], ["Sara", "Inactive"]]
for name, status in rows:
    print(f"{name:<6}{status}")

# Program 3: enumerate() together with unpacking
for number, (name, score) in enumerate(scores, start=1):
    print(f"{number}. {name} scored {score}")

# Program 4: First item and the rest
data = [[1, 2, 3], [4, 5]]
for first, *rest in data:
    print(first, rest)                  # 1 [2, 3]   then   4 [5]

# Program 5: A wrong size raises ValueError
try:
    for a, b in [[1, 2], [3]]:
        print(a, b)
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 2, got 1)


# =====================================================
# Concept 7: zip() (Several Lists at Once)
# =====================================================
"""
Definition:
zip(a, b) walks through the lists together and gives (a[i], b[i])
pairs. It stops when the SHORTEST list ends, without any error.
zip_longest fills the missing values. zip(..., strict=True) raises
an error when the lengths differ. zip(*pairs) does the opposite
(it splits pairs into separate sequences).
"""

# Program 1: Two lists together
names = ["Ali", "Sara", "Bilal"]
ages = [25, 22, 30]
for name, age in zip(names, ages):
    print(name, age)

# Program 2: Different lengths, the longer list is cut silently
print(list(zip([1, 2, 3], ["a", "b"])))                 # [(1, 'a'), (2, 'b')]

# Program 3: zip_longest keeps everything
print(list(zip_longest([1, 2, 3], ["a", "b"], fillvalue="-")))      # [(1, 'a'), (2, 'b'), (3, '-')]

# Program 4: strict=True makes a length mismatch visible
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError as e:
    print("Error:", e)                  # zip() argument 2 is shorter than argument 1

# Program 5: Three lists, and a dictionary from two lists
cities = ["Lahore", "Karachi", "Quetta"]
for name, age, city in zip(names, ages, cities):
    print(f"{name} ({age}) lives in {city}")
print(dict(zip(names, ages)))           # {'Ali': 25, 'Sara': 22, 'Bilal': 30}

# Program 6: Unzip
pairs = [("Ali", 90), ("Sara", 85)]
unzipped_names, unzipped_scores = zip(*pairs)
print(unzipped_names, unzipped_scores)  # ('Ali', 'Sara') (90, 85)

# Program 7: Compare two lists item by item
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Product", "Contact"]
for position, (e, a) in enumerate(zip(expected, actual), start=1):
    if e != a:
        print(f"Item {position}: expected {e!r}, got {a!r}")        # Item 2


# =====================================================
# Concept 8: Looping in a Different Order or on a Part
# =====================================================
"""
Definition:
You can loop over a changed VIEW of the list without changing the list:
reversed(x)         backwards
sorted(x)           sorted (a new list)
x[::2]              every second item
x[1:]               without the first item
x[:]                a copy of the list (safe if you change the list inside the loop)
"""

nums = [10, 20, 30, 40, 50]

# Program 1: Backwards
for n in reversed(nums):
    print(n)                            # 50 40 30 20 10

# Program 2: Sorted, the original order is kept
names = ["sara", "ali", "bilal"]
for name in sorted(names):
    print(name)                         # ali bilal sara
print(names)                            # ['sara', 'ali', 'bilal']

# Program 3: A part of the list
print([n for n in nums[::2]])           # [10, 30, 50]
for n in nums[1:]:
    print("without the first:", n)

# Program 4: Backwards with the index (the position in the ORIGINAL list)
for i in range(len(nums) - 1, -1, -1):
    print(i, nums[i])

# Program 5: A new count from the end
for i, n in enumerate(reversed(nums)):
    print(i, n)                         # 0 50, 1 40, ...


# =====================================================
# Concept 9: Accumulator Patterns
# =====================================================
"""
Definition:
An accumulator is a variable that you create BEFORE the loop and
update INSIDE the loop (a total, a counter, the biggest value so
far, a new list). Create it outside the loop, otherwise it starts
again at every round.
"""

nums = [4, 8, 15, 16, 23, 42]

# Program 1: Sum and average
total = 0
for n in nums:
    total += n
print(total, total / len(nums))         # 108 18.0

# Program 2: Count items that match a condition
even_count = 0
for n in nums:
    if n % 2 == 0:
        even_count += 1
print(even_count)                       # 4

# Program 3: Biggest and smallest
biggest = nums[0]
smallest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n
print(biggest, smallest)                # 42 4

# Program 4: Product and running total
product = 1
for n in [1, 2, 3, 4]:
    product *= n
print(product)                          # 24
running = []
current = 0
for n in [1, 2, 3, 4]:
    current += n
    running.append(current)
print(running)                          # [1, 3, 6, 10]

# Program 5: Build a text, then the shorter way with join()
text = ""
for word in ["a", "b", "c"]:
    text += word
print(text, "".join(["a", "b", "c"]))   # abc abc

# Program 6: The classic mistake, the accumulator inside the loop
for n in [1, 2, 3]:
    total = 0
    total += n
print(total)                            # 3 (only the last item, the old sum was lost)


# =====================================================
# Concept 10: Filtering and Transforming into a New List
# =====================================================
"""
Definition:
The usual job of a loop is to build a NEW list: keep some items
(filter), change every item (transform), or both. The original list
stays safe. (Comprehensions do this in one line: file 08.)
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Program 1: Filter
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)                            # [2, 4, 6, 8, 10]

# Program 2: Transform and filter together
odd_squares = []
for n in numbers:
    if n % 2 == 1:
        odd_squares.append(n * n)
print(odd_squares)                      # [1, 9, 25, 49, 81]

# Program 3: The first 3 numbers bigger than 4, then stop
found = []
for n in numbers:
    if n > 4:
        found.append(n)
    if len(found) == 3:
        break
print(found)                            # [5, 6, 7]

# Program 4: Remove blank texts
raw = ["a", " ", "b", "", "c"]
clean = []
for text in raw:
    if text.strip():
        clean.append(text)
print(clean)                            # ['a', 'b', 'c']

# Program 5: Transform all items into their lengths
lengths = []
for name in ["Ali", "Sara", "Bilal"]:
    lengths.append(len(name))
print(lengths)                          # [3, 4, 5]


# =====================================================
# Concept 11: Changing Items While Looping
# =====================================================
"""
Definition:
In "for x in my_list", x points to the item. x = something moves ONLY
the name x, it does not touch the list. To replace an item you need
its position: my_list[i] = ...
Careful: if the item itself is a MUTABLE object (a list), changing
it through x DOES change the list, because both names point to the
same inner list.
"""

# Program 1: Changing the loop variable does nothing to the list
nums = [1, 2, 3]
for n in nums:
    n = n * 10
print(nums)                             # [1, 2, 3]

# Program 2: Fix with the index
for i in range(len(nums)):
    nums[i] = nums[i] * 10
print(nums)                             # [10, 20, 30]

# Program 3: Fix with enumerate()
names = ["ali", "sara"]
for i, name in enumerate(names):
    names[i] = name.title()
print(names)                            # ['Ali', 'Sara']

# Program 4: Strings are immutable, so the name is a new string
words = ["ali", "sara"]
for word in words:
    word = word.upper()
print(words)                            # ['ali', 'sara'] (unchanged)

# Program 5: Inner lists are mutable, so this DOES change the outer list
grid = [[1], [2]]
for row in grid:
    row.append(0)
print(grid)                             # [[1, 0], [2, 0]]


# =====================================================
# Concept 12: Adding or Removing While Looping (the Trap)
# =====================================================
"""
Definition:
A for loop walks by POSITION. If the list changes while it runs:
- items you append at the end WILL be visited too
- items you remove shift to the left, so the next item is skipped
Safe ways: loop over a COPY (my_list[:]), build a NEW list,
walk from the END by index, or use a while loop.
"""

# Program 1: Appended items are visited too (a size limit stops it)
data = [1]
for x in data:
    if len(data) < 5:
        data.append(x + 1)
print(data)                             # [1, 2, 3, 4, 5]

# Program 2: Removing skips items
data = [1, 1, 2, 2, 3]
for x in data:
    if x == 1:
        data.remove(x)
print(data)                             # [1, 2, 2, 3] (one 1 is left)

# Program 3: Safe way 1, loop over a copy
data = [1, 1, 2, 2, 3]
for x in data[:]:
    if x == 1:
        data.remove(x)
print(data)                             # [2, 2, 3]

# Program 4: Safe way 2, build a new list
data = [1, 1, 2, 2, 3]
kept = []
for x in data:
    if x != 1:
        kept.append(x)
print(kept)                             # [2, 2, 3]

# Program 5: Safe way 3, walk from the end
data = [1, 1, 2, 2, 3]
for i in range(len(data) - 1, -1, -1):
    if data[i] == 1:
        del data[i]
print(data)                             # [2, 2, 3]

# Program 6: Safe way 4, a while loop
data = [1, 1, 2, 2, 3]
while 1 in data:
    data.remove(1)
print(data)                             # [2, 2, 3]


# =====================================================
# Concept 13: break, continue and else
# =====================================================
"""
Definition:
break      leaves the loop at once
continue   skips the rest of this round and goes to the next item
else       a block after the loop that runs ONLY if the loop ended
           WITHOUT a break (typical for "search, and tell if nothing was found")
break only leaves the INNERMOST loop.
"""

# Program 1: break at the first match
numbers = [3, 8, 5, 12, 7]
for n in numbers:
    if n % 2 == 0:
        print("First even number:", n)
        break

# Program 2: continue skips an item
for n in numbers:
    if n % 2 == 1:
        continue
    print("even:", n)                   # 8 then 12

# Program 3: for-else, nothing found
names = ["ali", "sara"]
target = "bilal"
for name in names:
    if name == target:
        print("found")
        break
else:
    print(target, "is not in the list")

# Program 4: for-else, found (the else block is skipped)
target = "sara"
for name in names:
    if name == target:
        print("found", name)
        break
else:
    print("not found")

# Program 5: break only leaves the inner loop
grid = [[1, 2], [3, 4], [5, 6]]
visited = 0
for row in grid:
    visited += 1
    for x in row:
        if x == 4:
            break
print("rows visited:", visited)         # 3 (the outer loop kept going)

# Program 6: Leave both loops with a flag
visited = 0
found = False
for row in grid:
    visited += 1
    for x in row:
        if x == 4:
            found = True
            break
    if found:
        break
print("rows visited:", visited)         # 2


# =====================================================
# Concept 14: Nested Loops
# =====================================================
"""
Definition:
A loop inside a loop. The inner loop runs completely for EVERY round
of the outer loop. The body runs len(a) * len(b) times.
"""

# Program 1: All combinations of two lists
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
for color in colors:
    for size in sizes:
        print(color, size)

# Program 2: A multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i * j:>3}", end="")
    print()

# Program 3: Find duplicates by comparing every pair (i < j avoids comparing twice)
data = [1, 2, 3, 2]
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] == data[j]:
            print("duplicate", data[i], "at index", i, "and", j)      # 2 at 1 and 3

# Program 4: Common items of two lists
a = [1, 2, 3, 4]
b = [3, 4, 5]
common = []
for x in a:
    if x in b and x not in common:
        common.append(x)
print(common)                           # [3, 4]

# Program 5: Sum of a 2D list
matrix = [[1, 2, 3], [4, 5, 6]]
total = 0
for row in matrix:
    for value in row:
        total += value
print(total)                            # 21

# Program 6: Count the rounds
rounds = 0
for x in [1, 2, 3]:
    for y in ["a", "b", "c", "d"]:
        rounds += 1
print(rounds)                           # 12


# =====================================================
# Concept 15: Looping Over Tables and Records
# =====================================================
"""
Definition:
Real data is often a list of lists (rows) or a list of dictionaries
(records). Loop over the rows, then use indexes or keys inside.
"""

# Program 1: A table with a header row
table = [["Name", "Score"], ["Ali", "90"], ["Sara", "85"]]
header = table[0]
print(f"{header[0]:<6}{header[1]}")
for row in table[1:]:
    print(f"{row[0]:<6}{row[1]}")

# Program 2: A list of dictionaries
users = [
    {"name": "Ali", "age": 25, "active": True},
    {"name": "Sara", "age": 22, "active": False},
    {"name": "Bilal", "age": 30, "active": True},
]
active_names = []
for user in users:
    if user["active"]:
        active_names.append(user["name"])
print(active_names)                     # ['Ali', 'Bilal']

# Program 3: Average age
total_age = 0
for user in users:
    total_age += user["age"]
print(f"{total_age / len(users):.1f}")  # 25.7

# Program 4: Find a record by a value
wanted = "Sara"
for user in users:
    if user["name"] == wanted:
        print(user)
        break
else:
    print(wanted, "not found")


# =====================================================
# Concept 16: Search Patterns
# =====================================================
"""
Definition:
Three questions you ask a list all the time:
1) What is the FIRST item that matches?   (loop + break, or None if nothing)
2) Does ANY item match?                   any(...)
3) Do ALL items match?                    all(...)
(The short generator expressions inside any/all are explained in file 08.)
"""

numbers = [1, 3, 6, 8]

# Program 1: First match, or None
first_even = None
for n in numbers:
    if n % 2 == 0:
        first_even = n
        break
print(first_even)                       # 6

# Program 2: Any and all
print(any(n % 2 == 0 for n in numbers))         # True
print(all(n % 2 == 0 for n in numbers))         # False
print(all(n > 0 for n in numbers))              # True

# Program 3: The same checks with a flag
all_positive = True
for n in numbers:
    if n <= 0:
        all_positive = False
        break
print(all_positive)                     # True

# Program 4: any() and all() on an EMPTY list
print(any([]), all([]))                 # False True (all() has nothing to disprove)


# =====================================================
# Concept 17: The Loop Variable After the Loop
# =====================================================
"""
Definition:
The loop variable is NOT deleted after the loop, it keeps the last
item. If the list was empty, the variable never gets created. And a
loop variable can overwrite an older variable with the same name.
"""

# Program 1: The last item stays
for letter in ["a", "b", "c"]:
    pass
print(letter)                           # c

# Program 2: An empty list never creates the variable
for brand_new_name in []:
    pass
try:
    print(brand_new_name)
except NameError as e:
    print("Error:", e)                  # name 'brand_new_name' is not defined

# Program 3: A loop variable overwrites an older variable
item = "keep me"
for item in ["a", "b"]:
    pass
print(item)                             # b


# =====================================================
# Concept 18: How a for Loop Works (Iterators)
# =====================================================
"""
Definition:
A for loop calls iter() on the list to get an ITERATOR, then asks it
for the next item again and again with next() until it raises
StopIteration. An iterator can be used ONCE, a list can be looped
many times.
"""

# Program 1: Do it by hand
it = iter([1, 2])
print(next(it))                         # 1
print(next(it))                         # 2

# Program 2: At the end
print(next(it, "done"))                 # done (a default instead of an error)
try:
    next(it)
except StopIteration:
    print("StopIteration: no more items")

# Program 3: The loop itself is a while loop in disguise
it = iter(["a", "b", "c"])
while True:
    try:
        item = next(it)
    except StopIteration:
        break
    print(item)

# Program 4: A list can be looped again, an iterator cannot
data = [1, 2, 3]
print(sum(data), sum(data))             # 6 6
it = iter(data)
print(sum(it), sum(it))                 # 6 0

# Program 5: Looping over a dictionary
scores = {"a": 1, "b": 2}
for key in scores:
    print(key)
for value in scores.values():
    print(value)
for key, value in scores.items():
    print(key, value)


# =====================================================
# Concept 19: Loops vs Comprehensions (Preview)
# =====================================================
"""
Definition:
A list comprehension builds a list in one line. It is the short form
of a loop that appends to a new list. Use a normal loop when the
body is long or has side effects (printing, changing things).
(Full explanation: 08_list_comprehension.py)
"""

numbers = [1, 2, 3, 4, 5, 6]

# Program 1: Loop and comprehension, the same result
squares_loop = []
for n in numbers:
    squares_loop.append(n * n)
squares_short = [n * n for n in numbers]
print(squares_loop == squares_short)    # True

# Program 2: With a condition
even_loop = []
for n in numbers:
    if n % 2 == 0:
        even_loop.append(n)
even_short = [n for n in numbers if n % 2 == 0]
print(even_loop, even_short)            # [2, 4, 6] [2, 4, 6]


# =====================================================
# Concept 20: Good Habits for Fast Loops
# =====================================================
"""
Definition:
1) "x in my_list" checks the items one by one, so inside a big loop
   it gets slow. Use a set for fast lookups.
2) Do not build text with += in a long loop, collect and join().
3) pop(0) and insert(0, x) in a loop are slow on big lists.
4) Do not call a slow function again and again inside the loop if
   its result does not change, calculate it once before the loop.
The times below depend on your computer, only compare them.
"""

# Program 1: List lookup vs set lookup
big_list = list(range(2000))
big_set = set(big_list)
lookups = list(range(2000, 4000))       # none of these is in the list (the slowest case)

start = time.perf_counter()
hits = 0
for x in lookups:
    if x in big_list:
        hits += 1
time_list = time.perf_counter() - start

start = time.perf_counter()
hits_set = 0
for x in lookups:
    if x in big_set:
        hits_set += 1
time_set = time.perf_counter() - start

print(f"list: {time_list:.4f}s | set: {time_set:.4f}s")
print(hits == hits_set, time_set < time_list)   # True True

# Program 2: Calculate once, use many times
words = ["Apple", "Banana", "Cherry"]
target = "banana"
lowered_target = target.lower()         # done once, not at every round
for w in words:
    if w.lower() == lowered_target:
        print("match:", w)


# =====================================================
# Concept 21: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with loops:
1) for i in len(my_list)       -> len() is a number, not iterable
2) enumerate() names swapped   -> the index comes FIRST
3) zip() drops items silently  -> use strict=True when lengths must match
4) a while loop that never changes its condition
5) range(len(x) + 1)           -> off by one, IndexError
6) changing the loop variable and expecting the list to change
7) removing items while looping
"""

nums = [10, 20, 30]

# Program 1: len() is not iterable
try:
    for i in len(nums):
        pass
except TypeError as e:
    print("Error:", e)                  # 'int' object is not iterable

# Program 2: The names of enumerate() swapped
for item, index in enumerate(["a", "b"]):
    print(item, index)                  # 0 a   1 b  (the names are wrong, not the values)

# Program 3: zip() drops items silently
names = ["Ali", "Sara", "Bilal"]
scores = [90, 85]
print(list(zip(names, scores)))         # [('Ali', 90), ('Sara', 85)] (Bilal is missing)

# Program 4: A while loop that never ends (stopped here by a guard)
i = 0
guard = 0
while i < 3:
    guard += 1                          # the mistake: i is never increased
    if guard > 5:
        print("stopped after 5 rounds, i is still", i)
        break

# Program 5: Off by one
try:
    for i in range(len(nums) + 1):
        print(nums[i])
except IndexError as e:
    print("Error:", e)                  # list index out of range (at i = 3)

# Program 6: Changing the loop variable
for n in nums:
    n += 1
print(nums)                             # [10, 20, 30] (unchanged)


# =====================================================
# Concept 22: Looping in SQA Automation
# =====================================================
"""
Definition:
Test code loops all the time: over test data, over elements of a
page, over results and over log lines. Good habits:
- check ALL items and collect every failure, instead of stopping at the first
- use for-else for "search, and fail if nothing was found"
- put the position in the message (enumerate), so the failure is easy to find
- check that both lists have the same length before comparing
Real Playwright code would look like this (not executed here):
    for text in page.locator("li").all_inner_texts():
        print(text)
    for i in range(page.locator("li").count()):
        print(page.locator("li").nth(i).inner_text())
"""

# Program 1: Count the results
results = [("login", "PASS"), ("cart", "FAIL"), ("search", "PASS"), ("payment", "ERROR")]
counts = {"PASS": 0, "FAIL": 0, "ERROR": 0}
for name, status in results:
    counts[status] += 1
print(counts)                           # {'PASS': 2, 'FAIL': 1, 'ERROR': 1}

# Program 2: Check every menu item, with its position in the message
menu_texts = ["Home", "Products", "", "Contact"]
for position, text in enumerate(menu_texts, start=1):
    if not text.strip():
        print(f"FAIL: menu item {position} is empty")

# Program 3: Soft checks, collect ALL failures
expected_labels = ["Home", "Products", "Contact"]
actual_labels = ["Home", "Product", "Contact "]
failures = []
if len(expected_labels) != len(actual_labels):
    failures.append("different number of labels")
for index, (e, a) in enumerate(zip(expected_labels, actual_labels), start=1):
    if e != a.strip():
        failures.append(f"item {index}: expected {e!r}, got {a!r}")
if failures:
    print("FAILED:", failures)          # one failure, the 2nd item
else:
    print("PASSED")

# Program 4: A data driven login check (the 'application' is a small dictionary here)
valid_users = {"admin": "Admin@123", "tester": "Test@456"}
login_rows = [
    ("admin", "Admin@123", True),
    ("admin", "wrong", False),
    ("", "Admin@123", False),
    ("tester", "Test@456", True),
    ("unknown", "x", False),
]
for username, password, expected_ok in login_rows:
    actual_ok = valid_users.get(username) == password
    print("PASS" if actual_ok == expected_ok else "FAIL", f"user={username!r:<10} expected={expected_ok}")

# Program 5: Wait until a page is ready (for-else, a real wait would sleep between tries)
for page_states in (["loading", "loading", "ready"], ["loading", "loading", "loading"]):
    for attempt, state in enumerate(page_states, start=1):
        print(f"Attempt {attempt}: {state}")
        if state == "ready":
            print("Page is ready")
            break
    else:
        print("FAIL: the page never became ready")

# Program 6: Compare two tables cell by cell
expected_table = [["Ali", "Active"], ["Sara", "Inactive"]]
actual_table = [["Ali", "Active"], ["Sara", "Active"]]
for row_number, (expected_row, actual_row) in enumerate(zip(expected_table, actual_table), start=1):
    for column_number, (e, a) in enumerate(zip(expected_row, actual_row), start=1):
        if e != a:
            print(f"Row {row_number}, column {column_number}: expected {e!r}, got {a!r}")

# Program 7: Count the levels of a log
log_lines = ["[PASS] a", "[FAIL] b", "[PASS] c", "[ERROR] d", "[PASS] e"]
level_counts = {}
for line in log_lines:
    level = line.split()[0].strip("[]")
    level_counts[level] = level_counts.get(level, 0) + 1
print(level_counts)                     # {'PASS': 3, 'FAIL': 1, 'ERROR': 1}

# Program 8: Duplicated test ids
ids = ["TC_001", "TC_002", "TC_001", "TC_003", "TC_002"]
seen = []
duplicates = []
for tid in ids:
    if tid in seen and tid not in duplicates:
        duplicates.append(tid)
    seen.append(tid)
print(duplicates)                       # ['TC_001', 'TC_002']

# Program 9: Is a list sorted? (compare every item with its neighbour using zip)
for prices in ([9.99, 45.0, 199.0], [9.99, 199.0, 45.0]):
    ordered = True
    for before, after in zip(prices, prices[1:]):
        if before > after:
            print(f"FAIL: {before} is followed by the smaller {after}")
            ordered = False
            break
    if ordered:
        print("PASS: prices are in ascending order")

# Program 10: A test matrix, every test on every browser
browsers = ["chromium", "firefox"]
tests = ["login", "cart", "search"]
runs = []
for browser in browsers:
    for test in tests:
        runs.append(f"{test} on {browser}")
print(len(runs), runs[0], "|", runs[-1])        # 6 login on chromium | search on firefox