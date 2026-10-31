"""
====================================================
10_Lists / 06_list_sorting_reversing.py
====================================================
Topic: Sorting and Reversing Lists
====================================================
Notes before you run this file:
1) Five tools are used here:
   sort()    method    sorts the list IN PLACE and returns None
   sorted()  function  returns a NEW sorted list, works on any iterable
   reverse() method    flips the CURRENT order IN PLACE and returns None
   reversed() function gives an ITERATOR that walks backwards
   [::-1]    slice     returns a NEW reversed list
2) reverse() does NOT sort. It only turns the list around.
3) The key= parameter takes a FUNCTION without brackets: key=len, not key=len()
4) sort() and sorted() always need items that can be compared with
   each other (numbers with numbers, text with text).
5) Plain programs only, no functions.
"""

import re
import heapq
from operator import itemgetter


# =====================================================
# Concept 1: Overview of the Five Tools
# =====================================================
"""
Definition:
sort()       -> in place, returns None, only for lists
sorted()     -> new list, any iterable
reverse()    -> in place, returns None, turns the order around
reversed()   -> iterator, any sequence
[::-1]       -> new reversed list
"""

# Program 1: The same list with all five tools
nums = [3, 1, 2]
a = nums.copy()
a.sort()
print(a)                                # [1, 2, 3]
print(sorted(nums))                     # [1, 2, 3]
b = nums.copy()
b.reverse()
print(b)                                # [2, 1, 3] (turned around, not sorted)
print(list(reversed(nums)))             # [2, 1, 3]
print(nums[::-1])                       # [2, 1, 3]
print(nums)                             # [3, 1, 2] (the original is still the same)

# Program 2: Which ones return None
print(a.sort())                         # None
print(b.reverse())                      # None
print(sorted(nums))                     # [1, 2, 3] (a real list)

# Program 3: Only a list has the sort() and reverse() methods
print(hasattr([], "sort"), hasattr((), "sort"), hasattr("", "sort"))    # True False False


# =====================================================
# Concept 2: sort()
# =====================================================
"""
Definition:
my_list.sort() puts the items in ascending order (small to big,
A to Z) and changes the list itself. It returns None.
sort() accepts only keyword arguments: key= and reverse=.
"""

# Program 1: Sort numbers
nums = [5, 2, 9, 1]
nums.sort()
print(nums)                             # [1, 2, 5, 9]

# Program 2: Sort strings
fruits = ["pear", "apple", "fig"]
fruits.sort()
print(fruits)                           # ['apple', 'fig', 'pear']

# Program 3: Integers, floats and negative numbers can be mixed
values = [3, -1, 2.5, 0, -7.25]
values.sort()
print(values)                           # [-7.25, -1, 0, 2.5, 3]

# Program 4: The return value is None
data = [3, 1, 2]
print(data.sort())                      # None

# Program 5: The same list object is changed
before = id(data)
data.sort()
print(before == id(data))               # True

# Program 6: sort() takes no positional arguments
try:
    data.sort(True)
except TypeError as e:
    print("Error:", e)                  # sort() takes no positional arguments


# =====================================================
# Concept 3: sorted()
# =====================================================
"""
Definition:
sorted(iterable) returns a NEW LIST with the sorted items. The
original is not changed. It accepts any iterable (list, tuple,
string, set, range, dictionary keys) and always returns a list.
"""

# Program 1: The original stays the same
nums = [3, 1, 2]
new_list = sorted(nums)
print(new_list, nums)                   # [1, 2, 3] [3, 1, 2]

# Program 2: Many kinds of iterables
print(sorted("hello"))                  # ['e', 'h', 'l', 'l', 'o']
print(sorted((3, 1, 2)))                # [1, 2, 3]
print(sorted({3, 1, 2}))                # [1, 2, 3]
print(sorted({"b": 1, "a": 2}))         # ['a', 'b'] (the keys)
print(sorted(range(5, 0, -1)))          # [1, 2, 3, 4, 5]

# Program 3: The result is always a list
print(type(sorted("abc")).__name__)     # list

# Program 4: Join the sorted characters back into a string
print("".join(sorted("hello")))         # ehllo
print(sorted("listen") == sorted("silent"))     # True (an anagram check)


# =====================================================
# Concept 4: sort() vs sorted()
# =====================================================
"""
Definition:
sort()   changes the list, returns None, only lists.
sorted() makes a new list, returns it, works on anything iterable.
Use sort() when you do not need the old order.
Use sorted() when the original must stay, or when the data is not a list.
"""

# Program 1: A second name for the list sees the change of sort() only
a = [3, 1, 2]
alias_a = a
a.sort()
print(alias_a)                          # [1, 2, 3] (changed)
b = [3, 1, 2]
alias_b = b
new = sorted(b)
print(alias_b, new)                     # [3, 1, 2] [1, 2, 3]

# Program 2: A tuple and a string have no sort()
t = (3, 1, 2)
try:
    t.sort()
except AttributeError as e:
    print("Error:", e)                  # 'tuple' object has no attribute 'sort'
print(sorted(t))                        # [1, 2, 3] (a list)

# Program 3: Keep the original order and also have a sorted view
original_order = ["login", "cart", "checkout"]
alphabetical = sorted(original_order)
print(original_order)                   # ['login', 'cart', 'checkout']
print(alphabetical)                     # ['cart', 'checkout', 'login']


# =====================================================
# Concept 5: reverse=True (Descending Order)
# =====================================================
"""
Definition:
reverse=True sorts from big to small (Z to A). It works with both
sort() and sorted(). It is NOT the same as the reverse() method.
"""

# Program 1: Descending numbers
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]

# Program 2: Descending strings with sort()
words = ["apple", "pear", "fig"]
words.sort(reverse=True)
print(words)                            # ['pear', 'fig', 'apple']

# Program 3: The 3 biggest and the 2 smallest scores
scores = [55, 90, 72, 88, 64]
print(sorted(scores, reverse=True)[:3]) # [90, 88, 72]
print(sorted(scores)[:2])               # [55, 64]

# Program 4: heapq does the same without sorting the whole list
print(heapq.nlargest(3, scores))        # [90, 88, 72]
print(heapq.nsmallest(2, scores))       # [55, 64]


# =====================================================
# Concept 6: Sorting Strings
# =====================================================
"""
Definition:
Strings are sorted by the Unicode number of their characters
(ord), so:
1) capital letters come BEFORE small letters (B before a)
2) space, digits and symbols come before letters
3) accented letters come after z
4) numbers written as text sort character by character ("10" < "9")
This is not the order of a dictionary of any language.
"""

# Program 1: Capitals first
words = ["banana", "Cherry", "apple", "Banana"]
print(sorted(words))                    # ['Banana', 'Cherry', 'apple', 'banana']
print(ord("B"), ord("a"))               # 66 97

# Program 2: Case-insensitive order with key=str.casefold
print(sorted(words, key=str.casefold))  # ['apple', 'banana', 'Banana', 'Cherry']

# Program 3: Accents come after z
print(sorted(["z", "é", "e", "E", "f"]))        # ['E', 'e', 'f', 'z', 'é']

# Program 4: Space, digits and symbols
print(sorted(["b", "B", "1", "_", "a", " "]))   # [' ', '1', 'B', '_', 'a', 'b']

# Program 5: Numbers written as text
texts = ["10", "9", "2"]
print(sorted(texts))                    # ['10', '2', '9'] (text order)
print(sorted(texts, key=int))           # ['2', '9', '10'] (number order, items stay text)

# Program 6: Urdu letters are sorted by code point, not by the Urdu alphabet
for ch in sorted(["پ", "ب", "ا"]):
    print(ch, hex(ord(ch)))             # ا 0x627, ب 0x628, پ 0x67e


# =====================================================
# Concept 7: The key Parameter
# =====================================================
"""
Definition:
key=function tells Python WHAT to compare. Python calls the function
once for every item, sorts by the results, and gives you back the
ORIGINAL items. The function is written WITHOUT brackets.
"""

# Program 1: Sort by length
print(sorted(["pear", "fig", "banana", "kiwi"], key=len))   # ['fig', 'pear', 'kiwi', 'banana']

# Program 2: Sort by absolute value
print(sorted([-5, 3, -1, 4], key=abs))  # [-1, 3, 4, -5]

# Program 3: A lambda picks the second element of each pair
pairs = [("a", 3), ("b", 1), ("c", 2)]
print(sorted(pairs, key=lambda p: p[1]))        # [('b', 1), ('c', 2), ('a', 3)]

# Program 4: Sort by the last letter
print(sorted(["ali", "sara", "bob"], key=lambda w: w[-1]))      # ['sara', 'bob', 'ali']

# Program 5: See what key calculates for each item
words = ["pear", "fig", "banana"]
for w in words:
    print(w, "->", len(w))              # pear -> 4, fig -> 3, banana -> 6

# Program 6: key needs the function itself, not a call
try:
    sorted(words, key=len())
except TypeError as e:
    print("Error:", e)                  # a TypeError, because len() was called without an argument

# Program 7: Sort ids by the number inside them
ids = ["TC_10", "TC_2", "TC_1"]
print(sorted(ids))                      # ['TC_1', 'TC_10', 'TC_2']
print(sorted(ids, key=lambda t: int(t.split("_")[1])))      # ['TC_1', 'TC_2', 'TC_10']


# =====================================================
# Concept 8: Sorting by Several Keys
# =====================================================
"""
Definition:
Let the key return a TUPLE. Python compares the first element, and
only if they are equal, the second, and so on.
For numbers, a minus sign gives descending order inside a tuple key.
Lists and tuples are compared item by item in the same way.
"""

# Program 1: Length first, then alphabetical
words = ["pear", "fig", "kiwi", "apple", "date"]
print(sorted(words, key=lambda w: (len(w), w)))     # ['fig', 'date', 'kiwi', 'pear', 'apple']

# Program 2: Score descending, then name ascending
students = [("Ali", 90), ("Sara", 85), ("Bilal", 90), ("Hina", 85)]
print(sorted(students, key=lambda s: (-s[1], s[0])))
# [('Ali', 90), ('Bilal', 90), ('Hina', 85), ('Sara', 85)]

# Program 3: Score descending, name DESCENDING (text cannot take a minus, so sort twice)
step1 = sorted(students, key=lambda s: s[0], reverse=True)      # name Z to A
step2 = sorted(step1, key=lambda s: s[1], reverse=True)         # then score big to small
print(step2)
# [('Bilal', 90), ('Ali', 90), ('Sara', 85), ('Hina', 85)]

# Program 4: itemgetter is a ready-made key function
print(sorted(students, key=itemgetter(1)))
# [('Sara', 85), ('Hina', 85), ('Ali', 90), ('Bilal', 90)]
print(sorted(students, key=itemgetter(1, 0)))
# [('Hina', 85), ('Sara', 85), ('Ali', 90), ('Bilal', 90)]

# Program 5: Sort rows (lists) by one column in place
rows = [["Ali", 25], ["Sara", 22], ["Bilal", 30]]
rows.sort(key=lambda r: r[1])
print(rows)                             # [['Sara', 22], ['Ali', 25], ['Bilal', 30]]

# Program 6: Lists compare item by item
print([1, 2] < [1, 3], [1, 2] < [1, 2, 0], [2] < [1, 9])        # True True False
print(sorted([[2, 1], [1, 5], [1, 2]]))                         # [[1, 2], [1, 5], [2, 1]]


# =====================================================
# Concept 9: Sort Stability
# =====================================================
"""
Definition:
Python's sort is STABLE: items with an equal key keep the same
relative order they had before. That is why you can sort in several
rounds: the LEAST important key first, the MOST important key last.
reverse=True also keeps this stability. The reverse() method does not,
because it flips everything.
"""

# Program 1: Equal keys keep their order
print(sorted(["bb", "a", "cc", "d"], key=len))      # ['a', 'd', 'bb', 'cc']

# Program 2: Two rounds, first by name, then by status
tests = [("login", "PASS"), ("cart", "FAIL"), ("search", "PASS"), ("payment", "FAIL")]
by_name = sorted(tests, key=lambda t: t[0])
by_status = sorted(by_name, key=lambda t: t[1])
print(by_status)
# [('cart', 'FAIL'), ('payment', 'FAIL'), ('login', 'PASS'), ('search', 'PASS')]

# Program 3: reverse=True keeps the order of equal items
print(sorted(["bb", "a", "cc", "d"], key=len, reverse=True))    # ['bb', 'cc', 'a', 'd']

# Program 4: sorting and then calling reverse() breaks that order
data = sorted(["bb", "a", "cc", "d"], key=len)
data.reverse()
print(data)                             # ['cc', 'bb', 'd', 'a']


# =====================================================
# Concept 10: Mixed Types and None
# =====================================================
"""
Definition:
Items must be comparable with each other. A number and a string
cannot be sorted together, and None cannot be compared with numbers.
Fix it with a key function that makes the items comparable.
"""

# Program 1: Numbers and text together fail
try:
    sorted([3, "a", 1])
except TypeError as e:
    print("Error:", e)                  # '<' not supported between instances of 'str' and 'int'

# Program 2: Integers and floats can be sorted together
print(sorted([3, 2.5, 1]))              # [1, 2.5, 3]

# Program 3: key=str makes anything comparable as text
print(sorted([10, "9", 2], key=str))    # [10, 2, '9'] (text order of '10', '2', '9')

# Program 4: Put None values at the end
values = [3, None, 1, None, 2]
try:
    sorted(values)
except TypeError as e:
    print("Error:", e)                  # '<' not supported between instances of 'NoneType' and 'int'
print(sorted(values, key=lambda x: (x is None, x if x is not None else 0)))     # [1, 2, 3, None, None]


# =====================================================
# Concept 11: Natural Sort (file2 before file10)
# =====================================================
"""
Definition:
Normal text sorting puts "file10" before "file2". A natural sort
reads the numbers inside the text as real numbers. Build a key that
turns the number parts into int. re.split(r"(\d+)", text) cuts a
text into text and number parts.
"""

# Program 1: The problem
files = ["file10", "file2", "file1"]
print(sorted(files))                    # ['file1', 'file10', 'file2']

# Program 2: A simple fix when the format is fixed
print(sorted(files, key=lambda f: int(f[4:])))      # ['file1', 'file2', 'file10']

# Program 3: A general fix with a regular expression
images = ["img12.png", "img10.png", "img2.png", "img1.png"]
print(re.split(r"(\d+)", "img12.png"))  # ['img', '12', '.png']
natural = sorted(images, key=lambda t: [int(p) if p.isdigit() else p for p in re.split(r"(\d+)", t)])
print(natural)                          # ['img1.png', 'img2.png', 'img10.png', 'img12.png']
# (the list comprehension inside the key is explained in file 08)

# Program 4: Version numbers
versions = ["1.10.0", "1.2.0", "1.9.1"]
print(sorted(versions))                 # ['1.10.0', '1.2.0', '1.9.1'] (wrong)
print(sorted(versions, key=lambda v: tuple(map(int, v.split(".")))))    # ['1.2.0', '1.9.1', '1.10.0']


# =====================================================
# Concept 12: Sorting by Hand (a Recap of the Algorithms)
# =====================================================
"""
Definition:
Bubble sort and selection sort are good practice, and interviewers
ask them. In real code always use sort() or sorted(), which are
much faster and well tested.
Bubble sort: compare neighbours and swap them if they are in the wrong order.
Selection sort: find the smallest item of the rest and move it forward.
"""

nums = [64, 34, 25, 12, 22, 11, 90]

# Program 1: Bubble sort
data = nums[:]
n = len(data)
for i in range(n):
    for j in range(0, n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)                             # [11, 12, 22, 25, 34, 64, 90]

# Program 2: Selection sort
data2 = nums[:]
for i in range(len(data2)):
    min_index = i
    for j in range(i + 1, len(data2)):
        if data2[j] < data2[min_index]:
            min_index = j
    data2[i], data2[min_index] = data2[min_index], data2[i]
print(data2)                            # [11, 12, 22, 25, 34, 64, 90]

# Program 3: Both give the same result as the built-in tool
print(data == data2 == sorted(nums))    # True


# =====================================================
# Concept 13: Useful Sorting Patterns
# =====================================================
"""
Definition:
Things you do with sorting again and again: unique sorted values,
check if a list is sorted, median, rank, sort a dictionary by value.
"""

# Program 1: Unique values in sorted order
print(sorted(set([3, 1, 3, 2, 1])))     # [1, 2, 3]

# Program 2: Is a list already sorted?
for candidate in ([1, 2, 2, 5], [3, 1, 2]):
    is_sorted = True
    for i in range(len(candidate) - 1):
        if candidate[i] > candidate[i + 1]:
            is_sorted = False
            break
    print(candidate, is_sorted, candidate == sorted(candidate))     # True True / False False

# Program 3: The median
for data in ([7, 1, 5], [4, 1, 3, 2]):
    ordered = sorted(data)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        median = ordered[middle]
    else:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    print(data, "median:", median)      # 5 and 2.5

# Program 4: The ends of a sorted list are the min and the max
data = [8, 3, 9, 1]
print(sorted(data)[0] == min(data), sorted(data)[-1] == max(data))      # True True

# Program 5: Sort a dictionary by value (items() gives (key, value) pairs)
scores = {"Ali": 90, "Sara": 85, "Bilal": 95}
ranking = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
print(ranking)                          # [('Bilal', 95), ('Ali', 90), ('Sara', 85)]

# Program 6: Print a ranking with numbers
for rank, (name, score) in enumerate(ranking, start=1):
    print(f"{rank}. {name:<6}{score}")


# =====================================================
# Concept 14: reverse()
# =====================================================
"""
Definition:
my_list.reverse() turns the CURRENT order around in place and
returns None. It does not look at the values, so it is not a sort.
"""

# Program 1: Basic use
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)                             # [4, 3, 2, 1]

# Program 2: Returns None, same object
before = id(nums)
print(nums.reverse())                   # None
print(before == id(nums))               # True

# Program 3: Reversing twice gives the original
data = [1, 2, 3]
data.reverse()
data.reverse()
print(data)                             # [1, 2, 3]

# Program 4: It does not sort
mixed = [3, 1, 2]
mixed.reverse()
print(mixed)                            # [2, 1, 3]

# Program 5: An empty list and a one item list are fine
empty = []
empty.reverse()
print(empty)                            # []
single = ["x"]
single.reverse()
print(single)                           # ['x']


# =====================================================
# Concept 15: reversed()
# =====================================================
"""
Definition:
reversed(sequence) gives an ITERATOR that goes from the last item
to the first. It does not change the original and does not build a
list by itself: wrap it in list() when you need a list.
An iterator can be used only ONCE. reversed() works on lists,
tuples, strings and ranges, but not on sets.
"""

# Program 1: It is an iterator, not a list
nums = [1, 2, 3]
print(type(reversed(nums)).__name__)    # list_reverseiterator

# Program 2: Make a list from it
print(list(reversed(nums)))             # [3, 2, 1]
print(nums)                             # [1, 2, 3] (unchanged)

# Program 3: Loop backwards without changing the list
items = ["a", "b", "c"]
for item in reversed(items):
    print(item)                         # c, b, a

# Program 4: An iterator is used up after one pass
r = reversed([1, 2, 3])
print(list(r))                          # [3, 2, 1]
print(list(r))                          # []

# Program 5: Other sequences, and a set that cannot be reversed
print("".join(reversed("abc")))         # cba
print(list(reversed(range(3))))         # [2, 1, 0]
try:
    reversed({1, 2})
except TypeError as e:
    print("Error:", e)                  # 'set' object is not reversible

# Program 6: Walk backwards by index
for i in range(len(items) - 1, -1, -1):
    print(i, items[i])                  # 2 c, 1 b, 0 a


# =====================================================
# Concept 16: Reverse with a Slice [::-1]
# =====================================================
"""
Definition:
my_list[::-1] returns a NEW reversed list. The original is not
changed, and a second name for the original does not see any change.
"""

# Program 1: A reversed copy
nums = [1, 2, 3]
copy_reversed = nums[::-1]
print(copy_reversed, nums)              # [3, 2, 1] [1, 2, 3]

# Program 2: Slice vs reverse() with a second name
a = [1, 2, 3]
alias = a
backwards = a[::-1]
print(alias, backwards)                 # [1, 2, 3] [3, 2, 1]
a.reverse()
print(alias)                            # [3, 2, 1] (reverse() changed the shared list)

# Program 3: Palindrome check
print([1, 2, 3, 2, 1] == [1, 2, 3, 2, 1][::-1])        # True

# Program 4: Reverse the order of the words of a sentence
text = "I love Python"
print(" ".join(text.split()[::-1]))     # Python love I


# =====================================================
# Concept 17: Which Reversing or Sorting Tool Should I Use?
# =====================================================
"""
Definition:
Need the same list reversed, no copy        -> reverse()
Need a reversed COPY, original must stay    -> [::-1]  or list(reversed(x))
Only need to LOOP backwards                 -> reversed(x)
Need DESCENDING ORDER (big to small)        -> sort(reverse=True) or sorted(..., reverse=True)
reverse() and sort(reverse=True) only give the same result when the
list is already in ascending order.
"""

# Program 1: Different results on an unsorted list
data = [2, 3, 1]
a = data.copy()
a.reverse()
b = data.copy()
b.sort(reverse=True)
print(a)                                # [1, 3, 2]
print(b)                                # [3, 2, 1]

# Program 2: Equal results on an ascending list
data = [1, 2, 3]
a = data.copy()
a.reverse()
b = data.copy()
b.sort(reverse=True)
print(a == b)                           # True

# Program 3: Last in first out with a list
history = ["step 1", "step 2", "step 3"]
for step in reversed(history):
    print("Undo", step)


# =====================================================
# Concept 18: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often in this file:
1) nums = nums.sort()           -> nums becomes None
2) nums.sort().reverse()        -> None has no reverse()
3) sorting numbers written as text without key=int
4) key=len()  instead of key=len
5) sort() or reverse() on a string or a tuple
6) printing reversed(x) and expecting a list
7) using sort() when a second name must keep the old order
"""

# Program 1: The classic bug
nums = [3, 1, 2]
nums = nums.sort()
print(nums)                             # None

# Program 2: Chaining on None
try:
    [3, 1, 2].sort().reverse()
except AttributeError as e:
    print("Error:", e)                  # 'NoneType' object has no attribute 'reverse'
nums = [3, 1, 2]
nums.sort(reverse=True)                 # the correct way to get descending order
print(nums)                             # [3, 2, 1]

# Program 3: Numbers as text
print(sorted(["100", "20", "3"]))               # ['100', '20', '3'] (wrong for numbers)
print(sorted(["100", "20", "3"], key=int))      # ['3', '20', '100']

# Program 4: key with brackets
try:
    sorted(["a", "bb"], key=str.lower())
except TypeError as e:
    print("TypeError: key must be a function, not a call")

# Program 5: A string has no sort() or reverse()
for text in ("abc",):
    try:
        text.sort()
    except AttributeError as e:
        print("Error:", e)              # 'str' object has no attribute 'sort'
print("".join(sorted("cab")), "cab"[::-1])        # abc bac

# Program 6: Printing reversed() directly
r = reversed([1, 2, 3])
print("<list_reverseiterator" in repr(r))       # True (it prints as an object, not as a list)
print(list(r))                          # [3, 2, 1]

# Program 7: sort() changes a second name too
a = [3, 1, 2]
alias = a
a.sort()
print(alias)                            # [1, 2, 3]


# =====================================================
# Concept 19: Sorting and Reversing in SQA Automation
# =====================================================
"""
Definition:
Test code sorts results to see the slowest tests or the failures
first, compares lists without caring about order, and checks that a
page really sorts its table or product list the way the user chose.
Texts read from a page (Playwright's all_inner_texts()) are plain
lists, so sorted() works on them directly.
"""

# Program 1: The 3 slowest tests
results = [("login", 2.3), ("cart", 5.1), ("search", 1.4), ("payment", 8.7), ("logout", 0.9)]
slowest = sorted(results, key=lambda r: r[1], reverse=True)[:3]
for name, seconds in slowest:
    print(f"{name:<9}{seconds:>5.1f}s")     # payment 8.7s, cart 5.1s, login 2.3s

# Program 2: Show the most serious results first (stable inside each group)
priority = ["FAIL", "ERROR", "WARNING", "PASS"]
entries = [("test_a", "PASS"), ("test_b", "ERROR"), ("test_c", "FAIL"),
           ("test_d", "WARNING"), ("test_e", "FAIL")]
for name, status in sorted(entries, key=lambda e: priority.index(e[1])):
    print(f"{status:<8}{name}")         # FAIL test_c, FAIL test_e, ERROR test_b, WARNING test_d, PASS test_a

# Program 3: Compare two lists without caring about the order
expected = ["Home", "Products", "Contact"]
actual = ["Contact", "Home", "Products"]
print(expected == actual)               # False (order matters for ==)
print(sorted(expected) == sorted(actual))       # True (same items)
print(sorted(["a", "a", "b"]) == sorted(["a", "b", "b"]))       # False (duplicates matter too)

# Program 4: Test a page that sorts its products by price (ascending)
page_working = ["$9.99", "$45.00", "$199.00", "$1,234.50"]
page_broken = ["$9.99", "$199.00", "$45.00", "$1,234.50"]
for label, texts in (("working page", page_working), ("broken page", page_broken)):
    prices = []
    for text in texts:
        prices.append(float(text.replace("$", "").replace(",", "")))
    if prices == sorted(prices):
        print(label, "-> PASS: prices are in ascending order")
    else:
        print(label, "-> FAIL: expected", sorted(prices), "but got", prices)

# Program 5: Test an alphabetical list (the case must not matter)
names_on_page = ["alice", "Bob", "carol", "Dave"]
print(names_on_page == sorted(names_on_page, key=str.casefold))     # True
print(names_on_page == sorted(names_on_page))                       # False (a false failure)

# Program 6: Sort test case ids by module, then by number
ids = ["TC_LOGIN_010", "TC_LOGIN_002", "TC_CART_001", "TC_LOGIN_001"]
print(sorted(ids, key=lambda t: (t.split("_")[1], int(t.split("_")[2]))))
# ['TC_CART_001', 'TC_LOGIN_001', 'TC_LOGIN_002', 'TC_LOGIN_010']

# Program 7: Newest log line first (timestamps in this format sort correctly as text)
log_lines = ["2026-10-17 10:00:05 [ERROR] db", "2026-10-17 10:00:01 [PASS] login",
             "2026-10-17 10:00:15 [FAIL] cart"]
for line in sorted(log_lines, reverse=True):
    print(line)                         # 10:00:15, 10:00:05, 10:00:01

# Program 8: Run the tests in a fixed order, so a failure is easy to reproduce
tests = ["test_payment", "test_login", "test_cart"]
tests.sort()
print(tests)                            # ['test_cart', 'test_login', 'test_payment']

# Program 9: Clean up created data in reverse order of creation
created = ["user", "order", "payment"]
for item in reversed(created):
    print("Deleting", item)             # payment, order, user