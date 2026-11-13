"""
====================================================
10_Lists / 12_list_built_in_functions.py
====================================================
Topic: Built-in Functions That Work with Lists
====================================================
Notes before you run this file:
1) A built-in function is ready to use, with no import. It is written
   as function(my_list), unlike a method, which is written
   my_list.method().
2) Built-in functions READ the list and give back something new. They
   never change the list.
3) Some of them return a plain value (len, sum, min, max, any, all).
   Some return a new list (sorted, list). Some return an ITERATOR
   (reversed, enumerate, zip, map, filter, iter). An iterator is lazy
   and can be used only ONCE.
4) Python versions: zip(strict=True) needs 3.10 or newer. In Python
   3.12 sum() became more accurate for floats (Concept 3).
5) Never use a built-in name as a variable name (sum, max, min, len,
   list, ...). Concept 22 shows what happens.
6) Plain programs only, no functions.
"""

import math
import statistics
import itertools
import sys
from functools import reduce


# =====================================================
# Concept 1: Overview of the Built-in Functions for Lists
# =====================================================
"""
Definition:
Gives a value:     len, sum, min, max, any, all
Gives a new list:  sorted, list
Gives an iterator: reversed, enumerate, zip, map, filter, iter
Gives information: isinstance, type, id, callable
Also useful:       range, print, round, abs, divmod, pow
"""

# Program 1: The four most used
nums = [4, 8, 15]
print(len(nums), sum(nums), min(nums), max(nums))       # 3 27 4 15

# Program 2: The list is not changed
sorted(nums, reverse=True)
list(reversed(nums))
print(nums)                             # [4, 8, 15]

# Program 3: A function and a method side by side
print(len(nums))                        # 3  (function)
print(nums.count(4))                    # 1  (method)

# Program 4: Is it callable?
print(callable(len), callable(nums))    # True False


# =====================================================
# Concept 2: len()
# =====================================================
"""
Definition:
len(x) returns the number of items of a sequence or collection.
An inner list counts as ONE item. Numbers, None, generators and
map/filter objects have no length.
"""

# Program 1: Simple lengths
print(len([10, 20, 30]), len([]), len([[1, 2], [3]]))   # 3 0 2

# Program 2: Other types
print(len("hello"), len((1, 2)), len({"a": 1}), len(range(5)))      # 5 2 1 5

# Program 3: The last index is len - 1
items = ["a", "b", "c"]
print(items[len(items) - 1], items[-1])                 # c c

# Program 4: Errors
try:
    len(5)
except TypeError as e:
    print("Error:", e)                  # object of type 'int' has no len()
try:
    len(None)
except TypeError as e:
    print("Error:", e)                  # object of type 'NoneType' has no len()

# Program 5: A generator has no length, make a list first
gen = (x for x in range(3))
try:
    len(gen)
except TypeError as e:
    print("Error:", e)                  # object of type 'generator' has no len()
print(len(list(gen)))                   # 3

# Program 6: Checking for an empty list
data = []
print(len(data) == 0, not data)         # True True


# =====================================================
# Concept 3: sum()
# =====================================================
"""
Definition:
sum(iterable, start=0) adds all the items to 'start'. The sum of an
empty list is the start value. sum() works for numbers. For strings
use "".join(). To count items that match a condition use
sum(1 for x in data if condition), because True counts as 1.
"""

# Program 1: Basic sums
print(sum([1, 2, 3, 4]), sum([]), sum([1.5, 2.5]))      # 10 0 4.0

# Program 2: A start value
print(sum([1, 2, 3], 10))               # 16

# Program 3: Average
marks = [80, 90, 70]
print(sum(marks) / len(marks))          # 80.0

# Program 4: Count with booleans
print(sum([True, False, True]))         # 2
print(sum(n > 3 for n in [1, 5, 7, 2])) # 2 (how many numbers are bigger than 3)

# Program 5: Join lists with [] as start (slow for big data, only for small examples)
print(sum([[1, 2], [3]], []))           # [1, 2, 3]

# Program 6: Strings cannot be summed
try:
    sum(["a", "b"])
except TypeError as e:
    print("Error:", e)                  # unsupported operand type(s) for +: 'int' and 'str'
try:
    sum(["a", "b"], "")
except TypeError as e:
    print(type(e).__name__)             # TypeError (the message advises "".join())
print("".join(["a", "b"]))              # ab

# Program 7: Float precision
print(sum([0.1] * 10) == 1.0)           # False before Python 3.12, True from 3.12
print(math.fsum([0.1] * 10) == 1.0)     # True (fsum is exact)
print(math.isclose(sum([0.1] * 10), 1.0))       # True (compare floats with a tolerance)

# Program 8: The average of an empty list
empty = []
try:
    print(sum(empty) / len(empty))
except ZeroDivisionError as e:
    print("Error:", e)                  # division by zero
print(sum(empty) / len(empty) if empty else "no data")  # no data


# =====================================================
# Concept 4: min() and max()
# =====================================================
"""
Definition:
min(iterable) and max(iterable) return the smallest and the biggest
item. They also accept several arguments: max(3, 9, 2). Strings are
compared by their Unicode numbers (capitals before small letters).
The items must be comparable with each other. On an EMPTY list they
raise ValueError, unless you give default=.
"""

# Program 1: Numbers and several arguments
print(min([3, 9, 2]), max([3, 9, 2]))   # 2 9
print(max(3, 9, 2), min(3, 9, 2))       # 9 2

# Program 2: Strings
print(min(["pear", "apple", "fig"]), max(["pear", "apple", "fig"]))     # apple pear

# Program 3: With a tie, the first one wins
print(max([1, 5, 5, 2]), [1, 5, 5, 2].index(5))         # 5 1

# Program 4: The position of the biggest item
nums = [4, 9, 2, 9]
print(nums.index(max(nums)))            # 1

# Program 5: Empty list
try:
    max([])
except ValueError as e:
    print(type(e).__name__)             # ValueError (the message wording depends on the version)
print(max([], default=0), min([], default=None))        # 0 None

# Program 6: Mixed types cannot be compared
try:
    max([1, "a"])
except TypeError as e:
    print(type(e).__name__)             # TypeError

# Program 7: Biggest and smallest cell of a 2D list
m = [[1, 9], [4, 2]]
print(max(max(row) for row in m), min(min(row) for row in m))   # 9 1
print(max(x for row in m for x in row))                         # 9

# Program 8: The second biggest value
print(sorted(set([5, 9, 9, 3]))[-2])    # 5

# Program 9: A dictionary
scores = {"Ali": 90, "Sara": 85}
print(max(scores))                      # Sara (the biggest KEY, alphabetically)
print(max(scores, key=scores.get))      # Ali (the key with the biggest value)
print(max(scores.values()))             # 90


# =====================================================
# Concept 5: key= and default= for min() and max()
# =====================================================
"""
Definition:
key=function tells min() and max() WHAT to compare. You get back the
ORIGINAL item, not the key. The key function is written without
brackets and is called once for each item.
default=value is returned when the iterable is empty.
"""

# Program 1: The longest and the shortest word
words = ["pear", "fig", "banana", "kiwi"]
print(max(words, key=len), min(words, key=len))         # banana fig

# Program 2: With a tie the first item wins
print(max(["ab", "cd"], key=len))       # ab

# Program 3: Pick a whole record by one field
students = [("Ali", 90), ("Sara", 85), ("Bilal", 95)]
print(max(students, key=lambda s: s[1]))        # ('Bilal', 95)
print(min(students, key=lambda s: s[1]))        # ('Sara', 85)

# Program 4: By absolute value
print(max([-10, 3, 7], key=abs), min([-10, 3, 7], key=abs))     # -10 3

# Program 5: Ignore the case
names = ["apple", "Zebra", "mango"]
print(max(names))                       # mango (capitals come first in the Unicode order)
print(max(names, key=str.casefold))     # Zebra

# Program 6: The key function is called once per item
calls = []
print(max([1, 2, 3], key=lambda x: calls.append(x) or x))       # 3
print(calls)                            # [1, 2, 3]


# =====================================================
# Concept 6: sorted()
# =====================================================
"""
Definition:
sorted(iterable, key=None, reverse=False) returns a NEW sorted list.
It accepts any iterable and the original is not changed. The method
list.sort() changes the list itself and returns None.
(Full details: 06_list_sorting_reversing.py)
"""

# Program 1: The original stays the same
nums = [3, 1, 2]
print(sorted(nums), nums)               # [1, 2, 3] [3, 1, 2]

# Program 2: key and reverse
print(sorted(["pear", "fig", "banana"], key=len, reverse=True))     # ['banana', 'pear', 'fig']

# Program 3: Any iterable
print(sorted("hello"))                  # ['e', 'h', 'l', 'l', 'o']
print(sorted({3, 1, 2}))                # [1, 2, 3]
print(sorted({"b": 1, "a": 2}))         # ['a', 'b']

# Program 4: The ends of a sorted list
print(sorted(nums)[0] == min(nums), sorted(nums)[-1] == max(nums))      # True True

# Program 5: The three biggest scores
scores = [55, 90, 72, 88, 64]
print(sorted(scores, reverse=True)[:3]) # [90, 88, 72]

# Program 6: The result is lost if you do not store it
sorted(nums)
print(nums)                             # [3, 1, 2]


# =====================================================
# Concept 7: reversed()
# =====================================================
"""
Definition:
reversed(sequence) gives an ITERATOR that goes from the last item to
the first. It does not change the original. Use list(reversed(x))
for a list. It works on sequences (list, tuple, string, range) but
not on sets or generators.
"""

# Program 1: The type and the result
r = reversed([1, 2, 3])
print(type(r).__name__)                 # list_reverseiterator
print(list(r))                          # [3, 2, 1]

# Program 2: Loop backwards
for x in reversed(["a", "b", "c"]):
    print(x)                            # c b a

# Program 3: An iterator is used up after one pass
r = reversed([1, 2])
print(list(r), list(r))                 # [2, 1] []

# Program 4: A set cannot be reversed
try:
    reversed({1, 2})
except TypeError as e:
    print("Error:", e)                  # 'set' object is not reversible

# Program 5: Palindrome check
data = [1, 2, 1]
print(list(reversed(data)) == data)     # True


# =====================================================
# Concept 8: enumerate()
# =====================================================
"""
Definition:
enumerate(iterable, start=0) gives (index, item) pairs. 'start'
changes only the numbers, not the items.
"""

# Program 1: Pairs
print(list(enumerate(["a", "b"])))              # [(0, 'a'), (1, 'b')]
print(list(enumerate(["a", "b"], start=1)))     # [(1, 'a'), (2, 'b')]

# Program 2: A numbered list
for number, name in enumerate(["Ali", "Sara"], start=1):
    print(f"{number}. {name}")

# Program 3: All positions of a value
data = [5, 7, 5]
print([i for i, v in enumerate(data) if v == 5])        # [0, 2]

# Program 4: A string
print(list(enumerate("ab")))            # [(0, 'a'), (1, 'b')]

# Program 5: It is an iterator, it is used up
e = enumerate("ab")
print(list(e), list(e))                 # [(0, 'a'), (1, 'b')] []

# Program 6: A dictionary from the pairs
print(dict(enumerate(["x", "y"])))      # {0: 'x', 1: 'y'}


# =====================================================
# Concept 9: zip()
# =====================================================
"""
Definition:
zip(a, b, ...) walks through several iterables together and gives
tuples: (a[0], b[0]), (a[1], b[1]) ... It stops at the SHORTEST one
without any error. zip(..., strict=True) raises ValueError when the
lengths differ (Python 3.10+). zip(*pairs) does the opposite (unzip).
"""

# Program 1: Pairs
print(list(zip([1, 2, 3], ["a", "b", "c"])))    # [(1, 'a'), (2, 'b'), (3, 'c')]

# Program 2: The shortest one decides
print(list(zip([1, 2, 3], ["a", "b"])))         # [(1, 'a'), (2, 'b')]

# Program 3: strict=True makes a mismatch visible
try:
    list(zip([1, 2, 3], ["a", "b"], strict=True))
except ValueError as e:
    print(type(e).__name__)             # ValueError

# Program 4: Three lists in a loop
for name, age, city in zip(["Ali", "Sara"], [25, 22], ["Lahore", "Karachi"]):
    print(name, age, city)

# Program 5: A dictionary from two lists
print(dict(zip(["a", "b"], [1, 2])))    # {'a': 1, 'b': 2}

# Program 6: Unzip
letters, numbers = zip(*[("a", 1), ("b", 2)])
print(letters, numbers)                 # ('a', 'b') (1, 2)

# Program 7: Neighbours (differences between steps)
nums = [1, 3, 6, 10]
print([b - a for a, b in zip(nums, nums[1:])])  # [2, 3, 4]

# Program 8: An iterator is used up
z = zip([1], [2])
print(list(z), list(z))                 # [(1, 2)] []


# =====================================================
# Concept 10: map()
# =====================================================
"""
Definition:
map(function, iterable, ...) applies the function to every item and
gives an ITERATOR of the results (lazy, one use). With several
iterables the function gets several arguments and map stops at the
shortest one. Use list(map(...)) to get a list.
"""

# Program 1: A ready-made function
print(list(map(int, ["1", "2", "3"])))          # [1, 2, 3]

# Program 2: A lambda
print(list(map(lambda n: n * n, [1, 2, 3])))    # [1, 4, 9]

# Program 3: Two iterables
print(list(map(pow, [2, 3, 4], [3, 2, 1])))     # [8, 9, 4]

# Program 4: map is an iterator
m = map(str.upper, ["a", "b"])
print(type(m).__name__)                 # map
print(list(m), list(m))                 # ['A', 'B'] []

# Program 5: map is lazy, nothing runs until you ask
m = map(print, ["x", "y"])
print("map created, nothing printed yet")
result = list(m)                        # now x and y are printed
print(result)                           # [None, None]

# Program 6: Methods as functions
print(list(map(str.strip, ["  a ", "b  "])))    # ['a', 'b']
print(list(map(len, ["ab", "cde"])))            # [2, 3]

# Program 7: Total number of items of all rows
print(sum(map(len, [[1], [2, 3], [4, 5, 6]])))  # 6

# Program 8: map and a comprehension give the same result
print([int(x) for x in "3 5 8".split()] == list(map(int, "3 5 8".split())))    # True

# Program 9: It stops at the shortest
print(list(map(lambda a, b: a + b, [1, 2, 3], [10, 20])))       # [11, 22]


# =====================================================
# Concept 11: filter()
# =====================================================
"""
Definition:
filter(function, iterable) keeps the items for which the function
returns a true value, and gives an ITERATOR. filter(None, items)
keeps the items that are true themselves (it drops 0, "", None, [],
False ...). map CHANGES items, filter KEEPS or DROPS them.
"""

# Program 1: A lambda
print(list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6])))   # [2, 4, 6]

# Program 2: None as the function
print(list(filter(None, [0, 1, "", 2, None, "a", []])))         # [1, 2, 'a']

# Program 3: A ready-made function
print(list(filter(str.isdigit, ["1", "a", "22", "b3"])))        # ['1', '22']

# Program 4: Drop blank texts
print(list(filter(str.strip, ["a", " ", "b", ""])))             # ['a', 'b']

# Program 5: An iterator, used once
f = filter(None, [0, 1])
print(type(f).__name__)                 # filter
print(list(f), list(f))                 # [1] []

# Program 6: Filter and map together
print(list(map(lambda n: n * 10, filter(lambda n: n > 2, [1, 2, 3, 4]))))      # [30, 40]
print([n * 10 for n in [1, 2, 3, 4] if n > 2])                  # [30, 40] (same result)


# =====================================================
# Concept 12: lambda (Small Unnamed Functions)
# =====================================================
"""
Definition:
lambda parameters: expression  creates a small function without a name.
It can hold only ONE expression, and that value is returned. It is
mostly used as key= for sorted/min/max, and inside map/filter.
For anything longer use a normal def.
"""

# Program 1: Define and call
square = lambda x: x * x
print(square(5))                        # 25
print((lambda a, b: a + b)(2, 3))       # 5

# Program 2: As a key
print(sorted(["pear", "fig", "banana"], key=lambda w: len(w)))  # ['fig', 'pear', 'banana']

# Program 3: Sort pairs by the second value
print(sorted([("a", 3), ("b", 1)], key=lambda p: p[1]))         # [('b', 1), ('a', 3)]

# Program 4: With a condition inside
label = lambda n: "even" if n % 2 == 0 else "odd"
print([label(n) for n in [1, 2]])       # ['odd', 'even']

# Program 5: Every lambda has the same name
print(callable(square), square.__name__)        # True <lambda>


# =====================================================
# Concept 13: any() and all()
# =====================================================
"""
Definition:
any(iterable)  True if AT LEAST ONE item is true.
all(iterable)  True if EVERY item is true.
Both stop as soon as the answer is known (short-circuit). On an empty
list: any gives False, all gives True. They look at the TRUTH VALUE of
items, not at the words True and False.
"""

# Program 1: Basics
print(any([0, 0, 1]), all([1, 1, 0]))   # True False

# Program 2: Empty lists
print(any([]), all([]))                 # False True

# Program 3: Truth values
print(any([0, "", None]))               # False
print(all([1, "a", [0]]))               # True ([0] is a non-empty list, so it is true)

# Program 4: With a generator expression
nums = [2, 4, 6]
print(all(n % 2 == 0 for n in nums))    # True
print(any(n > 5 for n in nums))         # True

# Program 5: Short-circuit, the loop stops at the first True
result = any(print("checking", n) or n > 1 for n in [1, 2, 3])
print(result)                           # True (3 was never checked)

# Program 6: any() with == is the same as in
print(5 in [1, 5], any(x == 5 for x in [1, 5]))         # True True

# Program 7: Same type for all items
print(all(isinstance(x, int) for x in [1, 2, 3]))       # True

# Program 8: Is a list sorted?
for data in ([1, 2, 2, 5], [3, 1]):
    print(data, all(a <= b for a, b in zip(data, data[1:])))    # True / False


# =====================================================
# Concept 14: Converting with list(), tuple(), set(), dict()
# =====================================================
"""
Definition:
The type names are also functions that build a new object from an
iterable:
list(x)   a NEW list (a shallow copy of a list)
tuple(x)  a tuple      set(x) a set (no duplicates, no order)
dict(pairs) a dictionary from (key, value) pairs
"""

# Program 1: list()
print(list("abc"), list((1, 2)), list(range(3)), list({"a": 1}))    # ['a', 'b', 'c'] [1, 2] [0, 1, 2] ['a']

# Program 2: tuple() and set()
print(tuple([1, 2]))                    # (1, 2)
print(sorted(set([1, 1, 2])), len(set([1, 1, 2])))      # [1, 2] 2

# Program 3: Remove duplicates, keep the order
print(list(dict.fromkeys(["a", "b", "a"])))     # ['a', 'b']

# Program 4: dict()
print(dict([("a", 1), ("b", 2)]))       # {'a': 1, 'b': 2}

# Program 5: Numbers to text
print(list(map(str, [1, 2, 3])))        # ['1', '2', '3']
print(",".join(map(str, [1, 2, 3])))    # 1,2,3

# Program 6: list() makes a copy
a = [1, 2]
b = list(a)
print(b == a, b is a)                   # True False

# Program 7: bool()
print(bool([]), bool([0]))              # False True

# Program 8: A list of lists of characters
print(list(map(list, ["ab", "cd"])))    # [['a', 'b'], ['c', 'd']]


# =====================================================
# Concept 15: range()
# =====================================================
"""
Definition:
range(stop), range(start, stop), range(start, stop, step) is a lazy
sequence of integers. It is NOT a list, but it has len(), indexing,
and "in", and it stores only 3 numbers, whatever its size.
The stop value is excluded. Floats are not allowed.
"""

# Program 1: The forms
print(list(range(5)))                   # [0, 1, 2, 3, 4]
print(list(range(2, 6)))                # [2, 3, 4, 5]
print(list(range(0, 10, 3)))            # [0, 3, 6, 9]
print(list(range(10, 0, -3)))           # [10, 7, 4, 1]

# Program 2: It behaves like a sequence
r = range(5)
print(type(r).__name__, len(r), r[2], 3 in r)           # range 5 2 True
print(range(1, 10, 2)[-1])              # 9

# Program 3: Empty ranges
print(list(range(5, 1)), list(range(0)))                # [] []

# Program 4: Floats are not allowed
try:
    range(2.5)
except TypeError as e:
    print("Error:", e)                  # 'float' object cannot be interpreted as an integer

# Program 5: The indexes of a list
for i in range(len(["a", "b"])):
    print(i)                            # 0 1

# Program 6: Sum of 1 to 100
print(sum(range(1, 101)))               # 5050

# Program 7: A small object, however big the range
print(sys.getsizeof(range(10)) == sys.getsizeof(range(10 ** 6)))        # True


# =====================================================
# Concept 16: isinstance() and type()
# =====================================================
"""
Definition:
isinstance(x, list)          is x a list (or a subclass of it)?
isinstance(x, (list, tuple)) a tuple of types means "any of these"
type(x).__name__             the name of the type as text
Use isinstance() to check data BEFORE you work with it. Note that
True and False are integers in Python (bool is a subclass of int).
"""

# Program 1: Basic checks
print(isinstance([1], list), isinstance((1,), list), isinstance("ab", list))    # True False False

# Program 2: Several types
print(isinstance((1,), (list, tuple)))  # True

# Program 3: type()
print(type([1]) is list, type([]).__name__)             # True list

# Program 4: bool is an int
print(isinstance(True, int), type(True) is int)         # True False

# Program 5: Check a list of different values
for v in [[1, 2], "ab", (3,), None]:
    print(repr(v), isinstance(v, list))

# Program 6: Real integers only (no booleans)
print(all(isinstance(x, int) and not isinstance(x, bool) for x in [1, 2, True]))       # False

# Program 7: A safe length
for v in ([1, 2], None, 5):
    if isinstance(v, (list, tuple, str)):
        print(len(v))                   # 2
    else:
        print(repr(v), "has no length") # None has no length   5 has no length


# =====================================================
# Concept 17: abs(), round(), divmod(), pow()
# =====================================================
"""
Definition:
abs(x)          absolute value
round(x, n)     rounds to n decimals. A .5 is rounded to the EVEN
                neighbour (round(2.5) is 2, round(3.5) is 4)
divmod(a, b)    (a // b, a % b) in one step
pow(a, b)       a ** b, and pow(a, b, m) is (a ** b) % m
They are very often used together with map() and comprehensions.
"""

# Program 1: abs
print(list(map(abs, [-3, 4, -5])))      # [3, 4, 5]
print(sum(abs(x) for x in [-1, 2, -3])) # 6

# Program 2: round to whole numbers (a .5 goes to the even number)
print(round(7.5), round(2.5), round(3.5), round(0.5))   # 8 2 4 0

# Program 3: round with decimals
print([round(x, 1) for x in [1.26, 2.34, 3.78]])        # [1.3, 2.3, 3.8]
print(round(3.14159, 2))                # 3.14

# Program 4: Floats are stored slightly off
print(round(2.675, 2))                  # 2.67 (not 2.68, the float is a little smaller than 2.675)

# Program 5: divmod
print(divmod(17, 5), divmod(125, 60))   # (3, 2) (2, 5)

# Program 6: pow
print(pow(2, 3), pow(2, 3, 5))          # 8 3
print(list(map(pow, [1, 2, 3], [2, 2, 2])))             # [1, 4, 9]

# Program 7: An average printed to two decimals
nums = [70, 85, 90]
print(f"{sum(nums) / len(nums):.2f}")   # 81.67


# =====================================================
# Concept 18: The statistics Module
# =====================================================
"""
Definition:
statistics (part of Python) gives mean, median, mode and spread.
The median is the middle value of the SORTED data (the average of
the two middle ones when the count is even). The median is not
disturbed by one huge value, the mean is. An empty list raises
StatisticsError.
"""

# Program 1: mean, median, mode
data = [1, 2, 2, 3, 4]
print(statistics.mean(data), statistics.median(data), statistics.mode(data))    # 2.4 2 2

# Program 2: An even number of items
print(statistics.median([1, 2, 3, 4]))  # 2.5

# Program 3: Several most common values
print(statistics.multimode([1, 1, 2, 2, 3]))            # [1, 2]

# Program 4: The spread
print(statistics.pstdev([2, 4, 4, 4, 5, 5, 7, 9]))      # 2.0

# Program 5: An empty list
try:
    statistics.mean([])
except statistics.StatisticsError as e:
    print(type(e).__name__)             # StatisticsError

# Program 6: Same as sum / len
print(statistics.mean([1, 2, 3, 4]) == sum([1, 2, 3, 4]) / 4)   # True

# Program 7: One huge value
times = [1, 2, 3, 100]
print(statistics.mean(times), statistics.median(times))         # 26.5 2.5


# =====================================================
# Concept 19: reduce(), accumulate() and math.prod()
# =====================================================
"""
Definition:
reduce(function, items, start) combines all the items into ONE value
by calling function(result_so_far, next_item). reduce() lives in
functools. itertools.accumulate() gives ALL the running results.
math.prod() multiplies all the items (Python 3.8+).
Without a start value, reduce() on an empty list raises TypeError.
"""

# Program 1: A sum
print(reduce(lambda a, b: a + b, [1, 2, 3, 4]))         # 10

# Program 2: With a start value an empty list is fine
print(reduce(lambda a, b: a + b, [], 0))                # 0

# Program 3: Product
print(reduce(lambda a, b: a * b, [1, 2, 3, 4]), math.prod([1, 2, 3, 4]))       # 24 24

# Program 4: The biggest item
print(reduce(lambda a, b: a if a > b else b, [3, 9, 2]))        # 9

# Program 5: Running results
print(list(itertools.accumulate([1, 2, 3, 4])))                 # [1, 3, 6, 10]
print(list(itertools.accumulate([3, 1, 5, 2], max)))            # [3, 3, 5, 5]

# Program 6: An empty list without a start value
try:
    reduce(lambda a, b: a + b, [])
except TypeError as e:
    print(type(e).__name__)             # TypeError

# Program 7: Join strings
print(reduce(lambda a, b: a + "-" + b, ["a", "b", "c"]))        # a-b-c


# =====================================================
# Concept 20: iter() and next()
# =====================================================
"""
Definition:
iter(x) gives an iterator and next(it) gives the next item. Without
a second argument, next() raises StopIteration at the end; next(it,
default) returns the default instead. next() with a generator
expression is the neat way to get the FIRST match.
"""

# Program 1: Step by step
it = iter([1, 2])
print(next(it), next(it), next(it, "done"))             # 1 2 done

# Program 2: Every iter() call gives a new, independent iterator
nums = [10, 20]
it1 = iter(nums)
it2 = iter(nums)
print(next(it1), next(it2))             # 10 10

# Program 3: The first match, or None
print(next((n for n in [1, 3, 6, 8] if n % 2 == 0), None))      # 6
print(next((n for n in [1, 3] if n % 2 == 0), None))            # None

# Program 4: StopIteration without a default
it = iter([])
try:
    next(it)
except StopIteration:
    print("StopIteration: no more items")


# =====================================================
# Concept 21: print() with Lists
# =====================================================
"""
Definition:
print(my_list) shows brackets and commas. print(*my_list) spreads the
items as separate arguments, so you control sep= and end=.
", ".join(map(str, items)) builds a text yourself.
"""

# Program 1: sep
items = ["a", "b", "c"]
print(*items)                           # a b c
print(*items, sep=", ")                 # a, b, c
print(*items, sep="\n")                 # one item per line

# Program 2: end
for x in [1, 2, 3]:
    print(x, end=" ")
print()                                 # 1 2 3

# Program 3: str() and repr() of a list are the same
print(str(items) == repr(items))        # True

# Program 4: join with numbers
print(", ".join(map(str, [1, 2, 3])))   # 1, 2, 3

# Program 5: f-strings
print(f"{items}")                       # ['a', 'b', 'c']
print(f"{len(items)} items: {', '.join(items)}")        # 3 items: a, b, c


# =====================================================
# Concept 22: Never Hide a Built-in Name
# =====================================================
"""
Definition:
If you assign a value to a name like sum, max or len, your variable
HIDES the built-in function in that file. Calling it then gives
"'int' object is not callable". del removes your variable, and the
built-in works again. Use clear names: total, biggest, count, items.
"""

# Program 1: sum
sum = 10
try:
    sum([1, 2])
except TypeError as e:
    print("Error:", e)                  # 'int' object is not callable
del sum
print(sum([1, 2]))                      # 3

# Program 2: The typical case, the result is stored under the function's name
max = max([1, 2])
try:
    max([3, 4])
except TypeError as e:
    print("Error:", e)                  # 'int' object is not callable
del max
print(max([3, 4]))                      # 4

# Program 3: len
len = 3
try:
    len([1])
except TypeError as e:
    print("Error:", e)
del len
print(len([1]))                         # 1

# Program 4: Proof that the built-in is back
import builtins
print(sum is builtins.sum, max is builtins.max, len is builtins.len)    # True True True


# =====================================================
# Concept 23: Which Tool for Which Job?
# =====================================================
"""
Definition:
How many items?                 len(x)
Total of numbers?               sum(x)
Biggest / smallest?             max(x) / min(x), with key= for records
Count matches?                  sum(1 for ...) or x.count(value)
Does any / every item match?    any(...) / all(...)
New sorted copy?                sorted(x)
Index and item together?        enumerate(x)
Two lists together?             zip(a, b)
Change every item?              [f(x) for x in items] or map
Keep some items?                [x for x in items if ...] or filter
"""

nums = [4, 8, 15, 16, 23, 42]

# Program 1: A total
total = 0
for n in nums:
    total += n
print(total == sum(nums))               # True

# Program 2: The biggest item, three ways
biggest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
print(biggest == max(nums) == sorted(nums)[-1])         # True

# Program 3: Count matches
print(sum(1 for n in nums if n % 2 == 0), len([n for n in nums if n % 2 == 0]))        # 4 4
print(["a", "b", "a"].count("a"))       # 2 (count() is only for an exact value)

# Program 4: An average
print(sum(nums) / len(nums) == statistics.mean(nums))   # True

# Program 5: The longest word
print(max(["to", "list", "built-in"], key=len))         # built-in

# Program 6: A flag loop and any() give the same answer
found = False
for n in nums:
    if n > 40:
        found = True
        break
print(found == any(n > 40 for n in nums))               # True


# =====================================================
# Concept 24: Common Mistakes
# =====================================================
"""
Definition:
1) len(list) instead of len(my_list)
2) printing a map/filter/zip object and expecting the values
3) using an iterator a second time
4) max()/min() on an empty list
5) sum() or an average of an empty list
6) zip() dropping items silently
7) any() on text: "False" and "0" are TRUE (non-empty strings)
8) expecting sorted() to change the list
9) mixing numbers and text in min/max/sorted
10) map() with a function that needs a different number of arguments
"""

# Program 1: The type instead of the variable
my_list = [1, 2, 3]
try:
    len(list)
except TypeError as e:
    print("Error:", e)                  # object of type 'type' has no len()

# Program 2: An iterator object, not a list
m = map(int, ["1", "2"])
print(type(m).__name__, list(m))        # map [1, 2]  (print(m) alone would show <map object at 0x...>)

# Program 3: A second use of an iterator
z = zip([1], [2])
print(list(z), list(z))                 # [(1, 2)] []

# Program 4: Empty input, use default=
results = []
print(max(results, default=None))       # None

# Program 5: A safe average
print(sum(results) / len(results) if results else 0)    # 0

# Program 6: zip drops the extra items
names = ["a", "b", "c"]
scores = [1, 2]
print(list(zip(names, scores)))         # [('a', 1), ('b', 2)]  (c is missing)

# Program 7: Text is true
print(any(["False", "0"]))              # True
print(any([False, 0]))                  # False

# Program 8: sorted() and sort()
print(sorted([2, 1]), [2, 1].sort())    # [1, 2] None

# Program 9: Mixed types
print(max([10, "9"], key=str))          # 9 (compared as text: "9" is bigger than "10")
try:
    max([10, "9"])
except TypeError as e:
    print(type(e).__name__)             # TypeError

# Program 10: The wrong number of arguments
try:
    list(map(pow, [1, 2]))
except TypeError as e:
    print(type(e).__name__)             # TypeError


# =====================================================
# Concept 25: Built-in Functions in SQA Automation
# =====================================================
"""
Definition:
Test code summarizes results with sum/min/max, checks whole lists with
any/all, pairs expected and actual data with zip, numbers items with
enumerate, cleans page texts with map/filter, and checks the TYPE of an
API value with isinstance. A real Playwright call such as
page.locator("li").count() gives the same number as
len(page.locator("li").all_inner_texts()).
"""

results = [("login", "PASS", 2.3), ("cart", "FAIL", 5.1), ("search", "PASS", 1.4),
           ("payment", "FAIL", 8.7), ("logout", "PASS", 0.9)]

# Program 1: Duration summary
durations = [r[2] for r in results]
total = sum(durations)
fastest = min(results, key=lambda r: r[2])
slowest = max(results, key=lambda r: r[2])
print(f"Total {total:.1f}s | average {total / len(durations):.2f}s")    # Total 18.4s | average 3.68s
print("Fastest:", fastest[0], "| slowest:", slowest[0])                  # logout | payment

# Program 2: Pass rate
passed = sum(1 for _, status, _ in results if status == "PASS")
print(f"{passed}/{len(results)} passed = {passed / len(results):.0%}")   # 3/5 passed = 60%

# Program 3: Are all expected items on the page?
expected = ["Home", "Products", "Contact"]
actual = ["Contact", "Home", "Products", "Blog"]
print(all(item in actual for item in expected))         # True
print("missing:", [x for x in expected if x not in actual])             # []
print("extra:", [x for x in actual if x not in expected])               # ['Blog']

# Program 4: Price checks
prices = [9.99, 45.0, 199.0, 1234.5]
print(all(p > 0 for p in prices), any(p > 1000 for p in prices))        # True True
print(all(a <= b for a, b in zip(prices, prices[1:])))                  # True (ascending)
print(all(a <= b for a, b in zip([9.99, 199.0, 45.0], [199.0, 45.0])))  # False

# Program 5: Compare labels and find the lengths mismatch
expected_labels = ["Home", "Products", "Contact"]
actual_labels = ["Home", "Product"]
try:
    list(zip(expected_labels, actual_labels, strict=True))
except ValueError:
    print("FAIL: different number of labels")
print([(i, e, a) for i, (e, a) in enumerate(zip(expected_labels, actual_labels), start=1) if e != a])
# [(2, 'Products', 'Product')]

# Program 6: Page price texts into numbers
texts = ["$9.99", " $1,234.50", "45.00 "]
cleaned = list(map(lambda t: t.strip().replace("$", "").replace(",", ""), texts))
numbers = list(map(float, cleaned))
print(cleaned)                          # ['9.99', '1234.50', '45.00']
print(numbers, f"{sum(numbers):.2f}")   # [9.99, 1234.5, 45.0] 1289.49

# Program 7: The longest and the shortest error message
messages = ["Invalid password", "Email is required", "Timeout", "Session expired, please log in again"]
print(max(messages, key=len))           # Session expired, please log in again
print(min(messages, key=len))           # Timeout

# Program 8: Any failure? Everything passed?
statuses = [r[1] for r in results]
print(any(s == "FAIL" for s in statuses), all(s == "PASS" for s in statuses))   # True False
print("No failures:", not any(s == "FAIL" for s in statuses))                   # False

# Program 9: Response time statistics
times = [1.2, 0.8, 2.5, 1.9, 0.9, 3.1, 1.4, 2.2, 1.1, 5.0]
print(f"min {min(times)} | max {max(times)}")                   # min 0.8 | max 5.0
print(f"mean {statistics.mean(times):.2f} | median {statistics.median(times):.2f}")     # mean 2.01 | median 1.65
slow_line = sorted(times)[int(0.9 * (len(times) - 1))]
print("90 percent of the requests took", slow_line, "s or less")        # 3.1

# Program 10: Numbered results
names = ["login", "cart", "search"]
states = ["PASS", "FAIL", "PASS"]
for number, (name, state) in enumerate(zip(names, states), start=1):
    print(f"{number}. {name:<8}{state}")

# Program 11: Clean the texts of a page and drop the blank ones
raw = ["  Home ", "", "Products\xa0", "   ", "Contact\n"]
page_texts = list(filter(None, map(lambda t: " ".join(t.split()), raw)))
print(page_texts)                       # ['Home', 'Products', 'Contact']

# Program 12: Failures first, then by name
ordered = sorted(results, key=lambda r: (r[1], r[0]))
print([r[0] for r in ordered])          # ['cart', 'payment', 'login', 'logout', 'search']

# Program 13: Failures per run, running total and the worst run
failures_per_run = [3, 1, 4, 2]
print(list(itertools.accumulate(failures_per_run)))     # [3, 4, 8, 10]
print("worst run:", failures_per_run.index(max(failures_per_run)) + 1)      # 3

# Program 14: Check the type of an API value
responses = [{"items": [1, 2, 3]}, {"items": None}, {"items": "oops"}]
for response in responses:
    items = response["items"]
    if isinstance(items, list):
        print("OK, items:", len(items))
    else:
        print("FAIL: items should be a list, got", type(items).__name__)
# OK, items: 3 / FAIL ... NoneType / FAIL ... str

# Program 15: The number of elements on the page
found = ["Pen", "Notebook", "Bag"]
expected_count = 3
print("PASS" if len(found) == expected_count else f"FAIL: expected {expected_count}, found {len(found)}")

# Program 16: Items of several groups
groups = [["a", "b"], ["c"], ["d", "e", "f"]]
print(sum(map(len, groups)))            # 6

# Program 17: No failures means no slowest failure
failed_times = []
slowest_failure = max(failed_times, default=None)
print("No failures" if slowest_failure is None else slowest_failure)    # No failures

# Program 18: The first failed test
first_failure = next((r for r in results if r[1] == "FAIL"), None)
print(first_failure)                    # ('cart', 'FAIL', 5.1)