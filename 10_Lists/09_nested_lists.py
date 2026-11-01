"""
====================================================
10_Lists / 09_nested_lists.py
====================================================
Topic: Nested Lists (lists inside lists, 2D lists, matrices)
====================================================
Notes before you run this file:
1) A nested list is a list whose items are lists. A list of rows is a
   2D list (a matrix, a table). You read a cell with  m[row][column].
2) len(m) is the number of ROWS. len(m[0]) is the number of COLUMNS.
3) The biggest dangers of this file:
   a) [[0] * 3] * 3  repeats ONE row three times (Concept 8)
   b) copy() and [:] copy only the OUTER list, the rows are shared (Concept 9)
4) Plain programs only, no functions.
"""

import copy
from itertools import chain, zip_longest
from pprint import pprint


# =====================================================
# Concept 1: What is a Nested List?
# =====================================================
"""
Definition:
A nested list is a list that contains other lists as items.
The inner lists are usually called ROWS. Nesting can go as deep as
you like: a list of lists of lists is a 3D list.
"""

# Program 1: A 3 x 3 matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)                           # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(matrix), type(matrix[0]))    # <class 'list'> <class 'list'>

# Program 2: A list of records (each row is one student)
students = [["Ali", 90], ["Sara", 85], ["Bilal", 78]]
print(len(students))                    # 3 (three rows)
print(students[0])                      # ['Ali', 90]

# Program 3: A table with a header row
table = [["Name", "Score"], ["Ali", 90], ["Sara", 85]]
for row in table:
    print(row)

# Program 4: A 3D list (planes, rows, columns)
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print(cube[1][0][1])                    # 6
print(len(cube), len(cube[0]), len(cube[0][0]))         # 2 2 2

# Program 5: Plain items and lists can be mixed
mixed = [1, [2, 3], "four", [5, [6]]]
print(len(mixed))                       # 4
print(mixed[3][1][0])                   # 6


# =====================================================
# Concept 2: Creating Nested Lists
# =====================================================
"""
Definition:
Ways to create them:
1) a literal with brackets inside brackets
2) a list comprehension (the safe way to build a grid of one value)
3) list() or split() on every row of text
Rows may have different lengths (a "jagged" list).
"""

# Program 1: A literal
m = [[1, 2], [3, 4]]
print(m)                                # [[1, 2], [3, 4]]

# Program 2: A multiplication table with a comprehension
print([[i * j for j in range(1, 4)] for i in range(1, 4)])      # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

# Program 3: A grid filled with one value (the SAFE way)
print([[0] * 3 for _ in range(2)])      # [[0, 0, 0], [0, 0, 0]]

# Program 4: Rows from lines of text
lines = ["1 2 3", "4 5 6"]
print([[int(x) for x in line.split()] for line in lines])       # [[1, 2, 3], [4, 5, 6]]

# Program 5: Rows from ranges
print([list(range(1, 4)), list(range(4, 7))])  # [[1, 2, 3], [4, 5, 6]]

# Program 6: Rows of different lengths
jagged = [[1], [2, 3], [4, 5, 6]]
print(jagged)                           # [[1], [2, 3], [4, 5, 6]]

# Program 7: Empty lists
print(len([]), len([[]]), len([[]][0]))         # 0 1 0 ([[]] has ONE row with no items)


# =====================================================
# Concept 3: Accessing Items  m[row][column]
# =====================================================
"""
Definition:
m[i] gives the row at position i (a list).
m[i][j] gives the item at position j INSIDE that row.
Read from left to right: first the outer index, then the inner one.
Negative indexes work on both levels.
"""

m = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
#  column:   0   1   2
#  row 0:   10  20  30
#  row 1:   40  50  60
#  row 2:   70  80  90

# Program 1: Rows and cells
print(m[0])                             # [10, 20, 30]
print(m[1][2])                          # 60
print(m[2][0])                          # 70

# Program 2: Two steps written separately
row = m[1]
item = row[2]
print(row, item)                        # [40, 50, 60] 60

# Program 3: Negative indexes
print(m[-1][-1], m[-1][0], m[0][-1])    # 90 70 30

# Program 4: The ORDER of the indexes matters
print(m[2][0], m[0][2])                 # 70 30

# Program 5: Errors
try:
    print(m[3])
except IndexError as e:
    print("Error:", e)                  # list index out of range
try:
    print(m[0][3])
except IndexError as e:
    print("Error:", e)                  # list index out of range
try:
    print(m[0][0][0])
except TypeError as e:
    print("Error:", e)                  # 'int' object is not subscriptable

# Program 6: Strings inside lists can be indexed again
names = [["ali", "sara"], ["bilal"]]
print(names[0][1], names[0][1][0], names[1][0][-1])     # sara s l


# =====================================================
# Concept 4: Changing Items
# =====================================================
"""
Definition:
m[i][j] = value replaces one cell. m[i] = new_row replaces a whole
row (the new row may have another length). The index must already
exist, you cannot create a new cell by assigning to it.
"""

# Program 1: Change one cell
m = [[1, 2, 3], [4, 5, 6]]
m[0][1] = 99
print(m)                                # [[1, 99, 3], [4, 5, 6]]

# Program 2: Replace a whole row
m = [[1, 2, 3], [4, 5, 6]]
m[1] = [0]
print(m)                                # [[1, 2, 3], [0]]

# Program 3: Change a cell using its old value
m = [[1, 2], [3, 4]]
m[0][0] += 10
print(m)                                # [[11, 2], [3, 4]]

# Program 4: Swap two rows, then two cells
m = [[1, 2], [3, 4]]
m[0], m[1] = m[1], m[0]
print(m)                                # [[3, 4], [1, 2]]
m[0][0], m[1][1] = m[1][1], m[0][0]
print(m)                                # [[2, 4], [1, 3]]

# Program 5: The index must exist
try:
    m[5][0] = 1
except IndexError as e:
    print("Error:", e)                  # list index out of range
try:
    m[0][5] = 1
except IndexError as e:
    print("Error:", e)                  # list assignment index out of range


# =====================================================
# Concept 5: Rows, Columns and Size
# =====================================================
"""
Definition:
rows    = len(m)
columns = len(m[0])        (only if every row has the same length)
cells   = rows * columns
A matrix is "rectangular" when all rows have the same length.
A column is not stored anywhere, you build it: [row[j] for row in m]
"""

# Program 1: Size
m = [[1, 2, 3], [4, 5, 6]]
rows = len(m)
columns = len(m[0])
print(rows, columns, rows * columns)    # 2 3 6

# Program 2: Is the matrix rectangular?
for candidate in ([[1, 2], [3, 4]], [[1, 2], [3]]):
    is_rectangular = all(len(row) == len(candidate[0]) for row in candidate)
    print(candidate, is_rectangular)    # True / False

# Program 3: A row and a column
print(m[1])                             # [4, 5, 6] (a row exists as it is)
print([row[2] for row in m])            # [3, 6] (a column must be built)

# Program 4: Count all items, also in uneven rows
print(sum(len(row) for row in m))       # 6
print(sum(len(row) for row in [[1], [2, 3], [4, 5, 6]]))        # 6

# Program 5: An empty matrix has no first row
empty = []
try:
    print(len(empty[0]))
except IndexError as e:
    print("Error:", e)                  # list index out of range
print(len(empty[0]) if empty else 0)    # 0 (the safe way)


# =====================================================
# Concept 6: Looping Over Nested Lists
# =====================================================
"""
Definition:
Loop over the rows first, then over the cells of each row.
To CHANGE cells you need the position (row[j] = ...). Changing the
loop variable does not change the list. A column loop needs the
column index.
"""

# Program 1: Rows
m = [[1, 2, 3], [4, 5, 6]]
for row in m:
    print(row)

# Program 2: Every cell, in one line per row
for row in m:
    for value in row:
        print(value, end=" ")
    print()

# Program 3: With positions
for i in range(len(m)):
    for j in range(len(m[i])):
        print(f"m[{i}][{j}] = {m[i][j]}")

# Program 4: enumerate() on both levels
for i, row in enumerate(m):
    for j, value in enumerate(row):
        if value % 2 == 0:
            print(f"even number {value} at row {i}, column {j}")

# Program 5: Aligned printing
for row in m:
    print("".join(f"{v:>4}" for v in row))

# Program 6: Change cells in place
m = [[1, 2], [3, 4]]
for row in m:
    for j in range(len(row)):
        row[j] *= 10
print(m)                                # [[10, 20], [30, 40]]

# Program 7: Changing the loop variable does NOT change the list
m = [[1, 2], [3, 4]]
for row in m:
    for value in row:
        value *= 10
print(m)                                # [[1, 2], [3, 4]]

# Program 8: Loop over the columns
for j in range(len(m[0])):
    print("column", j, [row[j] for row in m])       # column 0 [1, 3]   column 1 [2, 4]


# =====================================================
# Concept 7: Adding and Removing Rows and Columns
# =====================================================
"""
Definition:
ROWS are items of the outer list: append, insert, extend, pop, del, remove.
COLUMNS exist in every row, so you change EVERY row in a loop.
"""

# Program 1: Add rows
m = [[1, 2], [3, 4]]
m.append([5, 6])
m.insert(0, [0, 0])
print(m)                                # [[0, 0], [1, 2], [3, 4], [5, 6]]

# Program 2: Add a column at the end
m = [[1, 2], [3, 4]]
for row in m:
    row.append(0)
print(m)                                # [[1, 2, 0], [3, 4, 0]]

# Program 3: Insert a column at position 1
m = [[1, 2], [3, 4]]
for row in m:
    row.insert(1, 99)
print(m)                                # [[1, 99, 2], [3, 99, 4]]

# Program 4: Add a column with its own values
m = [[1, 2], [3, 4]]
new_column = [10, 20]
for row, value in zip(m, new_column):
    row.append(value)
print(m)                                # [[1, 2, 10], [3, 4, 20]]

# Program 5: Remove rows
m = [[1, 2], [3, 4], [5, 6]]
last = m.pop()
del m[0]
print(m, last)                          # [[3, 4]] [5, 6]
m = [[1, 2], [3, 4]]
m.remove([3, 4])
print(m)                                # [[1, 2]]

# Program 6: Remove a column
m = [[1, 2, 3], [4, 5, 6]]
for row in m:
    del row[1]
print(m)                                # [[1, 3], [4, 6]]

# Program 7: Take the first column out
m = [[1, 2, 3], [4, 5, 6]]
removed = []
for row in m:
    removed.append(row.pop(0))
print(removed, m)                       # [1, 4] [[2, 3], [5, 6]]

# Program 8: extend() and += add the SAME row objects
m1 = [[1, 2]]
m2 = [[3, 4]]
m1.extend(m2)
m1 += [[5, 6]]
print(m1)                               # [[1, 2], [3, 4], [5, 6]]
print(m1[1] is m2[0])                   # True (shared, not copied)

# Program 9: Put two tables side by side
a = [[1, 2], [3, 4]]
b = [[5], [6]]
print([r1 + r2 for r1, r2 in zip(a, b)])        # [[1, 2, 5], [3, 4, 6]]

# Program 10: Remove empty rows
print([row for row in [[1], [], [2, 3], []] if row])    # [[1], [2, 3]]


# =====================================================
# Concept 8: The Famous Trap [[0] * 3] * 3
# =====================================================
"""
Definition:
list * n repeats the SAME object n times, it does not copy it.
[0] * 3 is safe because the items are numbers (immutable).
[[0] * 3] * 3 repeats the same inner LIST three times, so all three
rows are ONE row seen three times. Changing a cell changes "all rows".
Build the rows separately with a comprehension: [[0] * 3 for _ in range(3)]
"""

# Program 1: The trap
bad = [[0] * 3] * 3
bad[0][0] = 1
print(bad)                              # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]
print(bad[0] is bad[1] is bad[2])       # True
print(len(set(map(id, bad))))           # 1 (only one row object exists)

# Program 2: The correct way
good = [[0] * 3 for _ in range(3)]
good[0][0] = 1
print(good)                             # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
print(len(set(map(id, good))))          # 3 (three different rows)

# Program 3: Replacing a WHOLE row is safe, only cell changes are shared
bad = [[0] * 2] * 2
bad[0] = [9, 9]
print(bad)                              # [[9, 9], [0, 0]]

# Program 4: The same trap with append() in a loop
row = []
table = []
for i in range(3):
    row.append(i)
    table.append(row)                   # the SAME row object every time
print(table)                            # [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# Program 5: The fix, create a NEW row in every round
table = []
for i in range(3):
    row = []
    for j in range(i + 1):
        row.append(j)
    table.append(row)
print(table)                            # [[0], [0, 1], [0, 1, 2]]

# Program 6: Empty rows
bad = [[]] * 3
bad[0].append("x")
print(bad)                              # [['x'], ['x'], ['x']]
good = [[] for _ in range(3)]
good[0].append("x")
print(good)                             # [['x'], [], []]

# Program 7: Build rows from a template with a copy
template = [0, 0, 0]
grid = [template[:] for _ in range(2)]
grid[0][0] = 5
print(grid)                             # [[5, 0, 0], [0, 0, 0]]


# =====================================================
# Concept 9: Copying Nested Lists
# =====================================================
"""
Definition:
b = a                    -> no copy, a second name
a.copy(), a[:], list(a)  -> SHALLOW copy: a new OUTER list, but the
                            ROWS are the same objects
[row[:] for row in a]    -> copies the rows too (enough for 2 levels)
copy.deepcopy(a)         -> copies every level, whatever the depth
Immutable items (numbers, strings) are shared safely, they cannot change.
"""

# Program 1: Who is the same object?
a = [[1, 2], [3, 4]]
alias = a
shallow = a.copy()
deep = copy.deepcopy(a)
print(alias is a, shallow is a, deep is a)          # True False False
print(shallow[0] is a[0], deep[0] is a[0])          # True False

# Program 2: A change through the shallow copy reaches the original
shallow[0].append(99)
print(a)                                # [[1, 2, 99], [3, 4]]
print(shallow)                          # [[1, 2, 99], [3, 4]]
print(deep)                             # [[1, 2], [3, 4]]

# Program 3: Replacing a whole row in the copy does not touch the original
a = [[1, 2], [3, 4]]
shallow = a[:]
shallow[0] = ["new"]
print(a)                                # [[1, 2], [3, 4]]
print(shallow)                          # [['new'], [3, 4]]

# Program 4: All three shallow copies share the rows
a = [[1, 2], [3, 4]]
copies = [a.copy(), a[:], list(a)]
print(all(c[0] is a[0] for c in copies))        # True

# Program 5: Copy each row (2 levels are enough)
a = [[1, 2], [3, 4]]
rows_copied = [row[:] for row in a]
rows_copied[0].append(7)
print(a)                                # [[1, 2], [3, 4]]
print(rows_copied)                      # [[1, 2, 7], [3, 4]]

# Program 6: With 3 levels, copying only the rows is NOT enough
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
planes_copied = [plane[:] for plane in cube]
print(planes_copied[0][0] is cube[0][0])                # True (still shared)
print(copy.deepcopy(cube)[0][0] is cube[0][0])          # False

# Program 7: Numbers are shared even by deepcopy, they can never change
deep = copy.deepcopy([[1, 2]])
print(deep[0][0] is 1 if False else deep[0] == [1, 2])  # True


# =====================================================
# Concept 10: Rows are Objects (Names and Sharing)
# =====================================================
"""
Definition:
A row is a list object. A name that points to a row (row = m[0], or
the loop variable of "for row in m") works on the SAME row.
Changing the row's content changes the matrix. Giving the name a NEW
list only moves the name.
"""

# Program 1: Changing through a name
m = [[1, 2], [3, 4]]
row = m[0]
row[0] = 100
print(m)                                # [[100, 2], [3, 4]]

# Program 2: Giving the name a new list changes nothing in m
row = [0, 0]
print(m)                                # [[100, 2], [3, 4]]

# Program 3: Unpacking gives names to the rows
m = [[1, 2], [3, 4]]
first, second = m
first.append(9)
print(m)                                # [[1, 2, 9], [3, 4]]

# Program 4: A sorted outer list still holds the same rows
m = [[3, 1], [2, 5]]
reordered = sorted(m)
print(reordered)                        # [[2, 5], [3, 1]]
reordered[0].append("x")
print(m)                                # [[3, 1], [2, 5, 'x']]


# =====================================================
# Concept 11: Slicing Nested Lists
# =====================================================
"""
Definition:
A slice of the OUTER list gives rows (and the rows are shared).
A slice of a ROW gives part of that row.
Slicing cannot give a COLUMN, build it with a comprehension.
m[:][0] is NOT a column, it is the first row.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Program 1: Slices of rows
print(m[1:])                            # [[4, 5, 6], [7, 8, 9]]
print(m[:2])                            # [[1, 2, 3], [4, 5, 6]]
print(m[::-1])                          # [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

# Program 2: Slices inside a row
print(m[1][1:])                         # [5, 6]
print(m[0][::2])                        # [1, 3]
print(m[2][::-1])                       # [9, 8, 7]

# Program 3: A column, and the common mistake
print([row[0] for row in m])            # [1, 4, 7]
print([row[-1] for row in m])           # [3, 6, 9]
print(m[:][0])                          # [1, 2, 3] (the first ROW, not a column)

# Program 4: A part of the matrix (a sub-matrix)
print([row[:2] for row in m[:2]])       # [[1, 2], [4, 5]] (top left)
print([row[1:] for row in m[1:]])       # [[5, 6], [8, 9]] (bottom right)

# Program 5: Reverse the rows of text inside, and everything
print([row[::-1] for row in m])         # [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print([row[::-1] for row in m[::-1]])   # [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

# Program 6: Rotate by 90 degrees
print([list(col) for col in zip(*m[::-1])])     # [[7, 4, 1], [8, 5, 2], [9, 6, 3]] (clockwise)
print([list(col) for col in zip(*m)][::-1])     # [[3, 6, 9], [2, 5, 8], [1, 4, 7]] (counter-clockwise)

# Program 7: A slice of rows shares the rows
data = [[1, 2], [3, 4], [5, 6]]
part = data[:2]
part[0].append(99)
print(data)                             # [[1, 2, 99], [3, 4], [5, 6]]
print(part is data, part[0] is data[0]) # False True

# Program 8: Slice assignment replaces rows
data = [[1, 2], [3, 4], [5, 6]]
data[1:2] = [[0, 0], [1, 1]]
print(data)                             # [[1, 2], [0, 0], [1, 1], [5, 6]]


# =====================================================
# Concept 12: Flattening (and the Opposite)
# =====================================================
"""
Definition:
Flattening turns a list of lists into one simple list.
Order of the for parts in a comprehension: the OUTER loop comes first.
sum(nested, []) also works but is slow on big data (it builds a new
list at every step).
For lists nested to ANY depth, open the inner lists in a while loop.
"""

nested = [[1, 2], [3], [4, 5, 6]]

# Program 1: Two loops
flat = []
for row in nested:
    for item in row:
        flat.append(item)
print(flat)                             # [1, 2, 3, 4, 5, 6]

# Program 2: A comprehension
print([x for row in nested for x in row])       # [1, 2, 3, 4, 5, 6]

# Program 3: itertools.chain
print(list(chain.from_iterable(nested)))        # [1, 2, 3, 4, 5, 6]

# Program 4: extend() in a loop
flat = []
for row in nested:
    flat.extend(row)
print(flat)                             # [1, 2, 3, 4, 5, 6]

# Program 5: sum() with a start list (short, but slow for big lists)
print(sum(nested, []))                  # [1, 2, 3, 4, 5, 6]

# Program 6: Any depth, with a while loop
data = [1, [2, [3, [4]], 5], 6]
flat = []
todo = data[:]
while todo:
    item = todo.pop(0)
    if isinstance(item, list):
        todo = item + todo              # open the inner list, its items go to the front
    else:
        flat.append(item)
print(flat)                             # [1, 2, 3, 4, 5, 6]
print(data)                             # [1, [2, [3, [4]], 5], 6] (unchanged)

# Program 7: Strings are not opened (we only open real lists)
data = ["ab", ["cd", ["e"]]]
flat = []
todo = data[:]
while todo:
    item = todo.pop(0)
    if isinstance(item, list):
        todo = item + todo
    else:
        flat.append(item)
print(flat)                             # ['ab', 'cd', 'e']

# Program 8: Flatten, then work with the items
print(sum(len(row) for row in nested))                  # 6
print(sorted(set(x for row in nested for x in row)))    # [1, 2, 3, 4, 5, 6]
print(list(dict.fromkeys(x for row in [[1, 2], [2, 3], [1]] for x in row)))     # [1, 2, 3]

# Program 9: The opposite, cut a flat list into rows of 3
flat = list(range(1, 10))
print([flat[i:i + 3] for i in range(0, len(flat), 3)])  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# =====================================================
# Concept 13: Transpose (Rows become Columns)
# =====================================================
"""
Definition:
The transpose of a matrix swaps rows and columns: the cell m[i][j]
becomes t[j][i]. zip(*m) does it in one step (it gives tuples, wrap
every one in list()). zip stops at the SHORTEST row, so uneven rows
lose items; zip_longest keeps them.
"""

m = [[1, 2, 3], [4, 5, 6]]

# Program 1: zip(*m)
print(list(zip(*m)))                    # [(1, 4), (2, 5), (3, 6)]
print([list(col) for col in zip(*m)])   # [[1, 4], [2, 5], [3, 6]]

# Program 2: A comprehension with indexes
print([[row[j] for row in m] for j in range(len(m[0]))])        # [[1, 4], [2, 5], [3, 6]]

# Program 3: With loops
rows, columns = len(m), len(m[0])
result = [[0] * rows for _ in range(columns)]
for i in range(rows):
    for j in range(columns):
        result[j][i] = m[i][j]
print(result)                           # [[1, 4], [2, 5], [3, 6]]

# Program 4: Transposing twice gives the original
t = [list(col) for col in zip(*m)]
back = [list(col) for col in zip(*t)]
print(back == m)                        # True

# Program 5: A symmetric matrix equals its transpose
s = [[1, 2], [2, 1]]
print(s == [list(col) for col in zip(*s)])      # True

# Program 6: Uneven rows
uneven = [[1, 2, 3], [4, 5]]
print(list(zip(*uneven)))               # [(1, 4), (2, 5)] (the 3 is lost)
print(list(zip_longest(*uneven)))       # [(1, 4), (2, 5), (3, None)]

# Program 7: The columns of a table
table = [["Name", "Score"], ["Ali", 90], ["Sara", 85]]
columns = list(zip(*table))
print(columns)                          # [('Name', 'Ali', 'Sara'), ('Score', 90, 85)]
print(columns[0][1:])                   # ('Ali', 'Sara')


# =====================================================
# Concept 14: Matrix Calculations
# =====================================================
"""
Definition:
Totals, row and column sums, the diagonal, adding matrices,
multiplying by a number and multiplying two matrices are the usual
exercises. Matrix multiplication: result[i][j] is the sum of
a[i][k] * b[k][j] over k.
"""

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]

# Program 1: Total, row sums and column sums
print(sum(sum(row) for row in a))               # 10
print([sum(row) for row in a])                  # [3, 7]
print([sum(col) for col in zip(*a)])            # [4, 6]

# Program 2: Biggest and smallest of all cells
print(max(max(row) for row in a))               # 4
print(min(x for row in a for x in row))         # 1

# Program 3: Diagonals of a square matrix
n = len(a)
print([a[i][i] for i in range(n)])              # [1, 4]
print([a[i][n - 1 - i] for i in range(n)])      # [2, 3]
print(sum(a[i][i] for i in range(n)))           # 5

# Program 4: Add two matrices
print([[x + y for x, y in zip(r1, r2)] for r1, r2 in zip(a, b)])        # [[6, 8], [10, 12]]

# Program 5: Multiply by a number
print([[x * 3 for x in row] for row in a])      # [[3, 6], [9, 12]]

# Program 6: Matrix multiplication with three loops
result = [[0] * len(b[0]) for _ in range(len(a))]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
print(result)                           # [[19, 22], [43, 50]]

# Program 7: The same with a comprehension
product = [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]
print(product == result)                # True

# Program 8: The identity matrix
identity = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
print(identity)                         # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Program 9: A times the identity is A
identity2 = [[1, 0], [0, 1]]
print([[sum(x * y for x, y in zip(row, col)) for col in zip(*identity2)] for row in a] == a)    # True

# Program 10: Averages
print([sum(row) / len(row) for row in a])               # [1.5, 3.5]
print([sum(col) / len(col) for col in zip(*a)])         # [2.0, 3.0]


# =====================================================
# Concept 15: Searching in Nested Lists
# =====================================================
"""
Definition:
"x in m" only looks at the ROWS (the items of the outer list), not
inside them. To look at the cells, loop over the rows or use
any(x in row for row in m).
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Program 1: in looks at the rows
print(5 in m)                           # False
print([4, 5, 6] in m)                   # True
print(any(5 in row for row in m))       # True

# Program 2: The first position of a value
target = 6
for i, row in enumerate(m):
    if target in row:
        print("found in row", i, "column", row.index(target))      # row 1 column 2
        break
else:
    print("not found")

# Program 3: Every position that matches
print([(i, j) for i, row in enumerate(m) for j, v in enumerate(row) if v % 2 == 0])
# [(0, 1), (1, 0), (1, 2), (2, 1)]

# Program 4: Count a value in all rows
print(sum(row.count(5) for row in [[5, 1], [5, 5]]))    # 3

# Program 5: The rows that contain a value
print([row for row in m if 5 in row])   # [[4, 5, 6]]
print(m.index([4, 5, 6]))               # 1 (the position of that row)

# Program 6: The row with the biggest sum, and the biggest cell with its position
print(max(m, key=sum))                  # [7, 8, 9]
print(m.index(max(m, key=sum)))         # 2
best = None
best_position = None
for i, row in enumerate(m):
    for j, v in enumerate(row):
        if best is None or v > best:
            best = v
            best_position = (i, j)
print(best, best_position)              # 9 (2, 2)

# Program 7: Checks on all rows
print(all(len(row) == 3 for row in m))  # True
print(any(0 in row for row in m))       # False

# Program 8: Look up a record
people = [["Ali", "Lahore"], ["Sara", "Karachi"]]
print(next((r[1] for r in people if r[0] == "Sara"), None))     # Karachi
print(next((r[1] for r in people if r[0] == "Zed"), None))      # None


# =====================================================
# Concept 16: Sorting Nested Lists
# =====================================================
"""
Definition:
sorted(rows) compares rows item by item (first item, then the second
if equal, and so on). Use key= to sort by a column. Sorting is
stable, so equal keys keep their order. The compared items must be
of comparable types.
"""

rows = [["Sara", 22], ["Ali", 25], ["Bilal", 22]]

# Program 1: Default order
print(sorted(rows))                     # [['Ali', 25], ['Bilal', 22], ['Sara', 22]]

# Program 2: By one column (Sara stays before Bilal because she was first)
print(sorted(rows, key=lambda r: r[1])) # [['Sara', 22], ['Bilal', 22], ['Ali', 25]]

# Program 3: Age descending, then name
print(sorted(rows, key=lambda r: (-r[1], r[0])))        # [['Ali', 25], ['Bilal', 22], ['Sara', 22]]

# Program 4: Sort in place by name
rows.sort(key=lambda r: r[0])
print(rows)                             # [['Ali', 25], ['Bilal', 22], ['Sara', 22]]

# Program 5: Sort the items inside every row
m = [[3, 1, 2], [9, 7, 8]]
print([sorted(r) for r in m])           # [[1, 2, 3], [7, 8, 9]] (new lists)
for row in m:
    row.sort()
print(m)                                # [[1, 2, 3], [7, 8, 9]] (changed in place)

# Program 6: By the sum or by the length of a row
print(sorted([[5, 5], [1], [2, 2, 2]], key=sum))        # [[1], [2, 2, 2], [5, 5]]
print(sorted([[5, 5], [1], [2, 2, 2]], key=len))        # [[1], [5, 5], [2, 2, 2]]

# Program 7: Find the column from the header name
header = ["Name", "Score"]
data = [["Ali", 90], ["Sara", 85], ["Bilal", 95]]
col = header.index("Score")
print(sorted(data, key=lambda r: r[col], reverse=True)) # [['Bilal', 95], ['Ali', 90], ['Sara', 85]]

# Program 8: A column that mixes numbers and text cannot be sorted
try:
    sorted([["a", 1], ["b", "x"]], key=lambda r: r[1])
except TypeError:
    print("TypeError: the column mixes numbers and text")

# Program 9: Numbers stored as text need int()
print(sorted([["a", "10"], ["b", "9"]], key=lambda r: int(r[1])))       # [['b', '9'], ['a', '10']]


# =====================================================
# Concept 17: Unpacking Nested Lists
# =====================================================
"""
Definition:
Unpacking splits a list into names. It also works on the inner level
with brackets: (x, y), (z, w) = [[1, 2], [3, 4]].
A name with * collects the rest. The number of names must match.
"""

# Program 1: Rows into names
a, b = [[1, 2], [3, 4]]
print(a, b)                             # [1, 2] [3, 4]

# Program 2: Rows and cells at once
(x, y), (z, w) = [[1, 2], [3, 4]]
print(x, y, z, w)                       # 1 2 3 4

# Program 3: In a for line
for name, (px, py) in [("A", (1, 2)), ("B", (3, 4))]:
    print(name, px, py)                 # A 1 2   B 3 4

# Program 4: Header and rows
table = [["Name", "Score"], ["Ali", 90], ["Sara", 85]]
header, *rows = table
print(header)                           # ['Name', 'Score']
print(rows)                             # [['Ali', 90], ['Sara', 85]]
first, *middle, last = [[1, 2], [3, 4], [5, 6]]
print(first, middle, last)              # [1, 2] [[3, 4]] [5, 6]

# Program 5: Print a matrix with *
for row in [[1, 2], [3, 4], [5, 6]]:
    print(*row)                         # 1 2   3 4   5 6

# Program 6: Join rows with *
m = [[1, 2], [3, 4]]
print([*m[0], *m[1]])                   # [1, 2, 3, 4]

# Program 7: Wrong number of names
try:
    a, b, c = [[1], [2]]
except ValueError as e:
    print("Error:", e)                  # not enough values to unpack (expected 3, got 2)

# Program 8: Unpacking in a comprehension
print([x + y for x, y in [[1, 2], [3, 4]]])             # [3, 7]
print([first for first, *rest in [[1, 2, 3], [4, 5]]])  # [1, 4]


# =====================================================
# Concept 18: Jagged (Uneven) Lists
# =====================================================
"""
Definition:
In a jagged list the rows have different lengths. A fixed column
index can fail with IndexError. Check the length first, or pad the
short rows with a filler value.
"""

jagged = [[1], [2, 3], [4, 5, 6]]

# Program 1: Row lengths
print([len(row) for row in jagged])     # [1, 2, 3]
print(max(len(row) for row in jagged))  # 3

# Program 2: The error
try:
    print(jagged[0][1])
except IndexError as e:
    print("Error:", e)                  # list index out of range

# Program 3: Read a cell safely
for i, j in [(2, 1), (0, 1), (5, 0)]:
    if 0 <= i < len(jagged) and 0 <= j < len(jagged[i]):
        print((i, j), "->", jagged[i][j])       # (2, 1) -> 5
    else:
        print((i, j), "-> no such cell")

# Program 4: Pad every row to the same length
width = max(len(row) for row in jagged)
print([row + [0] * (width - len(row)) for row in jagged])       # [[1, 0, 0], [2, 3, 0], [4, 5, 6]]

# Program 5: A column of the rows that have it
print([row[1] for row in jagged if len(row) > 1])       # [3, 5]

# Program 6: Pascal's triangle is jagged on purpose
triangle = [[1]]
for i in range(1, 5):
    previous = triangle[-1]
    row = [1]
    for j in range(1, i):
        row.append(previous[j - 1] + previous[j])
    row.append(1)
    triangle.append(row)
print(triangle)                         # [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


# =====================================================
# Concept 19: Other Nested Shapes
# =====================================================
"""
Definition:
Lists nest with other types too: lists of tuples, lists of
dictionaries, dictionaries of lists, and the JSON-like data that APIs
return. Read them one level at a time: users[0]["roles"][1].
"""

# Program 1: A list of tuples
points = [(1, 2), (3, 4)]
print([p[0] for p in points], [p[1] for p in points])           # [1, 3] [2, 4]

# Program 2: A list of dictionaries that hold lists
users = [
    {"name": "Ali", "roles": ["admin", "tester"]},
    {"name": "Sara", "roles": ["tester"]},
]
print(users[0]["roles"][1])             # tester
print([u["name"] for u in users if "admin" in u["roles"]])      # ['Ali']
print(sum(len(u["roles"]) for u in users))                      # 3

# Program 3: A dictionary of lists
scores = {"Ali": [90, 80], "Sara": [85, 95]}
print({name: sum(v) / len(v) for name, v in scores.items()})    # {'Ali': 85.0, 'Sara': 90.0}
print(scores["Ali"][-1])                # 80
print([s for v in scores.values() for s in v])                  # [90, 80, 85, 95]

# Program 4: JSON-like data
data = {"status": "ok", "items": [{"id": 1, "tags": ["a", "b"]}, {"id": 2, "tags": []}]}
print(data["items"][0]["tags"][-1])     # b
print(sum(len(i["tags"]) for i in data["items"]))               # 2
print([i["id"] for i in data["items"] if not i["tags"]])        # [2]

# Program 5: A 3D list
cube = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print([sum(sum(row) for row in plane) for plane in cube])       # [10, 26]
print([x for plane in cube for row in plane for x in row])      # [1, 2, 3, 4, 5, 6, 7, 8]

# Program 6: Group items into lists
groups = {}
for name, group in [("Ali", "A"), ("Sara", "B"), ("Bilal", "A")]:
    groups.setdefault(group, []).append(name)
print(groups)                           # {'A': ['Ali', 'Bilal'], 'B': ['Sara']}

# Program 7: A tuple inside a list cannot change, but its place can be replaced
pairs = [(1, 2)]
try:
    pairs[0][0] = 9
except TypeError as e:
    print("Error:", e)                  # 'tuple' object does not support item assignment
pairs[0] = (9, 2)
print(pairs)                            # [(9, 2)]


# =====================================================
# Concept 20: Printing Nested Lists Nicely
# =====================================================
"""
Definition:
print(m) shows everything in one line. For readable output print one
row per line, use * to drop the brackets, align the cells with
rjust()/ljust() or f-string widths, or use pprint for long data.
"""

# Program 1: Three styles
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(m)                                # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in m:
    print(row)                          # [1, 2, 3] ...
for row in m:
    print(*row)                         # 1 2 3 ...

# Program 2: Cells of different widths
m2 = [[1, 200, 3], [40, 5, 6000]]
width = max(len(str(x)) for row in m2 for x in row)
print(width)                            # 4
for row in m2:
    print(" ".join(str(x).rjust(width) for x in row))
#    1  200    3
#   40    5 6000

# Program 3: A table with a header and a width for every column
table = [["Name", "Score"], ["Ali", 90], ["Sara", 85]]
widths = [max(len(str(row[j])) for row in table) for j in range(len(table[0]))]
print(widths)                           # [4, 5]
for row in table:
    print(" | ".join(str(cell).ljust(w) for cell, w in zip(row, widths)))

# Program 4: pprint puts a long structure on several lines
pprint([[1, 2, 3, 4], [5, 6, 7, 8]], width=20)          # one row per line

# Program 5: Numbered rows
for number, row in enumerate(table[1:], start=1):
    print(f"{number}. {row[0]} -> {row[1]}")


# =====================================================
# Concept 21: Comparing Nested Lists
# =====================================================
"""
Definition:
== compares nested lists level by level, so the order of the rows AND
the order inside every row matter. To ignore the order, sort first.
zip() stops at the shortest list, so compare the LENGTHS as well.
Lists cannot be put into a set (they are not hashable), turn the rows
into tuples first.
"""

# Program 1: Equality
print([[1, 2], [3, 4]] == [[1, 2], [3, 4]])     # True
print([[1, 2], [3, 4]] == [[3, 4], [1, 2]])     # False (another row order)

# Program 2: Ignore the order of the rows
print(sorted([[3, 4], [1, 2]]) == sorted([[1, 2], [3, 4]]))     # True

# Program 3: Ignore the order of the rows AND inside the rows
left = sorted(sorted(r) for r in [[2, 1], [4, 3]])
right = sorted(sorted(r) for r in [[3, 4], [1, 2]])
print(left == right)                    # True

# Program 4: == vs is
a = [[1, 2]]
b = [[1, 2]]
print(a == b, a is b, a[0] is b[0])     # True False False

# Program 5: Where is the difference?
expected = [[1, 2], [3, 4]]
actual = [[1, 2], [3, 5]]
for i, (e_row, a_row) in enumerate(zip(expected, actual)):
    for j, (e, a) in enumerate(zip(e_row, a_row)):
        if e != a:
            print(f"cell [{i}][{j}]: expected {e}, got {a}")        # cell [1][1]: expected 4, got 5

# Program 6: Floats need a tolerance
print([[0.1 + 0.2]] == [[0.3]])         # False
x = [[0.1 + 0.2]]
y = [[0.3]]
print(all(abs(p - q) < 1e-9 for r1, r2 in zip(x, y) for p, q in zip(r1, r2)))       # True

# Program 7: zip hides missing rows, so check the lengths too
expected = [[1, 2], [3, 4]]
actual = [[1, 2]]
differences = [1 for e_row, a_row in zip(expected, actual) if e_row != a_row]
print(len(differences))                 # 0 (no difference found!)
print(len(expected) == len(actual))     # False (the missing row is found only here)

# Program 8: Remove duplicate rows, the order is kept
try:
    {[1, 2]}
except TypeError as e:
    print("Error:", e)                  # unhashable type: 'list'
rows = [[1, 2], [3, 4], [1, 2]]
unique = [list(t) for t in dict.fromkeys(tuple(r) for r in rows)]
print(unique)                           # [[1, 2], [3, 4]]


# =====================================================
# Concept 22: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with nested lists:
1) [[0] * 3] * 3 repeats ONE row
2) the wrong index order, m[column][row]
3) thinking m[:][0] is a column
4) thinking "x in m" looks inside the rows
5) believing copy() or [:] copies the rows
6) using len(m) as the number of columns
7) reading m[0] of an empty matrix
8) sum(nested) for flattening without the [] start value
"""

m = [[1, 2, 3], [4, 5, 6]]

# Program 1: The same row repeated
grid = [[0] * 2] * 2
grid[0][0] = 7
print(grid)                             # [[7, 0], [7, 0]]

# Program 2: The index order is row first
print(m[1][2])                          # 6
try:
    print(m[2][1])
except IndexError as e:
    print("Error:", e)                  # list index out of range

# Program 3: A column needs a comprehension
print(m[:][0])                          # [1, 2, 3] (a row)
print([row[0] for row in m])            # [1, 4] (the column)

# Program 4: "in" looks at rows only
print(5 in m, any(5 in row for row in m))       # False True

# Program 5: A shallow copy shares the rows
copy_of_m = m[:]
copy_of_m[0][0] = 99
print(m)                                # [[99, 2, 3], [4, 5, 6]]

# Program 6: Rows and columns
print(len(m), len(m[0]))                # 2 3

# Program 7: An empty matrix
empty = []
print(len(empty[0]) if empty else "no rows")    # no rows

# Program 8: sum() needs [] as start value for lists
try:
    print(sum([[1], [2]]))
except TypeError as e:
    print("Error:", e)                  # unsupported operand type(s) for +: 'int' and 'list'
print(sum([[1], [2]], []))              # [1, 2]


# =====================================================
# Concept 23: Nested Lists in SQA Automation
# =====================================================
"""
Definition:
A table on a web page, the rows of a CSV file, the results of tests
on several browsers, and parsed log lines are all nested lists.
Typical jobs: find the column by the header NAME (not by a fixed
number), compare two tables cell by cell with the row and column in
the message, count results per browser, and check test data.
Real Playwright code (not executed here): the text of a table row is
usually its cells separated by tabs:
    row_texts = page.locator("table tr").all_inner_texts()
    cells = [text.split("\\t") for text in row_texts]
"""

# Program 1: Read a column by its header name
table_texts = [
    ["Name", "Email", "Status"],
    ["Ali", "ali@example.com", "Active"],
    ["Sara", "sara@example.com", "Inactive"],
    ["Bilal", "bilal@example.com", "Active"],
]
header, *rows = table_texts
status_column = header.index("Status")
statuses = [row[status_column] for row in rows]
print(statuses)                         # ['Active', 'Inactive', 'Active']
print(f"{statuses.count('Active')} of {len(rows)} users are active")        # 2 of 3 users are active

# Program 2: Turn the rows into records
records = [dict(zip(header, row)) for row in rows]
print(records[1])       # {'Name': 'Sara', 'Email': 'sara@example.com', 'Status': 'Inactive'}
print(next((r["Email"] for r in records if r["Name"] == "Bilal"), None))    # bilal@example.com

# Program 3: Check the structure of a table
for label, check_rows in (("clean", rows),
                          ("broken", [["Ali", "", "Active"], ["Sara", "sara@example.com"]])):
    problems = []
    for row_number, row in enumerate(check_rows, start=1):
        if len(row) != len(header):
            problems.append(f"row {row_number}: wrong number of cells")
        for column_number, cell in enumerate(row, start=1):
            if not cell.strip():
                problems.append(f"row {row_number}, column {column_number}: empty cell")
    print(label, problems)
# clean []
# broken ['row 1, column 2: empty cell', 'row 2: wrong number of cells']

# Program 4: Expected vs actual table, cell by cell
expected_table = [["Ali", "Active"], ["Sara", "Inactive"]]
actual_table = [["Ali ", "Active"], ["Sara", "Active"]]
failures = []
if len(expected_table) != len(actual_table):
    failures.append("different number of rows")
for r, (e_row, a_row) in enumerate(zip(expected_table, actual_table), start=1):
    for c, (e, a) in enumerate(zip(e_row, a_row), start=1):
        if e != " ".join(a.split()):
            failures.append(f"row {r}, column {c}: expected {e!r}, got {a!r}")
print(failures)                         # ["row 2, column 2: expected 'Inactive', got 'Active'"]

# Program 5: Test results on several browsers
browsers = ["chromium", "firefox", "webkit"]
results = [
    ["login", "PASS", "PASS", "FAIL"],
    ["cart", "PASS", "FAIL", "FAIL"],
    ["search", "PASS", "PASS", "PASS"],
]
per_browser = {b: sum(1 for row in results if row[j] == "PASS")
               for j, b in enumerate(browsers, start=1)}
print(per_browser)                      # {'chromium': 3, 'firefox': 2, 'webkit': 1}
print([(row[0], browsers[j - 1]) for row in results for j in range(1, len(row)) if row[j] == "FAIL"])
# [('login', 'webkit'), ('cart', 'firefox'), ('cart', 'webkit')]
for row in results:
    print(f"{row[0]:<8}{row[1:].count('PASS')}/{len(row) - 1}")     # login 2/3   cart 1/3   search 3/3

# Program 6: CSV text into nested lists
csv_text = "name,age,city\nAli,25,Lahore\nSara,22,Karachi"
csv_rows = [line.split(",") for line in csv_text.splitlines()]
csv_header, *csv_data = csv_rows
typed = [[name, int(age), city] for name, age, city in csv_data]
print(typed)                            # [['Ali', 25, 'Lahore'], ['Sara', 22, 'Karachi']]
print(sum(r[1] for r in typed) / len(typed))    # 23.5

# Program 7: Log lines into rows
log_lines = [
    "2026-10-17 10:00:01 [PASS] login ok",
    "2026-10-17 10:00:05 [ERROR] database down",
    "2026-10-17 10:00:15 [FAIL] cart button missing",
]
parsed = [line.split(maxsplit=3) for line in log_lines]
print(parsed[1])                        # ['2026-10-17', '10:00:05', '[ERROR]', 'database down']
print([(row[1], row[3]) for row in parsed if row[2] in ("[ERROR]", "[FAIL]")])
# [('10:00:05', 'database down'), ('10:00:15', 'cart button missing')]

# Program 8: Data driven test data
login_data = [
    ["admin", "Admin@123", "success"],
    ["admin", "wrong", "error"],
    ["", "Admin@123", "error"],
    ["admin", "wrong", "error"],
]
print(all(len(row) == 3 for row in login_data))        # True
unique_rows = [list(t) for t in dict.fromkeys(tuple(row) for row in login_data)]
print(len(login_data), len(unique_rows))               # 4 3
for username, password, expected in unique_rows:
    print(f"user={username!r:<8} expected={expected}")

# Program 9: Pages of results (the last page is shorter)
items = list(range(1, 11))
pages = [items[i:i + 4] for i in range(0, len(items), 4)]
print(pages)                            # [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]
print(len(pages), len(pages[-1]))       # 3 2

# Program 10: A menu with sub menus
menu = {"Products": ["Laptops", "Phones"], "Support": ["FAQ", "Contact"]}
all_links = [link for sub in menu.values() for link in sub]
print(all_links)                        # ['Laptops', 'Phones', 'FAQ', 'Contact']
print("PASS" if len(all_links) == 4 else "FAIL", "- expected 4 links")

# Program 11: Screenshot names for every test on every browser
tests = ["login", "cart"]
two_browsers = ["chromium", "firefox"]
names = [[f"{t}_{b}.png" for b in two_browsers] for t in tests]
print(names)        # [['login_chromium.png', 'login_firefox.png'], ['cart_chromium.png', 'cart_firefox.png']]
print(len([n for row in names for n in row]))   # 4

# Program 12: Cells from the text of table rows (the tab separated format of Playwright)
row_texts = ["Name\tEmail\tStatus", "Ali\tali@example.com\tActive"]
cells = [text.split("\t") for text in row_texts]
print(cells)                            # [['Name', 'Email', 'Status'], ['Ali', 'ali@example.com', 'Active']]