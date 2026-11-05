"""
====================================================
10_Lists / 10_list_copying_references.py
====================================================
Topic: References, Copying, Mutability and Memory
====================================================
Notes before you run this file:
1) A variable is not a box that holds a list. It is a NAME that
   points to a list object. Two names can point to the SAME object.
2) "b = a" never copies anything. It only gives the object a second name.
3) id() numbers are different on every computer and every run, so we
   compare them (== or is) and never rely on the printed numbers.
4) Results marked "typical" are CPython details (small number cache,
   string sharing). Do not build real logic on them.
5) Do NOT name a variable "copy" in this file, it would hide the
   copy module (Concept 21 shows this mistake on purpose).
6) Functions are used only in Concepts 12, 13 and 22, because passing
   a list to a function is part of the topic. Everything else is plain code.
"""

import copy
import sys
import time


# =====================================================
# Concept 1: Names and Objects (References)
# =====================================================
"""
Definition:
A list is an OBJECT stored in memory. A variable is a NAME (a label)
that points to that object. "a = [1, 2, 3]" means: create the list,
then stick the label "a" on it. A second label can be stuck on the
same list. When the last label is removed, the object is freed.
"""

# Program 1: Two names, one object
a = [1, 2, 3]
b = a
print(a is b)                           # True
print(id(a) == id(b))                   # True

# Program 2: A change through one name is seen through the other
a = [1]
b = a
a.append(2)
print(b)                                # [1, 2]

# Program 3: The object lives on while at least one name points to it
x = [1, 2]
y = x
del x                                   # removes the NAME x, not the list
print(y)                                # [1, 2]
try:
    print(x)
except NameError as e:
    print("Error:", e)                  # name 'x' is not defined


# =====================================================
# Concept 2: Assignment Never Copies
# =====================================================
"""
Definition:
b = a copies nothing, not even for a huge list. It is instant and
uses no extra memory, because only a new name is created.
This is why a "backup" made with = is not a backup.
"""

# Program 1: Both names show the change
a = [1, 2]
b = a
b.append(3)
print(a, b)                             # [1, 2, 3] [1, 2, 3]

# Program 2: A fake backup
settings = ["dark", "english"]
backup = settings
settings.clear()
print(backup)                           # [] (the backup is gone too)

# Program 3: Count the different objects behind four names
a = [1]
b = a
c = a.copy()
d = c
print(len({id(a), id(b), id(c), id(d)}))        # 2 (a and b are one list, c and d are another)


# =====================================================
# Concept 3: id(), is and ==
# =====================================================
"""
Definition:
id(obj)   the identity (address) of an object while it is alive
a is b    True if both names point to the SAME object
a == b    True if the VALUES are equal (the objects may differ)
Equal lists can be different objects. The same object is always equal to itself.
"""

# Program 1: Equal but not the same
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)           # True False True

# Program 2: id() agrees with is
print(id(a) == id(c), id(a) == id(b))   # True False

# Program 3: is not
print(a is not b)                       # True

# Program 4: Nested lists, == looks inside, is does not
print([[1], [2]] == [[1], [2]])         # True
x = [[1], [2]]
y = [[1], [2]]
print(x is y, x[0] is y[0])             # False False

# Program 5: id() is an integer
print(type(id(a)).__name__)             # int


# =====================================================
# Concept 4: Aliasing (a Change Shows Through Every Name)
# =====================================================
"""
Definition:
Aliasing means several names for one object. Changing the OBJECT
(append, sort, item assignment, +=, slice assignment) is seen through
all names. Giving a name a NEW object (a = [...] or a = a + [...])
moves only that one name.
"""

# Program 1: Item assignment and methods change the shared object
a = [3, 1, 2]
b = a
a[0] = 99
a.append(4)
a.sort()
print(b)                                # [1, 2, 4, 99]

# Program 2: Rebinding moves only one name
a = [1, 2]
b = a
a = [9, 9]
print(a, b, a is b)                     # [9, 9] [1, 2] False

# Program 3: += changes the object, a = a + [...] makes a new one
a = [1]
b = a
a += [2]
print(b)                                # [1, 2]
a = a + [3]
print(a, b)                             # [1, 2, 3] [1, 2]

# Program 4: clear() vs = []
a = [1, 2]
b = a
a.clear()
print(b)                                # []
a = [1, 2]
b = a
a = []
print(b)                                # [1, 2]

# Program 5: Slice assignment keeps the same object
a = [1, 2, 3]
b = a
a[:] = [7]
print(b)                                # [7]


# =====================================================
# Concept 5: Mutable vs Immutable
# =====================================================
"""
Definition:
Mutable types can be changed in place: list, dict, set.
Immutable types never change: int, float, str, tuple, bool, None.
For an immutable object, an "update" (x += 1) creates a NEW object,
so another name is never affected. For a mutable one (l += [2]) the
same object is changed, so every name sees it.
"""

# Program 1: Numbers
x = 5
y = x
x += 1
print(x, y)                             # 6 5

# Program 2: Strings
s = "ab"
t = s
s += "c"
print(s, t)                             # abc ab

# Program 3: Tuples
t = (1, 2)
u = t
t += (3,)
print(t, u)                             # (1, 2, 3) (1, 2)

# Program 4: Lists (the difference)
l = [1]
m = l
l += [2]
print(l, m)                             # [1, 2] [1, 2]

# Program 5: hash() works only for immutable objects
for obj in (1, 2.5, "a", (1,), True, None, [1], {1}, {"a": 1}):
    try:
        hash(obj)
        kind = "hashable (immutable)"
    except TypeError:
        kind = "unhashable (mutable)"
    print(f"{type(obj).__name__:<9}{kind}")


# =====================================================
# Concept 6: Why is Is Not for Comparing Values
# =====================================================
"""
Definition:
CPython reuses some immutable objects (small integers from -5 to 256,
some strings), so "is" can look like it compares values. This is an
internal optimization, not a rule. Compare values with ==.
Use "is" only for None (and True/False).
Writing  x is 256  with a literal even gives a SyntaxWarning.
"""

# Program 1: Small and big integers (created while the program runs)
a = int("256")
b = int("256")
print(a == b, a is b)                   # True True  (typical, small number cache)
c = int("1000")
d = int("1000")
print(c == d, c is d)                   # True False (typical)

# Program 2: Strings built while the program runs
s1 = "".join(["he", "llo"])
s2 = "".join(["he", "llo"])
print(s1 == s2, s1 is s2)               # True False (typical)

# Program 3: Lists are never shared like this
print([] is [], [1] is [1])             # False False

# Program 4: The right use of is
result = None
print(result is None)                   # True
flag = True
print(flag is True)                     # True


# =====================================================
# Concept 7: Shallow Copy (Five Ways)
# =====================================================
"""
Definition:
A shallow copy creates a NEW outer list with the SAME items inside.
Ways to make one:
a.copy()   a[:]   list(a)   copy.copy(a)   [*a]   [x for x in a]
For a list of numbers, strings or tuples this is a full, safe copy,
because those items can never change.
"""

# Program 1: Five ways, one result
a = [1, 2, 3]
duplicates = [a.copy(), a[:], list(a), copy.copy(a), [*a], [x for x in a]]
print(all(d == a and d is not a for d in duplicates))   # True

# Program 2: The copy is independent
b = a.copy()
b[0] = 100
a.append(4)
print(a, b)                             # [1, 2, 3, 4] [100, 2, 3]

# Program 3: The items are the very same objects
words = ["x", "y"]
dup = words.copy()
print(all(p is q for p, q in zip(words, dup)))          # True

# Program 4: Empty lists are copied too
e = []
print(e.copy() is e, e.copy() == e)     # False True


# =====================================================
# Concept 8: The Shallow Copy Trap (Nested Lists)
# =====================================================
"""
Definition:
A shallow copy copies only the OUTER list. If an item is itself a
list (or dict), the copy holds the SAME inner object. Changing the
inner object through the copy changes the original too.
Replacing a whole item in the copy is safe, changing INSIDE it is not.
Picture:   original ---> [ row0, row1 ]
           shallow  ---> [ row0, row1 ]     (the same two rows)
"""

# Program 1: A change inside a row is seen by both
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[0].append(99)
print(original)                         # [[1, 2, 99], [3, 4]]
print(shallow)                          # [[1, 2, 99], [3, 4]]

# Program 2: Who is shared?
print(shallow is original)              # False (outer lists are different)
print(shallow[0] is original[0])        # True  (rows are shared)

# Program 3: Replacing a whole row is safe
original = [[1, 2], [3, 4]]
shallow = original.copy()
shallow[1] = ["new"]
print(original[1], shallow[1])          # [3, 4] ['new']

# Program 4: Dictionaries inside a list behave the same
users = [{"name": "Ali"}]
dup = users.copy()
dup[0]["name"] = "CHANGED"
print(users)                            # [{'name': 'CHANGED'}]


# =====================================================
# Concept 9: Deep Copy
# =====================================================
"""
Definition:
copy.deepcopy(x) copies the outer list AND everything inside it,
level after level. Immutable items (numbers, strings) are not
copied, they are shared, which is safe because they cannot change.
deepcopy also remembers what it already copied, so an object that
appears twice in the original appears twice (as one object) in the
copy, and a list that contains itself does not loop forever.
"""

# Program 1: A change in the copy does not reach the original
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
deep[0].append(99)
print(original)                         # [[1, 2], [3, 4]]
print(deep)                             # [[1, 2, 99], [3, 4]]

# Program 2: Rows are new objects, numbers are still shared
print(deep[1] is original[1])           # False
print(deep[1][0] is original[1][0])     # True

# Program 3: Any depth
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
deep_cube = copy.deepcopy(cube)
deep_cube[0][0].append("x")
print(cube[0][0], deep_cube[0][0])      # [1, 2] [1, 2, 'x']

# Program 4: Shared objects stay shared inside the copy
inner = [1]
pair = [inner, inner]
duplicate_pair = copy.deepcopy(pair)
print(duplicate_pair[0] is duplicate_pair[1])           # True
print(duplicate_pair[0] is inner)                       # False

# Program 5: deepcopy is slower than copying the rows yourself
rows = [[i] * 20 for i in range(500)]
start = time.perf_counter()
row_copy = [row[:] for row in rows]
time_rows = time.perf_counter() - start
start = time.perf_counter()
deep_rows = copy.deepcopy(rows)
time_deep = time.perf_counter() - start
print(f"row copy: {time_rows:.5f}s | deepcopy: {time_deep:.5f}s")
print(row_copy == deep_rows, time_deep > time_rows)     # True True (times differ on your computer)


# =====================================================
# Concept 10: Which Copy Should I Use?
# =====================================================
"""
Definition:
Items are numbers, strings, tuples of those  -> a.copy() is enough
Items are lists (2 levels)                   -> [row[:] for row in a]
Items are dicts with simple values           -> [d.copy() for d in a]
Anything deeper or mixed                     -> copy.deepcopy(a)
Not sure, and the data is small              -> copy.deepcopy(a)
Same list, only a second name is wanted      -> b = a
"""

# Program 1: Flat list of immutables, copy() is enough
names = ["ali", "sara"]
dup = names.copy()
dup[0] = "bilal"
print(names, dup)                       # ['ali', 'sara'] ['bilal', 'sara']

# Program 2: Rows (two levels)
grid = [[1, 2], [3, 4]]
dup = [row[:] for row in grid]
dup[0][0] = 99
print(grid, dup)                        # [[1, 2], [3, 4]] [[99, 2], [3, 4]]

# Program 3: Records with simple values
users = [{"name": "Ali", "age": 25}, {"name": "Sara", "age": 22}]
dup = [u.copy() for u in users]
dup[0]["age"] = 99
print(users[0]["age"], dup[0]["age"])   # 25 99

# Program 4: Records that contain lists need deepcopy
users = [{"name": "Ali", "roles": ["tester"]}]
half = [u.copy() for u in users]
half[0]["roles"].append("admin")
print(users)                            # [{'name': 'Ali', 'roles': ['tester', 'admin']}] (still shared)
users = [{"name": "Ali", "roles": ["tester"]}]
full = copy.deepcopy(users)
full[0]["roles"].append("admin")
print(users)                            # [{'name': 'Ali', 'roles': ['tester']}]


# =====================================================
# Concept 11: Dictionaries and Sets Copy the Same Way
# =====================================================
"""
Definition:
dict.copy(), dict(d), {**d} and copy.copy(d) are shallow, exactly
like list copies. A set can hold only immutable items, so a
shallow copy of a set is always enough.
"""

# Program 1: A shallow copy of a dictionary
d = {"a": [1], "b": 2}
e = d.copy()
e["a"].append(2)
e["b"] = 99
print(d)                                # {'a': [1, 2], 'b': 2}
print(e)                                # {'a': [1, 2], 'b': 99}

# Program 2: Four ways, all shallow
print(all(x["a"] is d["a"] for x in (dict(d), {**d}, d.copy(), copy.copy(d))))  # True

# Program 3: A set
s = {1, 2}
t = s.copy()
t.add(3)
print(sorted(s), sorted(t))             # [1, 2] [1, 2, 3]

# Program 4: deepcopy of a dictionary
deep = copy.deepcopy(d)
deep["a"].append(5)
print(d["a"], deep["a"])                # [1, 2] [1, 2, 5]


# =====================================================
# Concept 12: Passing a List to a Function
# =====================================================
"""
Definition:
A function receives a REFERENCE to the same list, not a copy
(Python calls this "call by object reference").
- changing the list (append, sort, items, +=) changes the caller's list
- giving the parameter a new list (items = items + [...]) changes
  only the local name
To protect the caller's data, copy first or build a new list.
"""

# Program 1: Changing the list inside the function
def add_item(items):
    items.append("x")

data = ["a"]
add_item(data)
print(data)                             # ['a', 'x']

# Program 2: Rebinding the local name does nothing to the caller
def rebind(items):
    items = items + ["y"]

data = ["a"]
rebind(data)
print(data)                             # ['a']

# Program 3: += changes the list in place (a common surprise)
def plus_equal(items):
    items += ["z"]

data = ["a"]
plus_equal(data)
print(data)                             # ['a', 'z']

# Program 4: sort() changes the caller's list, sorted() does not
def sort_in_place(items):
    items.sort()

def get_sorted(items):
    return sorted(items)

data = [3, 1, 2]
print(get_sorted(data), data)           # [1, 2, 3] [3, 1, 2]
sort_in_place(data)
print(data)                             # [1, 2, 3]

# Program 5: The safe way, work on a copy and return the new list
def safe_add(items):
    new_items = items.copy()
    new_items.append("q")
    return new_items

original = ["a"]
result = safe_add(original)
print(original, result)                 # ['a'] ['a', 'q']

# Program 6: The function receives the very same object
def get_id(value):
    return id(value)

print(get_id(original) == id(original)) # True


# =====================================================
# Concept 13: The Mutable Default Argument Trap
# =====================================================
"""
Definition:
A default value is created ONCE, when the function is defined (not at
every call). If the default is a list, every call that does not pass
its own list uses the SAME list, and it keeps growing.
Fix: use None as the default and create the list inside the function.
Immutable defaults (numbers, strings, None, tuples) are safe.
"""

# Program 1: The trap
def add_test(name, tests=[]):
    tests.append(name)
    return tests

print(add_test("a"))                    # ['a']
print(add_test("b"))                    # ['a', 'b'] (the old value is still there!)

# Program 2: The default list lives inside the function object
print(add_test.__defaults__)            # (['a', 'b'],)

# Program 3: The fix
def add_test_safe(name, tests=None):
    if tests is None:
        tests = []
    tests.append(name)
    return tests

print(add_test_safe("a"))               # ['a']
print(add_test_safe("b"))               # ['b']

# Program 4: Passing your own list works with both versions
mine = ["x"]
print(add_test_safe("y", mine), mine)   # ['x', 'y'] ['x', 'y']

# Program 5: An immutable default is fine
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Ali"), "|", greet("Sara", "Hi"))           # Hello, Ali | Hi, Sara


# =====================================================
# Concept 14: Repetition (list * n) Shares the Items
# =====================================================
"""
Definition:
list * n repeats the SAME objects n times, it does not copy them.
[0] * 3 is safe (numbers cannot change).
[[0] * 3] * 3 and [{}] * 3 repeat ONE inner object.
Build separate inner objects with a comprehension.
"""

# Program 1: Safe with immutable items
row = [0] * 3
row[0] = 1
print(row)                              # [1, 0, 0]

# Program 2: The trap with inner lists
grid = [[0] * 3] * 2
grid[0][0] = 1
print(grid)                             # [[1, 0, 0], [1, 0, 0]]
print(len(set(map(id, grid))))          # 1 (one row object)

# Program 3: The trap with dictionaries
records = [{}] * 3
records[0]["x"] = 1
print(records)                          # [{'x': 1}, {'x': 1}, {'x': 1}]

# Program 4: The fix, a new object in every round
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print(grid)                             # [[1, 0, 0], [0, 0, 0]]
records = [{} for _ in range(3)]
records[0]["x"] = 1
print(records)                          # [{'x': 1}, {}, {}]

# Program 5: Many names, one object (and so very little memory)
big_text = "x" * 1000
shared = [big_text] * 1000
print(len(set(map(id, shared))))        # 1


# =====================================================
# Concept 15: A List That Contains Itself
# =====================================================
"""
Definition:
Because a list only stores references, it can store a reference to
itself. Python prints the inner copy as [...]. This is rare, but it
shows how references work. copy.copy() keeps pointing to the original,
copy.deepcopy() builds a new self-containing list.
"""

# Program 1: Create and print
loop = [1, 2]
loop.append(loop)
print(loop)                             # [1, 2, [...]]
print(len(loop), loop[2] is loop)       # 3 True

# Program 2: A shallow copy still points to the ORIGINAL list
shallow = loop.copy()
print(shallow[2] is loop, shallow[2] is shallow)        # True False

# Program 3: A deep copy points to ITSELF
deep = copy.deepcopy(loop)
print(deep is loop, deep[2] is deep)    # False True


# =====================================================
# Concept 16: Tuples That Hold Lists
# =====================================================
"""
Definition:
A tuple is immutable, but it only holds REFERENCES. If one of them
points to a list, that list can still be changed. Such a tuple is
also not hashable (it cannot be a dictionary key).
"""

# Program 1: The list inside can change
t = ([1], "x")
t[0].append(2)
print(t)                                # ([1, 2], 'x')

# Program 2: The reference itself cannot be replaced
try:
    t[0] = [9]
except TypeError as e:
    print("Error:", e)                  # 'tuple' object does not support item assignment

# Program 3: The famous surprise with +=
t = ([1],)
try:
    t[0] += [2]
except TypeError as e:
    print("Error:", e)                  # 'tuple' object does not support item assignment
print(t)                                # ([1, 2],) (it failed AND it worked)

# Program 4: Not hashable
try:
    hash(([1], 2))
except TypeError as e:
    print("Error:", e)                  # unhashable type: 'list'
print(hash((1, 2)) == hash((1, 2)))     # True


# =====================================================
# Concept 17: Reference Counting and del
# =====================================================
"""
Definition:
CPython counts how many references point to every object. When the
count reaches 0 the object is freed. del removes a NAME, it never
deletes an object directly. A list that holds an item also counts as
one reference to that item.
sys.getrefcount(x) always shows ONE extra (the argument of the call
itself), so compare differences only.
"""

# Program 1: A new name adds one reference
obj = [1, 2]
before = sys.getrefcount(obj)
other = obj
after = sys.getrefcount(obj)
print(after - before)                   # 1

# Program 2: del removes a name, the object stays while another name exists
a = [1]
b = a
del a
print(b)                                # [1]
try:
    print(a)
except NameError as e:
    print("Error:", e)                  # name 'a' is not defined

# Program 3: A container counts as a reference
item = [1]
before = sys.getrefcount(item)
box = [item]
print(sys.getrefcount(item) - before)   # 1

# Program 4: del brings the count down again
extra = obj
count_with_extra = sys.getrefcount(obj)
del extra
print(sys.getrefcount(obj) == count_with_extra - 1)     # True


# =====================================================
# Concept 18: Memory Size of Lists
# =====================================================
"""
Definition:
sys.getsizeof(x) gives the size of the object ITSELF in bytes.
It is shallow: a list is counted as its own space (about 8 bytes per
slot for the references), NOT the items inside. Exact numbers differ
between Python versions, so compare them.
A list grows in jumps and keeps some spare slots, so it does not
resize at every append(). A copy is built with exactly the size it needs.
"""

# Program 1: A longer list needs more memory
print(sys.getsizeof([]) < sys.getsizeof([1, 2, 3]) < sys.getsizeof(list(range(100))))   # True

# Program 2: The items are not counted
big = ["x" * 1000]
print(sys.getsizeof(big) < sys.getsizeof(big[0]))       # True

# Program 3: The size grows in jumps, not at every append
numbers = []
last_size = sys.getsizeof(numbers)
size_changes = 0
for n in range(100):
    numbers.append(n)
    size = sys.getsizeof(numbers)
    if size != last_size:
        size_changes += 1
        last_size = size
print(0 < size_changes < 100)           # True (a few dozen jumps at most)

# Program 4: A copy has no spare slots
grown = []
for n in range(100):
    grown.append(n)
print(sys.getsizeof(grown.copy()) <= sys.getsizeof(grown))      # True

# Program 5: A rough total size of a list of lists
rows = [[i] * 10 for i in range(5)]
total = sys.getsizeof(rows) + sum(sys.getsizeof(r) for r in rows)
print(total > sys.getsizeof(rows))      # True

# Program 6: One shared object or many equal objects
shared = ["x" * 1000] * 1000
separate = ["".join(["x"] * 1000) for _ in range(1000)]
print(len(set(map(id, shared))), len(set(map(id, separate))))   # 1 1000 (typical)
print(shared == separate)                                        # True (equal values, different memory use)


# =====================================================
# Concept 19: Alias vs Shallow vs Deep (Identity Table)
# =====================================================
"""
Definition:
For original = [[1, 2], [3, 4]]:
              outer list   rows     numbers
alias         same         same     same
shallow       new          same     same
deep          new          new      same (they are immutable)
"""

# Program 1: Print the table
original = [[1, 2], [3, 4]]
alias = original
shallow = original.copy()
deep = copy.deepcopy(original)
for label, other in (("alias", alias), ("shallow", shallow), ("deep", deep)):
    outer = other is original
    row = other[0] is original[0]
    number = other[0][0] is original[0][0]
    print(f"{label:<9}outer same: {str(outer):<6} row same: {str(row):<6} number same: {number}")
# alias    outer same: True   row same: True   number same: True
# shallow  outer same: False  row same: True   number same: True
# deep     outer same: False  row same: False  number same: True

# Program 2: All three compare equal with ==
print(alias == original, shallow == original, deep == original)         # True True True

# Program 3: After a change inside a row, who still equals the original?
original[0].append("x")
print(alias == original, shallow == original, deep == original)         # True True False


# =====================================================
# Concept 20: Operations That Share the Items
# =====================================================
"""
Definition:
Operations that build a NEW list but reuse the SAME items:
slicing, list(), +, * n, sorted(), reversed(), comprehensions
without copying, extend() and +=.
So for lists of lists, any of them gives a new outer list, but the
rows are shared.
"""

# Program 1: Seven new lists, all with the original rows
a = [[1], [2]]
new_lists = [a[:], list(a), sorted(a), list(reversed(a)), a + [], a * 2, [r for r in a]]
print(all(all(any(row is original_row for original_row in a) for row in new) for new in new_lists))     # True

# Program 2: A change through sorted() reaches the original rows
a = [[3], [1]]
s = sorted(a)
s[0].append(0)
print(a)                                # [[3], [1, 0]]

# Program 3: + shares the rows
x = [[1]]
y = x + [[2]]
y[0].append("!")
print(x)                                # [[1, '!']]

# Program 4: extend() and += add the same row objects
first = [[1]]
second = [[2]]
first.extend(second)
first += [[3]]
print(first[1] is second[0])            # True

# Program 5: Copy the rows when you need independent data
safe = [row[:] for row in sorted(a)]
safe[0].append("only in the copy")
print(a)                                # [[3], [1, 0]]


# =====================================================
# Concept 21: Common Mistakes
# =====================================================
"""
Definition:
1) b = a as a "backup"
2) .copy() or [:] on a list of lists
3) b = a.copy().append(4)  -> b is None
4) appending the SAME list again and again in a loop
5) [[0] * 3] * 3
6) a mutable default argument
7) comparing values with is
8) hiding the copy module with a variable named copy
9) using deepcopy everywhere (slow, and often not needed)
"""

# Program 1: Backup with =
data = [1, 2, 3]
backup = data
data.append(4)
print(backup)                           # [1, 2, 3, 4] (wrong)
backup = data.copy()
data.append(5)
print(backup)                           # [1, 2, 3, 4] (right)

# Program 2: copy() on nested lists
grid = [[1], [2]]
wrong = grid.copy()
wrong[0].append("!")
print(grid)                             # [[1, '!'], [2]]

# Program 3: Storing the result of append()
a = [1, 2, 3]
b = a.copy().append(4)
print(b)                                # None
b = a.copy()
b.append(4)
print(b)                                # [1, 2, 3, 4]

# Program 4: The same list appended again and again
path = []
paths = []
for step in "abc":
    path.append(step)
    paths.append(path)
print(paths)                            # [['a', 'b', 'c'], ['a', 'b', 'c'], ['a', 'b', 'c']]
path = []
paths = []
for step in "abc":
    path.append(step)
    paths.append(path.copy())
print(paths)                            # [['a'], ['a', 'b'], ['a', 'b', 'c']]

# Program 5: Value comparison with is
x = [1, 2]
y = [1, 2]
print(x is y, x == y)                   # False True

# Program 6: A variable named copy hides the module
saved_module = copy
copy = [1, 2]
try:
    copy.deepcopy(copy)
except AttributeError as e:
    print("Error:", e)                  # 'list' object has no attribute 'deepcopy'
copy = saved_module                     # put the module back
print(copy.deepcopy([[1]]))             # [[1]]

# Program 7: deepcopy of a flat list is a waste
flat = [1, 2, 3]
print(copy.deepcopy(flat) == flat.copy())       # True (flat.copy() is enough and faster)


# =====================================================
# Concept 22: Copying and References in SQA Automation
# =====================================================
"""
Definition:
Test data is often shared: a base user, default settings, a list of
test rows. If one test changes the shared object, the next test starts
with dirty data and fails for no real reason. Typical protections:
deepcopy a base object for every test, copy rows before a test
changes them, snapshot a list (copy) before an action to compare
"before" and "after", never let "expected" be the SAME list as "actual",
and avoid mutable default arguments in helpers.
"""

# Program 1: A shared base user is damaged by one test
BASE_USER = {"name": "ali", "roles": ["tester"]}
test_user = BASE_USER.copy()                    # shallow
test_user["name"] = "sara"
test_user["roles"].append("admin")
print(BASE_USER)                        # {'name': 'ali', 'roles': ['tester', 'admin']} (dirty!)

# Program 2: The fix, a deep copy for every test
BASE_USER = {"name": "ali", "roles": ["tester"]}
test_user = copy.deepcopy(BASE_USER)
test_user["name"] = "sara"
test_user["roles"].append("admin")
print(BASE_USER)                        # {'name': 'ali', 'roles': ['tester']}
print(test_user)                        # {'name': 'sara', 'roles': ['tester', 'admin']}

# Program 3: A test that can never fail (expected is the same list as actual)
actual_menu = ["Home", "Product", "Contact"]
expected_menu = actual_menu                     # the bug: an alias, not independent data
print(expected_menu == actual_menu)             # True (always!)
expected_menu = ["Home", "Products", "Contact"] # the fix: independent expected data
print(expected_menu == actual_menu)             # False (the real bug is found)

# Program 4: A snapshot before an action, to find what changed
items_on_page = ["Pen", "Notebook"]
snapshot = items_on_page.copy()
items_on_page.append("Bag")                     # the action under test
print(snapshot)                         # ['Pen', 'Notebook']
print(items_on_page)                    # ['Pen', 'Notebook', 'Bag']
print([x for x in items_on_page if x not in snapshot])  # ['Bag'] (what was added)

# Program 5: A history of states (a copy at every step)
current = []
history = []
for result in ["PASS", "FAIL", "PASS"]:
    current.append(result)
    history.append(current.copy())
print(history)                          # [['PASS'], ['PASS', 'FAIL'], ['PASS', 'FAIL', 'PASS']]

# Program 6: Keep the test rows safe when a test changes them
login_rows = [["admin", "Admin@123"], ["tester", "Test@456"]]
run_rows = [row[:] for row in login_rows]
run_rows[0][1] = "****"                         # the test masks the password for its log
print(login_rows[0])                    # ['admin', 'Admin@123']
print(run_rows[0])                      # ['admin', '****']

# Program 7: Build many test records from one template
base = {"username": "", "password": "Admin@123", "tags": ["login"]}
rows = []
for name in ["ali", "sara"]:
    row = copy.deepcopy(base)
    row["username"] = name
    row["tags"].append(name)
    rows.append(row)
print(rows[0]["tags"], rows[1]["tags"])         # ['login', 'ali'] ['login', 'sara']
print(base["tags"])                     # ['login'] (the template is clean)

# Program 8: The same job with a shallow copy goes wrong
base = {"username": "", "password": "Admin@123", "tags": ["login"]}
rows = []
for name in ["ali", "sara"]:
    row = base.copy()
    row["username"] = name
    row["tags"].append(name)
    rows.append(row)
print(rows[0]["tags"])                  # ['login', 'ali', 'sara'] (shared list!)
print(rows[0]["tags"] is rows[1]["tags"] is base["tags"])       # True

# Program 9: A mutable default argument leaks failures between tests
def record_failure(message, failures=[]):
    failures.append(message)
    return failures

print(record_failure("test_login failed"))      # ['test_login failed']
print(record_failure("test_cart failed"))       # ['test_login failed', 'test_cart failed'] (leak)

def record_failure_safe(message, failures=None):
    if failures is None:
        failures = []
    failures.append(message)
    return failures

print(record_failure_safe("test_login failed"))     # ['test_login failed']
print(record_failure_safe("test_cart failed"))      # ['test_cart failed']

# Program 10: Sorting a copy of the texts does not change the original order
# (a real all_inner_texts() call also gives you your own new list each time)
page_items = ["Pen", "Notebook", "Bag"]
texts = page_items.copy()
texts.sort(reverse=True)
print(page_items)                       # ['Pen', 'Notebook', 'Bag']
print(texts)                            # ['Pen', 'Notebook', 'Bag'] -> sorted descending: ['Pen', 'Notebook', 'Bag']