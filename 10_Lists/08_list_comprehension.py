"""
====================================================
10_Lists / 08_list_comprehension.py
====================================================
Topic: List Comprehensions
====================================================
Notes before you run this file:
1) A list comprehension builds a NEW list in one line:
       [expression for item in iterable if condition]
   It is the short form of a loop that appends to a new list.
2) It does not change the list you loop over.
3) Rule of thumb: if you cannot read it easily, use a normal loop.
4) The walrus operator := (Concept 11) needs Python 3.8 or newer.
5) "_" is the usual name for a loop variable you do not use.
6) Plain programs only, no functions.
"""

import re
import sys
import time


# =====================================================
# Concept 1: What is a List Comprehension?
# =====================================================
"""
Definition:
A list comprehension creates a new list by taking every item of an
iterable, optionally filtering it, and optionally changing it.
It is written inside square brackets and always returns a list.
"""

# Program 1: Squares of numbers
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)                          # [1, 4, 9, 16, 25]

# Program 2: Change every name
names = ["ali", "sara", "bilal"]
print([name.title() for name in names])         # ['Ali', 'Sara', 'Bilal']

# Program 3: Lengths of the names
print([len(name) for name in names])    # [3, 4, 5]

# Program 4: The result is a list
print(type(squares).__name__)           # list


# =====================================================
# Concept 2: The Syntax and its Loop Version
# =====================================================
"""
Definition:
[expression for item in iterable if condition]
  1) 'for' takes the items one by one
  2) 'if' (optional) decides if the item is used
  3) 'expression' creates the value that goes into the new list
The same job as a loop:
  result = []
  for item in iterable:
      if condition:
          result.append(expression)
"""

# Program 1: A loop and a comprehension give the same list
loop_result = []
for n in [1, 2, 3, 4, 5, 6]:
    if n % 2 == 0:
        loop_result.append(n * 10)
comp_result = [n * 10 for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(loop_result, comp_result)         # [20, 40, 60] [20, 40, 60]
print(loop_result == comp_result)       # True

# Program 2: A new list is created, the original stays the same
original = [1, 2, 3]
new_list = [n + 1 for n in original]
print(original, new_list)               # [1, 2, 3] [2, 3, 4]
print(original is new_list)             # False

# Program 3: Without the expression part, you get a plain copy of the items
print([n for n in original])            # [1, 2, 3]


# =====================================================
# Concept 3: Transforming Items (the Expression Part)
# =====================================================
"""
Definition:
The expression can be anything that makes a value: a calculation,
a method call, a function call, an f-string, a tuple, even another
list. This is the "map" part: every item goes in, one new value
comes out.
"""

# Program 1: Calculations
print([n * 2 for n in [1, 2, 3]])       # [2, 4, 6]
print([abs(n) for n in [-3, 4, -5]])    # [3, 4, 5]

# Program 2: Clean texts and convert them to numbers
print([t.strip() for t in ["  a ", "b  "]])             # ['a', 'b']
print([int(t) for t in "3 5 8".split()])                # [3, 5, 8]

# Program 3: f-strings
print([f"{n:03}" for n in [1, 2, 3]])                   # ['001', '002', '003']
print([f"item_{n}" for n in range(1, 4)])               # ['item_1', 'item_2', 'item_3']

# Program 4: Every item becomes a tuple
words = ["pear", "fig"]
print([(w, len(w)) for w in words])     # [('pear', 4), ('fig', 3)]

# Program 5: A fixed value for every round
print([0 for _ in range(4)])            # [0, 0, 0, 0]
print([str(n) for n in [1, 2]])         # ['1', '2']


# =====================================================
# Concept 4: Filtering Items (the if Part)
# =====================================================
"""
Definition:
An 'if' at the END keeps only the items for which the condition is
True. The other items are left out completely. This is the "filter" part.
"""

# Program 1: Even numbers
print([n for n in range(1, 11) if n % 2 == 0])          # [2, 4, 6, 8, 10]

# Program 2: Words longer than 3 letters, and files that start with test_
print([w for w in ["pear", "fig", "banana", "kiwi"] if len(w) > 3])     # ['pear', 'banana', 'kiwi']
files = ["test_a.py", "helper.py", "test_b.py"]
print([f for f in files if f.startswith("test_")])      # ['test_a.py', 'test_b.py']

# Program 3: Remove empty texts (a text with only spaces is also removed)
print([t for t in ["a", "", " ", "b"] if t.strip()])    # ['a', 'b']

# Program 4: Remove None, but keep 0
data = [0, 1, None, 2, None]
print([x for x in data if x])                           # [1, 2] (0 is removed too!)
print([x for x in data if x is not None])               # [0, 1, 2]

# Program 5: Remove items that are in another list
print([x for x in [1, 2, 3, 4] if x not in [2, 3]])     # [1, 4]


# =====================================================
# Concept 5: if-else Inside the Expression
# =====================================================
"""
Definition:
To CHANGE items depending on a condition (and keep all of them), put
a conditional expression in the FIRST part:
    [A if condition else B for item in iterable]
A plain filter 'if' goes at the END and has no else.
Mixing them up gives a SyntaxError.
"""

# Program 1: A label for every number
print(["even" if n % 2 == 0 else "odd" for n in [1, 2, 3, 4]])          # ['odd', 'even', 'odd', 'even']

# Program 2: Replace negative numbers with 0
print([n if n > 0 else 0 for n in [3, -1, 5, -2]])      # [3, 0, 5, 0]

# Program 3: PASS or FAIL for every score
print(["PASS" if s >= 50 else "FAIL" for s in [75, 30, 50]])            # ['PASS', 'FAIL', 'PASS']

# Program 4: Three outcomes (a chain)
print(["A" if s >= 90 else "B" if s >= 75 else "C" for s in [95, 80, 60]])      # ['A', 'B', 'C']

# Program 5: Filter AND if-else together
nums = [1, 2, 3, 4, 5, 6]
print([n * 2 if n % 2 == 0 else n for n in nums if n > 2])      # [3, 8, 5, 12]

# Program 6: The wrong place for else
try:
    eval("[n for n in [1, 2] if n > 0 else 0]")
except SyntaxError:
    print("SyntaxError: 'else' cannot come after the filter if")
print([n if n > 0 else 0 for n in [1, -2]])             # [1, 0] (the right way)


# =====================================================
# Concept 6: Several Conditions
# =====================================================
"""
Definition:
Combine conditions with and / or / not, or write several 'if' parts
one after the other (they work like 'and').
"""

numbers = list(range(1, 21))

# Program 1: and
print([n for n in numbers if n % 2 == 0 and n % 3 == 0])        # [6, 12, 18]

# Program 2: Two if parts (same result as and)
print([n for n in numbers if n % 2 == 0 if n % 3 == 0])         # [6, 12, 18]

# Program 3: or
print([n for n in numbers if n % 5 == 0 or n % 7 == 0])         # [5, 7, 10, 14, 15, 20]

# Program 4: not
print([n for n in range(1, 8) if not n % 2 == 0])               # [1, 3, 5, 7]


# =====================================================
# Concept 7: Looping Over Different Iterables
# =====================================================
"""
Definition:
The 'for' part accepts anything iterable: a string, a range, a
dictionary, zip(), enumerate(), the result of split() and so on.
"""

# Program 1: A string
print([c.upper() for c in "abc"])                       # ['A', 'B', 'C']
print([c for c in "automation" if c in "aeiou"])        # ['a', 'u', 'o', 'a', 'i', 'o']

# Program 2: A range
print([n ** 2 for n in range(1, 6)])                    # [1, 4, 9, 16, 25]

# Program 3: A dictionary
scores = {"Ali": 90, "Sara": 85}
print([name for name, score in scores.items() if score >= 88])          # ['Ali']
print([score for score in scores.values()])             # [90, 85]

# Program 4: zip()
print([a + b for a, b in zip([1, 2, 3], [10, 20, 30])])                 # [11, 22, 33]

# Program 5: enumerate()
print([f"{i}:{c}" for i, c in enumerate("abc")])        # ['0:a', '1:b', '2:c']
print([i for i, v in enumerate([5, 7, 5]) if v == 5])   # [0, 2]

# Program 6: The result of split()
print([int(x) for x in "10,20,30".split(",")])          # [10, 20, 30]


# =====================================================
# Concept 8: Several for Parts (Nested Loops in One Comprehension)
# =====================================================
"""
Definition:
You can write more than one 'for'. They are read from LEFT to RIGHT
in the same order as nested for loops: the FIRST for is the OUTER
loop, the last one is the INNER loop.
"""

# Program 1: All combinations
colors = ["red", "blue"]
sizes = ["S", "M"]
print([(c, s) for c in colors for s in sizes])
# [('red', 'S'), ('red', 'M'), ('blue', 'S'), ('blue', 'M')]

# Program 2: The same with real nested loops
pairs = []
for c in colors:
    for s in sizes:
        pairs.append((c, s))
print(pairs == [(c, s) for c in colors for s in sizes])         # True

# Program 3: Flatten a list of lists
matrix = [[1, 2, 3], [4, 5, 6]]
print([x for row in matrix for x in row])               # [1, 2, 3, 4, 5, 6]

# Program 4: Flatten and filter
print([x for row in matrix for x in row if x % 2 == 0]) # [2, 4, 6]

# Program 5: Pairs where the first is smaller than the second
print([(i, j) for i in range(3) for j in range(i + 1, 3)])      # [(0, 1), (0, 2), (1, 2)]

# Program 6: Every product
print([x * y for x in [1, 2, 3] for y in [10, 100]])    # [10, 100, 20, 200, 30, 300]


# =====================================================
# Concept 9: Nested Comprehensions (a List of Lists)
# =====================================================
"""
Definition:
A comprehension INSIDE the expression part builds a list of lists:
[[... for column in ...] for row in ...]
Careful: this is different from several 'for' parts in one pair of
brackets (Concept 8), which gives ONE flat list.
"""

# Program 1: A multiplication table
print([[i * j for j in range(1, 4)] for i in range(1, 4)])      # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Program 2: A grid of zeros, the safe way
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 1
print(grid)                             # [[1, 0, 0], [0, 0, 0]]

# Program 3: The trap, one row repeated
bad = [[0] * 3] * 2
bad[0][0] = 1
print(bad)                              # [[1, 0, 0], [1, 0, 0]] (both rows changed)
print(bad[0] is bad[1])                 # True

# Program 4: Change every cell
m = [[1, 2, 3], [4, 5, 6]]
print([[cell * 10 for cell in row] for row in m])       # [[10, 20, 30], [40, 50, 60]]

# Program 5: Transpose (rows become columns)
print([[row[i] for row in m] for i in range(len(m[0]))])        # [[1, 4], [2, 5], [3, 6]]
print(list(map(list, zip(*m))))         # [[1, 4], [2, 5], [3, 6]]

# Program 6: Row sums and column sums
print([sum(row) for row in m])          # [6, 15]
print([sum(col) for col in zip(*m)])    # [5, 7, 9]


# =====================================================
# Concept 10: Scope of the Loop Variable
# =====================================================
"""
Definition:
In Python 3 a comprehension has its OWN scope: its loop variable
does not leak out and does not overwrite a variable with the same
name. The comprehension CAN read variables from outside.
Trap: functions created inside a comprehension remember the VARIABLE,
not its value at that moment (late binding).
"""

# Program 1: The loop variable does not leak
x = "outside"
squares = [x * x for x in range(3)]
print(x)                                # outside (not changed)

# Program 2: The variable does not exist after the comprehension
try:
    [sq for sq in range(3)]
    print(sq)
except NameError as e:
    print("Error:", e)                  # name 'sq' is not defined

# Program 3: Outside variables can be read
factor = 10
print([n * factor for n in [1, 2, 3]])  # [10, 20, 30]

# Program 4: Late binding
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])             # [2, 2, 2] (all see the last i)
funcs = [lambda i=i: i for i in range(3)]
print([f() for f in funcs])             # [0, 1, 2] (fixed with a default value)


# =====================================================
# Concept 11: The Walrus Operator := in a Comprehension
# =====================================================
"""
Definition:
name := value assigns AND gives the value back. In a comprehension it
lets you calculate something ONCE and use it twice (in the filter and
in the result). The name stays available AFTER the comprehension.
(Python 3.8 or newer.)
"""

values = [1, 5, 10]

# Program 1: Calculate once, use in the filter and in the result
print([y for x in values if (y := x * x) > 10])         # [25, 100]

# Program 2: Keep the original and the calculated value
print([(x, y) for x in values if (y := x * x) > 10])    # [(5, 25), (10, 100)]

# Program 3: Strip a text once and skip it if it is empty
words = ["  Ali ", "", " Sara"]
print([clean for w in words if (clean := w.strip())])   # ['Ali', 'Sara']

# Program 4: The walrus name is still there afterwards
print(y)                                # 100 (the last value)


# =====================================================
# Concept 12: Set and Dictionary Comprehensions
# =====================================================
"""
Definition:
The same idea with other brackets:
{expression for item in iterable}         -> a SET (no duplicates, no order)
{key: value for item in iterable}         -> a DICTIONARY
Empty {} is a dictionary, not a set. If a dictionary key repeats,
the LAST value wins.
"""

# Program 1: A set removes duplicates (sorted() only gives it a fixed order for printing)
print(sorted({n % 3 for n in range(10)}))               # [0, 1, 2]
print(sorted({n.lower() for n in ["Ali", "ali", "Sara", "SARA"]}))      # ['ali', 'sara']

# Program 2: A dictionary
print({n: n * n for n in range(1, 4)})                  # {1: 1, 2: 4, 3: 9}
print({w: len(w) for w in ["pear", "fig"]})             # {'pear': 4, 'fig': 3}

# Program 3: A dictionary from two lists
names = ["Ali", "Sara"]
ages = [25, 22]
print({n: a for n, a in zip(names, ages)})              # {'Ali': 25, 'Sara': 22}

# Program 4: Invert and filter a dictionary
print({v: k for k, v in {"a": 1, "b": 2}.items()})      # {1: 'a', 2: 'b'}
scores = {"Ali": 90, "Sara": 85}
print({k: v for k, v in scores.items() if v >= 88})     # {'Ali': 90}

# Program 5: Empty braces and repeated keys
print(type({}).__name__)                                # dict
print({len(w): w for w in ["a", "b", "cc"]})            # {1: 'b', 2: 'cc'}


# =====================================================
# Concept 13: Generator Expressions
# =====================================================
"""
Definition:
Round brackets instead of square brackets give a GENERATOR: it makes
the values one at a time when asked, and does not build a list in
memory. It can be used only ONCE. When it is the only argument of a
function, you can drop the extra pair of brackets:
sum(n * n for n in numbers)
"""

# Program 1: sum, max, min, any, all
numbers = [1, 2, 3, 4, 5]
print(sum(n * n for n in numbers))                      # 55
print(max(len(w) for w in ["pear", "banana", "fig"]))   # 6
print(any(n > 4 for n in numbers), all(n > 0 for n in numbers))         # True True

# Program 2: A generator is lazy and works only once
gen = (n * 2 for n in [10, 20])
print(type(gen).__name__)               # generator
print(next(gen), next(gen))             # 20 40
print(next(gen, "done"))                # done
gen = (n for n in range(3))
print(list(gen), list(gen))             # [0, 1, 2] []

# Program 3: join() with a generator
print(",".join(str(n) for n in [1, 2, 3]))              # 1,2,3

# Program 4: Memory, a list stores everything, a generator does not
size = 100000
big_list = [n for n in range(size)]
big_gen = (n for n in range(size))
print(sys.getsizeof(big_list), sys.getsizeof(big_gen))  # the numbers depend on the Python version
print(sys.getsizeof(big_gen) < sys.getsizeof(big_list)) # True

# Program 5: The first match, or None if there is none
print(next((n for n in [1, 3, 6, 8] if n % 2 == 0), None))      # 6
print(next((n for n in [1, 3] if n % 2 == 0), None))            # None


# =====================================================
# Concept 14: Comprehension vs Loop vs map() and filter()
# =====================================================
"""
Definition:
The same job in different styles:
for loop + append            -> clear when the body is long or does extra work
list comprehension           -> clear for one simple transform or filter
list(map(f, items))          -> fine when f is a ready-made function (int, str.strip)
list(filter(f, items))       -> same idea for filtering
A comprehension is for BUILDING a list. Do not use it only to run
code (like print), use a normal loop for that.
"""

nums = [1, 2, 3, 4, 5, 6]

# Program 1: Four ways to double the numbers
loop = []
for n in nums:
    loop.append(n * 2)
print(loop == [n * 2 for n in nums] == list(map(lambda n: n * 2, nums)))        # True

# Program 2: Two ways to filter
print([n for n in nums if n % 2 == 0] == list(filter(lambda n: n % 2 == 0, nums)))      # True

# Program 3: map() with a ready-made function is short
print(list(map(int, ["1", "2", "3"])))                  # [1, 2, 3]
print(list(map(str.strip, ["  a ", "b "])))             # ['a', 'b']

# Program 4: A comprehension used only for its side effect (bad style)
result = [print(n) for n in [1, 2]]                     # prints 1 and 2
print(result)                                           # [None, None] (a useless list)
for n in [1, 2]:                                        # the right way
    print(n)


# =====================================================
# Concept 15: Readability
# =====================================================
"""
Definition:
Short comprehensions are great, long ones are hard to read. Ways to
keep them readable:
1) break it over several lines, one part per line
2) use clear names (word, not w) when it is long
3) split the job into steps with named lists
4) with more than 2 'for' or 2 'if' parts, use a normal loop
"""

# Program 1: Hard to read
hard = [(x, y) for x in range(5) for y in range(5) if x != y if (x + y) % 2 == 0 if x < y]
print(hard)                             # [(0, 2), (0, 4), (1, 3), (2, 4)]

# Program 2: The same job as a loop, easy to follow
easy = []
for x in range(5):
    for y in range(x + 1, 5):
        if (x + y) % 2 == 0:
            easy.append((x, y))
print(easy == hard)                     # True

# Program 3: One part per line
result = [
    n * n
    for n in range(10)
    if n % 2 == 0
]
print(result)                           # [0, 4, 16, 36, 64]

# Program 4: Steps with names are clearer than one long line
raw = ["  Ali ", "", " sara", "BILAL  "]
cleaned = [name.strip() for name in raw]
non_empty = [name for name in cleaned if name]
formatted = [name.title() for name in non_empty]
print(formatted)                        # ['Ali', 'Sara', 'Bilal']


# =====================================================
# Concept 16: A Comprehension Creates a NEW List
# =====================================================
"""
Definition:
The original list is never changed. To update a list IN PLACE, assign
to the whole slice: my_list[:] = [...]. Then every name that points to
the list sees the change. Items that are lists are shared, not copied
(a shallow copy), unless you copy them too.
"""

# Program 1: Reassigning moves only one name
data = [1, 2, 3]
alias = data
data = [n * 10 for n in data]
print(data, alias)                      # [10, 20, 30] [1, 2, 3]

# Program 2: Slice assignment changes the same list
data = [1, 2, 3]
alias = data
data[:] = [n * 10 for n in data]
print(data, alias)                      # [10, 20, 30] [10, 20, 30]

# Program 3: Inner lists are shared
grid = [[1, 2], [3, 4]]
shallow = [row for row in grid]
shallow[0].append(9)
print(grid)                             # [[1, 2, 9], [3, 4]] (changed through the copy)

# Program 4: Copy the rows too
copy_rows = [row[:] for row in grid]
copy_rows[1].append(7)
print(copy_rows)                        # [[1, 2, 9], [3, 4, 7]]
print(grid)                             # [[1, 2, 9], [3, 4]] (not affected)


# =====================================================
# Concept 17: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with comprehensions:
1) round brackets give a generator, not a list
2) else in the wrong place (a SyntaxError)
3) [x for x in range(5)] is only a long way to write list(range(5))
4) wrong order of two 'for' parts
5) [[0] * 3] * 3 repeats ONE inner list
6) using a comprehension to print or to change things
7) "if x" also removes 0 and empty text
"""

# Program 1: Brackets decide the type
print(type([x for x in range(3)]).__name__)             # list
print(type((x for x in range(3))).__name__)             # generator
print(type({x for x in range(3)}).__name__)             # set

# Program 2: Pointless comprehension
print([x for x in range(3)] == list(range(3)))          # True

# Program 3: The order of the 'for' parts changes the result
print([(a, b) for a in [1, 2] for b in "xy"])           # [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]
print([(a, b) for b in "xy" for a in [1, 2]])           # [(1, 'x'), (2, 'x'), (1, 'y'), (2, 'y')]

# Program 4: One inner list repeated
wrong = [[0] * 2] * 2
right = [[0] * 2 for _ in range(2)]
wrong[0][0] = 5
right[0][0] = 5
print(wrong, right)                     # [[5, 0], [5, 0]] [[5, 0], [0, 0]]

# Program 5: A condition that is too short
values = [0, "", "a", 3, None]
print([v for v in values if v])                         # ['a', 3]
print([v for v in values if v is not None])             # [0, '', 'a', 3]

# Program 6: A comprehension cannot contain a statement like break
try:
    eval("[n for n in [1, 2, 3] if n > 1 or break]")
except SyntaxError:
    print("SyntaxError: use a normal loop when you need break")


# =====================================================
# Concept 18: Speed
# =====================================================
"""
Definition:
A comprehension is usually a little faster than a loop with append(),
because the work is done inside Python's own machinery. Readability
matters more than this small gain. Use a generator expression when you
only need a total, so no big list is built. The times depend on your
computer, only compare them.
"""

size = 200000

# Program 1: Loop with append vs comprehension
start = time.perf_counter()
result_loop = []
for n in range(size):
    result_loop.append(n * 2)
time_loop = time.perf_counter() - start

start = time.perf_counter()
result_comp = [n * 2 for n in range(size)]
time_comp = time.perf_counter() - start

print(f"loop: {time_loop:.4f}s | comprehension: {time_comp:.4f}s")
print(result_loop == result_comp)       # True (same list)

# Program 2: A generator does not build the list
print(sum(n * 2 for n in range(size)) == sum(result_comp))      # True


# =====================================================
# Concept 19: Comprehensions in SQA Automation
# =====================================================
"""
Definition:
Test code uses comprehensions to clean texts from a page, pick the
failed tests, turn price texts into numbers, build test data and test
matrices, find differences between expected and actual lists, and
check "all items" or "any item" quickly. A real Playwright call like
page.locator("li").all_inner_texts() returns a list, so these work
directly on it.
"""

# Program 1: Clean the texts of a page (split() also handles \xa0 and \n)
texts = ["  Home ", "Products\xa0", "", "Contact\n"]
print([" ".join(t.split()) for t in texts if t.strip()])         # ['Home', 'Products', 'Contact']

# Program 2: Failed tests and the pass rate
results = [("login", "PASS"), ("cart", "FAIL"), ("search", "PASS"), ("payment", "FAIL")]
failed = [name for name, status in results if status == "FAIL"]
passed = [name for name, status in results if status == "PASS"]
print(failed)                           # ['cart', 'payment']
print(f"{len(passed) / len(results):.0%}")      # 50%

# Program 3: Price texts to numbers
price_texts = ["$9.99", "$1,234.50", "$45.00"]
prices = [float(t.replace("$", "").replace(",", "")) for t in price_texts]
print(prices)                           # [9.99, 1234.5, 45.0]
print(f"{sum(prices):.2f}")             # 1289.49

# Program 4: Log levels
lines = ["[PASS] a", "[FAIL] b", "[PASS] c", "[ERROR] d", "[PASS] e"]
levels = [line.split()[0].strip("[]") for line in lines]
print(levels)                           # ['PASS', 'FAIL', 'PASS', 'ERROR', 'PASS']
print({level: levels.count(level) for level in sorted(set(levels))})    # {'ERROR': 1, 'FAIL': 1, 'PASS': 3}

# Program 5: Extract ids from log lines (the walrus avoids searching twice)
log_lines = ["user id=12 ok", "no id here", "user id=7 ok"]
print([m.group(1) for line in log_lines if (m := re.search(r"id=(\d+)", line))])    # ['12', '7']

# Program 6: Differences between expected and actual
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Product", "Contact"]
print([(i, e, a) for i, (e, a) in enumerate(zip(expected, actual), start=1) if e != a])
# [(2, 'Products', 'Product')]
print("missing:", [x for x in expected if x not in actual])     # ['Products']
print("extra:", [x for x in actual if x not in expected])       # ['Product']

# Program 7: A test matrix, every test on every browser
browsers = ["chromium", "firefox"]
tests = ["login", "cart"]
runs = [f"{t} on {b}" for b in browsers for t in tests]
print(runs)     # ['login on chromium', 'cart on chromium', 'login on firefox', 'cart on firefox']

# Program 8: Generate test case ids
print([f"TC_LOGIN_{n:03}" for n in range(1, 4)])         # ['TC_LOGIN_001', 'TC_LOGIN_002', 'TC_LOGIN_003']

# Program 9: Find invalid emails (a simple check)
emails = ["ali@example.com", "bad.email", "sara@x.org", "a b@x.com"]
print([e for e in emails if "@" not in e or " " in e])  # ['bad.email', 'a b@x.com']

# Program 10: Check ALL or ANY menu items with generator expressions
menu = ["Home", "Products", "", "Contact"]
print(all(t.strip() for t in menu))                     # False (one is empty)
print(any(not t.strip() for t in menu))                 # True

# Program 11: Dictionaries from results
print({name: status for name, status in results if status == "FAIL"})   # {'cart': 'FAIL', 'payment': 'FAIL'}
print(sorted({status for _, status in results}))        # ['FAIL', 'PASS']

# Program 12: Unique ids, case-insensitive, the first spelling order kept
print(list(dict.fromkeys(i.upper() for i in ["tc_1", "TC_1", "tc_2"])))     # ['TC_1', 'TC_2']

# Program 13: Rows of CSV text
csv_lines = ["ali,25,Active", "sara,22,Inactive"]
rows = [line.split(",") for line in csv_lines]
print(rows)                             # [['ali', '25', 'Active'], ['sara', '22', 'Inactive']]
print([r[0] for r in rows if r[2] == "Active"])         # ['ali']
print([int(r[1]) for r in rows])        # [25, 22]