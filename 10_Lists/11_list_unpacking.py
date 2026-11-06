"""
====================================================
10_Lists / 11_list_unpacking.py
====================================================
Topic: Unpacking and Packing  (a, b = [1, 2]   *rest   *args   **kwargs)
====================================================
Notes before you run this file:
1) Unpacking = take the items of an iterable and give every item its own
   name. Packing = the opposite, several values are collected into ONE
   tuple or list.
2) The right side of "=" is calculated FIRST and completely. Then the
   names on the left are filled from left to right.
3) The number of names must match the number of items, unless one name
   has a star (*).
4) A star-name always gets a LIST, even if the source is a tuple or a string.
5) Error messages are shown as Python prints them. The wording can be a
   little different in other Python versions.
6) Functions appear only where the topic needs them (Concepts 9, 10, 13
   and 21). Everything else is plain code.
"""

from collections import namedtuple

# =====================================================
# Concept 1: What is Unpacking (and Packing)?
# =====================================================
"""
Definition:
Unpacking:  a, b, c = [10, 20, 30]   -> every item goes into its own name
Packing:    t = 1, 2, 3              -> the values are collected into a tuple
The two work together: a tuple is packed on the right, unpacked on the left.
"""

# Program 1: Unpack a list into three names
a, b, c = [10, 20, 30]
print(a, b, c)                          # 10 20 30

# Program 2: Packing, several values become one tuple
packed = 1, 2, 3
print(packed, type(packed).__name__)    # (1, 2, 3) tuple


# Program 3: Unpack the packed tuple again
x, y, z = packed
print(x + y + z)                        # 6


# Program 4: Names are easier to read than indexes
point = [3, 4]
print(point[0], point[1])               # 3 4
px, py = point
print(px, py)                           # 3 4


# =====================================================
# Concept 2: Unpacking Any Iterable
# =====================================================
"""
Definition:
Everything you can loop over can be unpacked: list, tuple, string,
range, dictionary (its KEYS), set, map(), generators and so on.
A number is not iterable, so it cannot be unpacked.
"""

# Program 1: Tuple, string and range
a, b, c = (1, 2, 3)
d, e, f = "xyz"
g, h, i = range(3)
print(a, b, c, d, e, f, g, h, i)        # 1 2 3 x y z 0 1 2

# Program 2: A dictionary gives its keys, map() and generators work too
key1, key2 = {"k": 1, "j": 2}
print(key1, key2)                       # k j
low, high = map(int, "3 9".split())
print(low, high)                        # 3 9
sq1, sq2 = (n * n for n in (2, 3))
print(sq1, sq2)                         # 4 9


# Program 3: A number cannot be unpacked
try:
    a, b = 5
except TypeError as e:
    print("Error:", e)                  # cannot unpack non-iterable int object


# =====================================================
# Concept 3: The Number of Names Must Match
# =====================================================
"""
Definition:
Too few or too many items raise a ValueError.
To unpack ONE item you need a comma after the name: a, = [5]
Without the comma, a = [5] is a normal assignment of the whole list.
"""

# Program 1: Too few items
try:
    a, b, c = [1, 2]
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 3, got 2)

# Program 2: Too many items
try:
    a, b = [1, 2, 3]
except ValueError as e:
    print("Error:", e)                  # too many values to unpack (expected 2)

# Program 3: One item, the comma makes the difference
(only,) = [5]
only2, = [6]
whole = [7]
print(only, only2, whole)               # 5 6 [7]

# Program 4: An empty list
try:
    nothing, = []
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 1, got 0)

# Program 5: Check the size first when you are not sure
data = [1, 2, 3]
if len(data) == 3:
    a, b, c = data
    print(a, b, c)                      # 1 2 3
else:
    print("unexpected size", len(data))


# =====================================================
# Concept 4: Swapping Values
# =====================================================
"""
Definition:
a, b = b, a swaps two values in one line, without a temporary variable.
Why it works: the right side is built FIRST as a tuple (b, a), and
only then it is unpacked into a and b.
Also works for list items: nums[i], nums[j] = nums[j], nums[i]
"""

# Program 1: Swap two names
a, b = 1, 2
a, b = b, a
print(a, b)                             # 2 1

# Program 2: What happens inside
a, b = 1, 2
pair = (b, a)                           # the right side is built first: (2, 1)
a, b = pair
print(a, b)                             # 2 1

# Program 3: The wrong swap (the first value is lost)
a, b = 1, 2
a = b
b = a
print(a, b)                             # 2 2

# Program 4: Rotate three values
a, b, c = 1, 2, 3
a, b, c = b, c, a
print(a, b, c)                          # 2 3 1

# Program 5: Swap items of a list
nums = [1, 2, 3, 4]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)                             # [4, 2, 3, 1]

# Program 6: Reverse a list in place with swaps
nums = [1, 2, 3, 4, 5]
left, right = 0, len(nums) - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
print(nums)                             # [5, 4, 3, 2, 1]

# Program 7: One bubble sort pass
nums = [3, 1, 2]
for j in range(len(nums) - 1):
    if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)                             # [1, 2, 3]

# Program 8: Fibonacci and GCD use the same idea
a, b = 0, 1
for _ in range(8):
    print(a, end=" ")
    a, b = b, a + b
print()                                 # 0 1 1 2 3 5 8 13
a, b = 48, 18
while b:
    a, b = b, a % b
print(a)                                # 6


# =====================================================
# Concept 5: Star Unpacking  (*rest)
# =====================================================
"""
Definition:
A name with a star collects ALL the items that are left over. The
star-name is always a NEW LIST, it can be empty, and only ONE star is
allowed in one assignment. The star can be at the start, in the
middle or at the end.
"""

# Program 1: Start, end and middle
numbers = [1, 2, 3, 4, 5]
first, *rest = numbers
print(first, rest)                      # 1 [2, 3, 4, 5]
*init, last = numbers
print(init, last)                       # [1, 2, 3, 4] 5
first, *middle, last = numbers
print(first, middle, last)              # 1 [2, 3, 4] 5

# Program 2: The star part can be empty
a, *b = [1]
print(a, b)                             # 1 []
a, *b, c = [1, 2]
print(a, b, c)                          # 1 [] 2

# Program 3: The star-name is always a list
first, *rest = (1, 2, 3)
print(rest, type(rest).__name__)        # [2, 3] list
head, *tail = "hello"
print(head, tail)                       # h ['e', 'l', 'l', 'o']
print("".join(tail))                    # ello

# Program 4: More names around the star
a, b, *c = [1, 2, 3, 4]
print(a, b, c)                          # 1 2 [3, 4]
a, *b, c, d = [1, 2, 3, 4, 5]
print(a, b, c, d)                       # 1 [2, 3] 4 5

# Program 5: The names without a star still need their items
try:
    a, b, *c = [1]
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected at least 2, got 1)

# Program 6: Only one star, and a lonely star needs a comma
try:
    exec("a, *b, *c = [1, 2, 3]")
except SyntaxError as e:
    print("SyntaxError:", e.msg)        # multiple starred expressions in assignment
try:
    exec("*a = [1, 2]")
except SyntaxError as e:
    print("SyntaxError:", e.msg)        # starred assignment target must be in a list or tuple
*a, = [1, 2]
print(a)                                # [1, 2]

# Program 7: The star-name is a new list, the source is not touched
nums = [1, 2, 3]
first, *rest = nums
rest.append(99)
print(nums, rest)                       # [1, 2, 3] [2, 3, 99]


# =====================================================
# Concept 6: Ignoring Values with _
# =====================================================
"""
Definition:
By habit, the name _ means "I do not need this value". It is a
normal variable, Python does not treat it in a special way inside a
file. _ can be used many times, it keeps the LAST value. *_ ignores
a whole group of items.
"""

# Program 1: Ignore one value
name, _, city = ["Ali", 25, "Lahore"]
print(name, city)                       # Ali Lahore

# Program 2: Ignore the rest, or the start
first, *_ = [1, 2, 3]
*_, last = [1, 2, 3]
print(first, last)                      # 1 3

# Program 3: _ is only a normal name
_, _, third = (1, 2, 3)
print(third, _)                         # 3 2 (_ keeps the last value it got)

# Program 4: In loops
for _, score in [("Ali", 90), ("Sara", 85)]:
    print(score)                        # 90 then 85
for _ in range(2):
    print("hello")                      # printed twice, the counter is not needed


# =====================================================
# Concept 7: Unpacking in for Loops
# =====================================================
"""
Definition:
The loop variable can be several names. Every round unpacks the
current item. This is the normal way to loop over enumerate(), zip(),
dict.items() and lists of tuples or lists. Every item must have the
right size.
"""

# Program 1: enumerate()
for i, name in enumerate(["Ali", "Sara"], start=1):
    print(i, name)                      # 1 Ali   2 Sara

# Program 2: zip()
names = ["Ali", "Sara", "Bilal"]
scores = [90, 85, 78]
for name, score in zip(names, scores):
    print(name, score)

# Program 3: dict.items()
marks = {"Ali": 90, "Sara": 85}
for name, mark in marks.items():
    print(f"{name} -> {mark}")

# Program 4: enumerate() and zip() together
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name} scored {score}")

# Program 5: A star in the loop line
for first, *rest in [[1, 2, 3], [4, 5], [6]]:
    print(first, rest)                  # 1 [2, 3]   4 [5]   6 []

# Program 6: Strings are unpacked too
for a, b in ["ab", "cd"]:
    print(b, a)                         # b a   d c

# Program 7: Items of the wrong size
try:
    for a, b in [[1, 2], [3]]:
        print(a, b)
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 2, got 1)


# =====================================================
# Concept 8: Nested Unpacking
# =====================================================
"""
Definition:
Brackets on the left side unpack items that are themselves iterables:
(a, b), (c, d) = [[1, 2], [3, 4]]
A star can be used inside the inner brackets too.
"""

# Program 1: Two levels
(a, b), (c, d) = [[1, 2], [3, 4]]
print(a, b, c, d)                       # 1 2 3 4

# Program 2: A name and a pair
name, (x, y) = "P", (3, 4)
print(name, x, y)                       # P 3 4

# Program 3: A star inside
(first, *rest), last = [[1, 2, 3], 9]
print(first, rest, last)                # 1 [2, 3] 9
a, [b, *c] = 1, [2, 3, 4]
print(a, b, c)                          # 1 2 [3, 4]

# Program 4: Three levels
(a, b), (c, (d, e)) = [[1, 2], [3, [4, 5]]]
print(a, b, c, d, e)                    # 1 2 3 4 5

# Program 5: A wrong inner size
try:
    (a, b), c = [[1], 2]
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 2, got 1)

# Program 6: In a loop
records = [("Ali", (25, "Lahore")), ("Sara", (22, "Karachi"))]
for name, (age, city) in records:
    print(name, age, city)


# =====================================================
# Concept 9: Unpacking in Function Calls  (* and **)
# =====================================================
"""
Definition:
In a CALL, *iterable spreads the items as separate positional
arguments, and **dictionary spreads the pairs as keyword arguments.
Several of them can be mixed in one call. The names must match the
parameters of the function.
"""

# Program 1: A list as arguments
def add3(a, b, c):
    return a + b + c

args = [1, 2, 3]
print(add3(*args))                      # 6
print(add3(1, *[2, 3]))                 # 6
print(add3(*[1], *[2, 3]))              # 6

# Program 2: A dictionary as keyword arguments
options = {"a": 1, "b": 2, "c": 3}
print(add3(**options))                  # 6
print(add3(1, **{"b": 2, "c": 3}))      # 6

# Program 3: Built-in functions
print(*[1, 2, 3])                       # 1 2 3
print(*[1, 2, 3], sep=" - ")            # 1 - 2 - 3
print(list(range(*[1, 10, 3])))         # [1, 4, 7]
print(*"abc")                           # a b c
print(max(*[3, 9, 2]), max([3, 9, 2]))  # 9 9

# Program 4: Errors
try:
    add3(*[1, 2])
except TypeError as e:
    print("Error:", e)                  # add3() missing 1 required positional argument: 'c'
try:
    add3(**{"a": 1, "b": 2, "c": 3, "x": 4})
except TypeError as e:
    print("Error:", e)                  # add3() got an unexpected keyword argument 'x'
try:
    print(*5)
except TypeError:
    print("TypeError: only an iterable can follow *")


# =====================================================
# Concept 10: Packing in Function Definitions  (*args, **kwargs)
# =====================================================
"""
Definition:
In a function DEFINITION the stars work the other way round:
*args    collects extra positional arguments into a TUPLE
**kwargs collects extra keyword arguments into a DICTIONARY
Parameters after a lone * can only be given by keyword.
Memory trick: in def = PACK, in a call = UNPACK.
"""

# Program 1: *numbers is a tuple
def total(*numbers):
    return numbers, sum(numbers)

print(total(1, 2, 3))                   # ((1, 2, 3), 6)
print(total())                          # ((), 0)

# Program 2: **options is a dictionary
def show(**options):
    return options

print(show(a=1, b=2))                   # {'a': 1, 'b': 2}

# Program 3: All kinds together
def mix(first, *rest, **extra):
    return first, rest, extra

print(mix(1, 2, 3, x=4))                # (1, (2, 3), {'x': 4})

# Program 4: Pass everything on to another function
def wrapper(*args, **kwargs):
    return add3(*args, **kwargs)

print(wrapper(1, 2, c=3))               # 6

# Program 5: Keyword-only parameters
def connect(host, *, port=80):
    return f"{host}:{port}"

print(connect("localhost", port=8080))  # localhost:8080
try:
    connect("localhost", 8080)
except TypeError as e:
    print("Error:", e)                  # connect() takes 1 positional argument but 2 were given


# =====================================================
# Concept 11: Building New Lists with *
# =====================================================
"""
Definition:
Inside [ ] ( ) { } a star spreads the items of any iterable:
[*a, *b]       joins lists (and any other iterables)
[0, *a, 99]    mixes single values and groups
The result is a NEW object. The items inside are shared with the
source (a shallow copy).
"""

# Program 1: Join lists
a = [1, 2]
b = [3, 4]
print([*a, *b])                         # [1, 2, 3, 4]
print([0, *a, 99, *b])                  # [0, 1, 2, 99, 3, 4]

# Program 2: Any iterable can be spread
print([*"ab", *range(2)])               # ['a', 'b', 0, 1]
print([*{"x": 1, "y": 2}])              # ['x', 'y']
print([*a, *"cd"])                      # [1, 2, 'c', 'd']
try:
    a + "cd"
except TypeError as e:
    print("Error:", e)                  # can only concatenate list (not "str") to list

# Program 3: Tuples and sets
print((*[1, 2], *[3]))                  # (1, 2, 3)
print(sorted({*[1, 2], *[2, 3]}))       # [1, 2, 3]

# Program 4: Copy, insert and rotate
nums = [1, 2, 3]
dup = [*nums]
print(dup == nums, dup is nums)         # True False
print([*nums[:1], "new", *nums[1:]])    # [1, 'new', 2, 3]
print([*nums[1:], nums[0]])             # [2, 3, 1]

# Program 5: The items are shared (shallow)
rows = [[1], [2]]
dup = [*rows]
dup[0].append("!")
print(rows)                             # [[1, '!'], [2]]


# =====================================================
# Concept 12: Dictionaries and Unpacking
# =====================================================
"""
Definition:
Unpacking a dictionary directly gives its KEYS. Use .values() or
.items() for the rest. {**d1, **d2} merges dictionaries, and when a
key repeats the LATER one wins. (d1 | d2 does the same in Python 3.9+.)
"""

d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}

# Program 1: Keys, values and pairs
k1, k2 = d1
print(k1, k2)                           # a b
v1, v2 = d1.values()
print(v1, v2)                           # 1 2
(k1, v1), (k2, v2) = d1.items()
print(k1, v1, k2, v2)                   # a 1 b 2

# Program 2: Merge
print({**d1, **d2})                     # {'a': 1, 'b': 20, 'c': 30}
print((d1 | d2) == {**d1, **d2})        # True

# Program 3: The order decides who wins
print({**d1, "a": 100})                 # {'a': 100, 'b': 2}
print({"a": 100, **d1})                 # {'a': 1, 'b': 2}

# Program 4: Add a key without changing the original
d3 = {**d1, "z": 0}
print(d1, d3)                           # {'a': 1, 'b': 2} {'a': 1, 'b': 2, 'z': 0}


# =====================================================
# Concept 13: Returning and Unpacking Several Values
# =====================================================
"""
Definition:
"return a, b" packs the values into a TUPLE, and the caller unpacks
it: x, y = function(). Without unpacking you get the whole tuple.
A namedtuple gives names to the values, so the result can be read
both ways: by unpacking and by name.
"""

# Program 1: A function with two results
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 4])
print(low, high)                        # 1 9
result = min_max([3, 1, 9, 4])
print(result, type(result).__name__)    # (1, 9) tuple

# Program 2: divmod() returns two values
quotient, remainder = divmod(17, 5)
print(quotient, remainder)              # 3 2
minutes, seconds = divmod(125, 60)
print(f"{minutes:02}:{seconds:02}")     # 02:05

# Program 3: Three results and a wrong number of names
def stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lo, hi, avg = stats([2, 4, 6])
print(lo, hi, avg)                      # 2 6 4.0
try:
    a, b = stats([2, 4, 6])
except ValueError as e:
    print("Error:", e)                  # too many values to unpack (expected 2)

# Program 4: Take only what you need
lo, *_ = stats([2, 4, 6])
print(lo)                               # 2

# Program 5: namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
x, y = p
print(x, y, p.x, p.y)                   # 3 4 3 4


# =====================================================
# Concept 14: Unpacking Text with split() and partition()
# =====================================================
"""
Definition:
split() gives a list, so you can unpack it straight away. The pieces
are STRINGS, convert them to numbers yourself. If the number of
pieces can change, use a star or partition() (always exactly 3 parts).
"""

# Program 1: Split and unpack
name, age = "Ali,25".split(",")
print(name, age, type(age).__name__)    # Ali 25 str
age = int(age)
print(age + 1)                          # 26

# Program 2: More examples
first, last = "Ali Khan".split()
host, port = "localhost:8080".split(":")
year, month, day = map(int, "2026-10-17".split("-"))
print(first, last, host, port, year, month, day)

# Program 3: maxsplit and partition
head, tail = "a/b/c".split("/", 1)
print(head, tail)                       # a b/c
user, _, domain = "ali@example.com".partition("@")
print(user, domain)                     # ali example.com
key, _, value = "mode=fast".partition("=")
print(key, value)                       # mode fast

# Program 4: The folders and the file name of a path
*folders, filename = "C:/data/reports/final.xlsx".split("/")
print(folders, filename)                # ['C:', 'data', 'reports'] final.xlsx

# Program 5: A wrong number of pieces
try:
    first, last = "Ali Ahmed Khan".split()
except ValueError as e:
    print("Error:", e)                  # too many values to unpack (expected 2)
first, *others = "Ali Ahmed Khan".split()
print(first, others)                    # Ali ['Ahmed', 'Khan']


# =====================================================
# Concept 15: Unpacking in Comprehensions
# =====================================================
"""
Definition:
The "for" part of a comprehension can unpack every item, exactly
like a for loop. This is the neat way to work with lists of pairs,
rows and dictionary items.
"""

# Program 1: Pairs
pairs = [(1, 2), (3, 4)]
print([a + b for a, b in pairs])        # [3, 7]

# Program 2: A dictionary from pairs
print({name: score for name, score in [("Ali", 90), ("Sara", 85)]})     # {'Ali': 90, 'Sara': 85}

# Program 3: A star in a comprehension
print([first for first, *rest in [[1, 2, 3], [4, 5]]])      # [1, 4]

# Program 4: Filter with unpacked names
points = [(1, 5), (2, -3), (4, 7)]
print([x for x, y in points if y > 0])  # [1, 4]

# Program 5: enumerate() inside
print([f"{i}:{c}" for i, c in enumerate("ab")])     # ['0:a', '1:b']


# =====================================================
# Concept 16: zip(*) (Unzip and Transpose)
# =====================================================
"""
Definition:
zip(*pairs) is the opposite of zip(): it splits a list of pairs into
separate sequences. The same trick turns the rows of a matrix into
columns. The results are tuples. Careful: zip(*[]) gives NOTHING, so
unpacking it into names fails.
"""

# Program 1: Unzip a list of pairs
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(letters, numbers)                 # ('a', 'b', 'c') (1, 2, 3)

# Program 2: Get lists instead of tuples
letters, numbers = map(list, zip(*pairs))
print(letters, numbers)                 # ['a', 'b', 'c'] [1, 2, 3]

# Program 3: Rows become columns
m = [[1, 2, 3], [4, 5, 6]]
print(list(zip(*m)))                    # [(1, 4), (2, 5), (3, 6)]
for col in zip(*m):
    print(sum(col))                     # 5 7 9

# Program 4: The first row and the others
first_row, *other_rows = m
print(first_row, other_rows)            # [1, 2, 3] [[4, 5, 6]]

# Program 5: The empty trap
try:
    names, scores = zip(*[])
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 2, got 0)


# =====================================================
# Concept 17: Other Targets and Chained Assignment
# =====================================================
"""
Definition:
The left side can be list items, dictionary keys and slices, not only
names. Chained assignment (a = b = value) gives ONE object to several
names: harmless for numbers, a trap for lists.
Targets are filled from left to right, and an index is calculated at
the moment its turn comes.
"""

# Program 1: List items and dictionary keys
nums = [1, 2, 3]
nums[0], nums[2] = nums[2], nums[0]
print(nums)                             # [3, 2, 1]
d = {}
d["x"], d["y"] = 1, 2
print(d)                                # {'x': 1, 'y': 2}

# Program 2: Chained assignment with numbers is fine
x = y = 0
x += 1
print(x, y)                             # 1 0

# Program 3: Chained assignment with lists shares ONE list
a = b = []
a.append(1)
print(b, a is b)                        # [1] True
c, d = [], []
c.append(1)
print(d, c is d)                        # [] False

# Program 4: Order of the targets
i = 0
nums = [10, 20, 30]
i, nums[i] = 1, 99                      # first i = 1, then nums[i] means nums[1]
print(i, nums)                          # 1 [10, 99, 30]
i = 0
nums = [10, 20, 30]
nums[i], i = 99, 1                      # first nums[0] = 99, then i = 1
print(i, nums)                          # 1 [99, 20, 30]

# Program 5: Slices as targets (together with a star)
nums = [1, 2, 3, 4]
nums[:2], nums[2:] = [9, 9], [8, 8]
print(nums)                             # [9, 9, 8, 8]


# =====================================================
# Concept 18: Unpacking is Shallow
# =====================================================
"""
Definition:
Unpacking never copies the items. The names point to the SAME
objects that are inside the list. Changing a mutable item through
its name changes it inside the list too.
"""

# Program 1: Names for the rows
rows = [[1, 2], [3, 4]]
r1, r2 = rows
r1.append(9)
print(rows)                             # [[1, 2, 9], [3, 4]]
print(r1 is rows[0])                    # True

# Program 2: Rebinding a name changes nothing in the list
r1 = ["new"]
print(rows[0])                          # [1, 2, 9]

# Program 3: The star-name is a new list, its items are not copied
data = [[1], [2], [3]]
first, *rest = data
rest[0].append("!")
print(data)                             # [[1], [2, '!'], [3]]
rest.append([4])
print(len(data), len(rest))             # 3 3

# Program 4: Numbers and strings are safe, they cannot change
a, b = 1, "x"
a += 1
print(a, b)                             # 2 x


# =====================================================
# Concept 19: Names Instead of Indexes (Readability)
# =====================================================
"""
Definition:
row[0], row[1], row[2] hide the meaning of the data. Unpacking into
clear names makes the code self-explaining and fails loudly when a
row has the wrong size, instead of reading the wrong column quietly.
"""

row = ["Ali", 25, "Lahore"]

# Program 1: Hard to read
print(row[0], "is", row[1], "years old and lives in", row[2])

# Program 2: Easy to read
name, age, city = row
print(name, "is", age, "years old and lives in", city)

# Program 3: A wrong row is found at once
try:
    name, age, city = ["Sara", 22]
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 3, got 2)
print(["Sara", 22][2:3])                # [] (an index or slice would not complain loudly)


# =====================================================
# Concept 20: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with unpacking:
1) a different number of names and items
2) forgetting the comma for one item: a = [5] instead of a, = [5]
3) a wrong swap with two assignments
4) a = b = [] shares one list
5) expecting values from a dictionary, but getting keys
6) forgetting that split() gives strings
7) unpacking overwrites names that already exist
8) zip(*empty_list) cannot be unpacked
"""

# Program 1: One name too many
try:
    a, b, c = "ab"
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 3, got 2)

# Program 2: The comma
a = [5]
b, = [5]
print(a, b)                             # [5] 5

# Program 3: The wrong swap
a, b = 1, 2
a = b
b = a
print(a, b)                             # 2 2

# Program 4: One list for two names
a = b = []
a.append("x")
print(b)                                # ['x']

# Program 5: Keys, not values
x, y = {"a": 1, "b": 2}
print(x, y)                             # a b

# Program 6: Strings, not numbers
a, b = "3 4".split()
print(a + b)                            # 34
a, b = map(int, "3 4".split())
print(a + b)                            # 7

# Program 7: A name that already exists is overwritten silently
x = "important"
x, y = 1, 2
print(x)                                # 1

# Program 8: An empty list into zip(*)
data = []
if data:
    names, scores = zip(*data)
else:
    print("no data, nothing to unzip")


# =====================================================
# Concept 21: Unpacking in SQA Automation
# =====================================================
"""
Definition:
Test code is full of small records: (name, status, time) results,
expected/actual pairs, rows with a header, log lines, test ids, URLs and
data driven test cases. Unpacking gives every value a clear name and
stops a wrongly shaped row at once. A real Playwright call such as
page.viewport_size is a dictionary with "width" and "height", but a
plain (width, height) tuple works the same way.
"""

# Program 1: Results in a loop
results = [("login", "PASS", 2.3), ("cart", "FAIL", 5.1), ("search", "PASS", 1.4)]
for name, status, seconds in results:
    print(f"{name:<8}{status:<6}{seconds:>5.1f}s")

# Program 2: The header and the rows of a table
table = [["Name", "Status"], ["Ali", "Active"], ["Sara", "Inactive"]]
header, *rows = table
print(header, len(rows))                # ['Name', 'Status'] 2
for name, status in rows:
    print(f"{name} is {status}")

# Program 3: Expected against actual, with the position in the message
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Product", "Contact"]
for position, (e, a) in enumerate(zip(expected, actual), start=1):
    if e != a:
        print(f"item {position}: expected {e!r}, got {a!r}")    # item 2

# Program 4: Parse a log line
line = "2026-10-17 10:00:05 [ERROR] Database connection failed"
date, time_text, level, message = line.split(maxsplit=3)
print(date, "|", time_text, "|", level, "|", message)

# Program 5: Parse a test case id
prefix, module, number = "TC_LOGIN_001".split("_")
print(prefix, module, int(number))      # TC LOGIN 1

# Program 6: Split a URL
url = "https://example.com/shop/item/42"
scheme, rest = url.split("://")
host, _, path = rest.partition("/")
print(scheme, host, path)               # https example.com shop/item/42
*sections, item_id = path.split("/")
print(sections, item_id)                # ['shop', 'item'] 42

# Program 7: Data driven test cases (the "application" is a small dictionary here)
valid_users = {"admin": "Admin@123"}
login_cases = [
    ("admin", "Admin@123", True),
    ("admin", "wrong", False),
    ("", "Admin@123", False),
]
for username, password, expected_ok in login_cases:
    actual_ok = valid_users.get(username) == password
    print("PASS" if actual_ok == expected_ok else "FAIL", f"user={username!r:<8} expected={expected_ok}")

# Program 8: The fastest and the slowest test
durations = [2.3, 5.1, 0.9, 1.4]
fastest, *_, slowest = sorted(durations)
print(fastest, slowest)                 # 0.9 5.1

# Program 9: The first and the last log line
log_lines = ["start", "[PASS] login", "[FAIL] cart", "end"]
first_line, *_, last_line = log_lines
print(first_line, "|", last_line)       # start | end

# Program 10: Seconds into hours:minutes:seconds
hours, rest_seconds = divmod(3725, 3600)
minutes, seconds = divmod(rest_seconds, 60)
print(f"{hours:02}:{minutes:02}:{seconds:02}")      # 01:02:05

# Program 11: Merge a base test configuration with the settings of one run
base_config = {"browser": "chromium", "headless": True, "timeout": 30}
run_config = {"browser": "firefox", "slow_mo": 100}
config = {**base_config, **run_config}
print(config)           # {'browser': 'firefox', 'headless': True, 'timeout': 30, 'slow_mo': 100}
print(base_config)      # unchanged

# Program 12: Combine lists of tests
smoke = ["login", "search"]
regression = ["cart", "payment"]
all_tests = [*smoke, *regression, "logout"]
print(all_tests)                        # ['login', 'search', 'cart', 'payment', 'logout']

# Program 13: A value that itself contains "=" (the token below is fake)
line = "token=abc123=="
key, *value_parts = line.split("=")
value = "=".join(value_parts)
print(key, value)                       # token abc123==

# Program 14: A viewport size
viewport = (1280, 720)
width, height = viewport
print(f"{width}x{height}")              # 1280x720

# Program 15: A row that may have extra cells
for row in (["Ali", "Active"], ["Sara", "Inactive", "note 1", "note 2"]):
    name, status, *extra = row
    print(name, status, extra)          # Ali Active []   Sara Inactive ['note 1', 'note 2']

# Program 16: Count before and after an action
before, after = len(["Pen", "Notebook"]), len(["Pen", "Notebook", "Bag"])
print("PASS" if after == before + 1 else "FAIL", "- exactly one item should be added")

# Program 17: Check the size of a row before unpacking it
for row in (["Ali", "ali@example.com", "Active"], ["Sara", "sara@example.com"]):
    if len(row) != 3:
        print("FAIL: a row has", len(row), "cells instead of 3:", row)
        continue
    name, email, status = row
    print("OK:", name, status)











