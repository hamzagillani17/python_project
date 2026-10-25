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








































































