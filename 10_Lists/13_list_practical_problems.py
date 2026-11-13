"""
====================================================
10_Lists / 13_list_practical_problems.py
====================================================
Topic: Practical Problems with Lists (interview style)
====================================================
Notes before you run this file:
1) Every concept is ONE problem. Read the problem and the idea first,
   try to write the code yourself, then compare it with the programs.
2) Most problems are shown the "by hand" way first (loops, so you see
   the logic) and then the short Python way (built-ins).
3) Every program creates its own data, so programs do not depend on
   each other.
4) Interview habit: say the idea in one sentence, then ask yourself
   about the edge cases: an empty list, one item, duplicates,
   negative numbers, items that are all equal.
5) A variable called total, biggest or data is better than sum, max
   or list (never hide a built-in name).
6) Plain programs only, no functions.
"""

import bisect
import heapq
import itertools
import re


# =====================================================
# Problem 1: Sum, Average and Count
# =====================================================
"""
Problem:
Find the total, the average and the number of items that match a
condition. Be careful with an empty list (division by zero).
Idea:
Keep an accumulator (a running total or counter) outside the loop.
"""

# Program 1: Total and average with a loop
nums = [4, 8, 15, 16, 23, 42]
total = 0
for n in nums:
    total += n
print(total, total / len(nums))         # 108 18.0

# Program 2: Count the numbers bigger than 10
count = 0
for n in nums:
    if n > 10:
        count += 1
print(count)                            # 4

# Program 3: An empty list needs a check
data = []
print(sum(data) / len(data) if data else "no data")     # no data

# Program 4: Average with two decimals
marks = [70, 85, 90]
print(f"{sum(marks) / len(marks):.2f}")                 # 81.67


# =====================================================
# Problem 2: Largest and Smallest Without max() and min()
# =====================================================
"""
Problem:
Find the biggest and the smallest item, and their positions, with a loop.
Idea:
Start with the FIRST item (not with 0), compare every item with the
best one so far, and replace it when a better one comes.
"""

# Program 1: Biggest and smallest
nums = [7, 2, 9, 4, 9, 1]
biggest = nums[0]
smallest = nums[0]
for n in nums:
    if n > biggest:
        biggest = n
    if n < smallest:
        smallest = n
print(biggest, smallest)                # 9 1

# Program 2: The position of the biggest item (the first one wins a tie)
best_index = 0
for i, n in enumerate(nums):
    if n > nums[best_index]:
        best_index = i
print(best_index, nums[best_index])     # 2 9

# Program 3: ALL positions of the biggest item
print([i for i, n in enumerate(nums) if n == max(nums)])        # [2, 4]

# Program 4: Why you must not start with 0
data = [-5, -2, -9]
wrong = 0
for n in data:
    if n > wrong:
        wrong = n
print(wrong)                            # 0 (wrong, there is no 0 in the list)
right = data[0]
for n in data:
    if n > right:
        right = n
print(right)                            # -2 (correct)


# =====================================================
# Problem 3: Second Largest and the Nth Largest
# =====================================================
"""
Problem:
Find the second biggest DIFFERENT value. [89, 89, 45] has the
second largest 45, not 89. If all items are equal there is none.
Idea:
Short way: sorted(set(data))[-2].
One pass: keep the two best values and update them.
"""

# Program 1: With sorted() and set()
data = [12, 45, 2, 89, 34, 89]
print(sorted(set(data))[-2])            # 45

# Program 2: One pass
largest = None
second = None
for n in data:
    if largest is None or n > largest:
        second = largest
        largest = n
    elif n != largest and (second is None or n > second):
        second = n
print(largest, second)                  # 89 45

# Program 3: All items equal, there is no second largest
same = [5, 5, 5]
unique = sorted(set(same))
if len(unique) < 2:
    print("no second largest value")
else:
    print(unique[-2])

# Program 4: The 3 biggest different values
print(heapq.nlargest(3, set(data)))     # [89, 45, 34]
print(sorted(set(data), reverse=True)[:3])      # [89, 45, 34]

# Program 5: Negative numbers
print(sorted(set([-1, -5, -3]))[-2])    # -3


# =====================================================
# Problem 4: Reverse a List
# =====================================================
"""
Problem:
Reverse the order of the items.
Idea:
[::-1] makes a new reversed list, reverse() does it in place, and
two pointers swap items from both ends towards the middle.
"""

# Program 1: A new list with a slice
nums = [1, 2, 3, 4, 5]
print(nums[::-1], nums)                 # [5, 4, 3, 2, 1] [1, 2, 3, 4, 5]

# Program 2: In place with reverse()
data = nums.copy()
data.reverse()
print(data)                             # [5, 4, 3, 2, 1]

# Program 3: Two pointers (in place, without reverse())
data = nums.copy()
left, right = 0, len(data) - 1
while left < right:
    data[left], data[right] = data[right], data[left]
    left += 1
    right -= 1
print(data)                             # [5, 4, 3, 2, 1]

# Program 4: Build a new list from the end
result = []
for i in range(len(nums) - 1, -1, -1):
    result.append(nums[i])
print(result)                           # [5, 4, 3, 2, 1]

# Program 5: Reverse the order of the words of a sentence
sentence = "I love Python"
print(" ".join(sentence.split()[::-1])) # Python love I


# =====================================================
# Problem 5: Palindrome
# =====================================================
"""
Problem:
Is the list (or the text) the same when read backwards?
Idea:
Compare it with its reverse, or compare the two ends with two
pointers and stop at the first difference. For text, clean it first.
"""

# Program 1: With a slice
for data in ([1, 2, 3, 2, 1], [1, 2, 3]):
    print(data, data == data[::-1])     # True / False

# Program 2: Two pointers
data = [1, 2, 2, 1]
left, right = 0, len(data) - 1
is_palindrome = True
while left < right:
    if data[left] != data[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1
print(is_palindrome)                    # True

# Program 3: A sentence, ignoring case, spaces and punctuation
text = "A man, a plan, a canal: Panama"
cleaned = [c.lower() for c in text if c.isalnum()]
print(cleaned == cleaned[::-1])         # True


# =====================================================
# Problem 6: Count and Separate Items
# =====================================================
"""
Problem:
Count the even, odd, positive, negative items and zeros, and split
the list into separate lists. Note: 0 is even, and -1 % 2 is 1 in
Python, so negative odd numbers are found correctly.
Idea:
One loop with if / elif / else and one counter (or list) per group.
"""

nums = [3, -1, 0, 8, -4, 0, 7, 2]

# Program 1: Counters
even = odd = positive = negative = zero = 0
for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    if n > 0:
        positive += 1
    elif n < 0:
        negative += 1
    else:
        zero += 1
print(even, odd)                        # 5 3
print(positive, negative, zero)         # 4 2 2

# Program 2: Separate lists
positives, negatives, zeros = [], [], []
for n in nums:
    if n > 0:
        positives.append(n)
    elif n < 0:
        negatives.append(n)
    else:
        zeros.append(n)
print(positives, negatives, zeros)      # [3, 8, 7, 2] [-1, -4] [0, 0]

# Program 3: The sum of the even numbers only
print(sum(n for n in nums if n % 2 == 0))       # 6

# Program 4: Items at even and odd POSITIONS (not values)
print(nums[::2], nums[1::2])            # [3, 0, -4, 7] [-1, 8, 0, 2]


# =====================================================
# Problem 7: Duplicates
# =====================================================
"""
Problem:
Remove the duplicates (keep the order), find the duplicated values,
find the values that appear only once, and check if there is any
duplicate at all.
Idea:
Remember what you have seen. A set or dict is faster than a list for
that. dict.fromkeys() keeps the first-seen order.
"""

data = ["ali", "sara", "ali", "bilal", "sara", "ali"]

# Program 1: Remove duplicates, keep the order
unique = []
for name in data:
    if name not in unique:
        unique.append(name)
print(unique)                           # ['ali', 'sara', 'bilal']

# Program 2: The short way
print(list(dict.fromkeys(data)))        # ['ali', 'sara', 'bilal']

# Program 3: Which values are duplicated (each one reported once)?
seen = []
duplicates = []
for name in data:
    if name in seen:
        if name not in duplicates:
            duplicates.append(name)
    else:
        seen.append(name)
print(duplicates)                       # ['ali', 'sara']

# Program 4: Values that appear exactly once
print([x for x in data if data.count(x) == 1])  # ['bilal']

# Program 5: Is there any duplicate?
print(len(data) != len(set(data)))      # True
print(len([1, 2, 3]) != len(set([1, 2, 3])))    # False

# Program 6: Faster membership tests with a set
seen_set = set()
duplicates = []
for name in data:
    if name in seen_set:
        duplicates.append(name)
    else:
        seen_set.add(name)
print(duplicates)                       # ['ali', 'sara', 'ali'] (every repeated occurrence)


# =====================================================
# Problem 8: Frequency Count
# =====================================================
"""
Problem:
Count how many times every item appears, find the most and the
least frequent, and the first character that never repeats.
Idea:
A dictionary item -> count. dict.get(key, 0) avoids a KeyError.
"""

# Program 1: A frequency dictionary
words = ["a", "b", "a", "c", "b", "a"]
freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1
print(freq)                             # {'a': 3, 'b': 2, 'c': 1}

# Program 2: The same with get()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print(freq)                             # {'a': 3, 'b': 2, 'c': 1}

# Program 3: Most and least frequent (a tie goes to the first one)
print(max(freq, key=freq.get), min(freq, key=freq.get))         # a c

# Program 4: Sorted by count (big first), then by name
print(sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])))     # [('a', 3), ('b', 2), ('c', 1)]

# Program 5: Characters of a word
letters = {}
for ch in "banana":
    letters[ch] = letters.get(ch, 0) + 1
print(letters)                          # {'b': 1, 'a': 3, 'n': 2}

# Program 6: A small bar chart
for item, number in sorted(freq.items()):
    print(f"{item} {'#' * number}")     # a ###   b ##   c #

# Program 7: The first character that never repeats
text = "swiss"
for ch in text:
    if text.count(ch) == 1:
        print(ch)                       # w
        break
else:
    print("every character repeats")


# =====================================================
# Problem 9: Merge Lists
# =====================================================
"""
Problem:
Join two lists, merge two SORTED lists into one sorted list, mix the
items of two lists one by one, and join without duplicates.
Idea:
For two sorted lists use two pointers: always take the smaller of the
two current items.
"""

# Program 1: Simple joins
a = [1, 3, 5]
b = [2, 4]
print(a + b, [*a, *b])                  # [1, 3, 5, 2, 4] [1, 3, 5, 2, 4]

# Program 2: Merge two sorted lists by hand
a = [1, 3, 5, 7]
b = [2, 4, 6]
i = j = 0
merged = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1
merged += a[i:]
merged += b[j:]
print(merged)                           # [1, 2, 3, 4, 5, 6, 7]

# Program 3: The short ways
print(sorted(a + b))                    # [1, 2, 3, 4, 5, 6, 7]
print(list(heapq.merge(a, b)))          # [1, 2, 3, 4, 5, 6, 7]

# Program 4: Mix the items one by one
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
print([x for pair in zip(numbers, letters) for x in pair])      # [1, 'a', 2, 'b', 3, 'c']

# Program 5: Join without duplicates, keep the order
print(list(dict.fromkeys([1, 2, 3] + [3, 4, 2])))               # [1, 2, 3, 4]


# =====================================================
# Problem 10: Missing Number
# =====================================================
"""
Problem:
A list should contain the numbers 1 to n, but one (or more) is
missing. Find it.
Idea:
The sum of 1..n is n * (n + 1) // 2, so the difference to the real
sum is the missing number. A set difference also works for several.
"""

# Program 1: The sum formula
data = [1, 2, 4, 5, 6]
n = 6
print(n * (n + 1) // 2 - sum(data))     # 3

# Program 2: A set difference (works for several missing numbers)
print(set(range(1, n + 1)) - set(data)) # {3}
data2 = [1, 2, 4, 7]
print(sorted(set(range(1, 9)) - set(data2)))    # [3, 5, 6, 8]

# Program 3: A loop
for x in range(1, n + 1):
    if x not in data:
        print("missing:", x)            # 3

# Program 4: The gaps in a sorted list
missing = []
for a, b in zip(data2, data2[1:]):
    if b - a > 1:
        missing.extend(range(a + 1, b))
print(missing)                          # [3, 5, 6]

# Program 5: The XOR trick (equal numbers cancel each other)
result = 0
for x in range(1, n + 1):
    result ^= x
for x in data:
    result ^= x
print(result)                           # 3


# =====================================================
# Problem 11: Common Items, Union and Difference
# =====================================================
"""
Problem:
Which items are in both lists, in either list, only in the first one?
Idea:
Sets do this in one step but lose the order and the duplicates.
A comprehension keeps the order of the first list.
"""

a = [1, 2, 3, 4, 4]
b = [3, 4, 5]

# Program 1: Common items, order of the first list, no duplicates
print([x for x in dict.fromkeys(a) if x in b])  # [3, 4]

# Program 2: The set operations
print(sorted(set(a) & set(b)))          # [3, 4]        in both
print(sorted(set(a) | set(b)))          # [1, 2, 3, 4, 5]   in either
print(sorted(set(a) - set(b)))          # [1, 2]        only in a
print(sorted(set(a) ^ set(b)))          # [1, 2, 5]     in only one of them

# Program 3: A loop
common = []
for x in a:
    if x in b and x not in common:
        common.append(x)
print(common)                           # [3, 4]

# Program 4: Items of a that are not in b (duplicates kept)
print([x for x in a if x not in b])     # [1, 2]

# Program 5: A set makes the lookups fast
b_set = set(b)
print([x for x in a if x in b_set])     # [3, 4, 4]


# =====================================================
# Problem 12: Rotate a List
# =====================================================
"""
Problem:
Move the items k places to the left or to the right. Items that fall
off one end come back at the other end.
Idea:
Left:  nums[k:] + nums[:k]      Right: nums[-k:] + nums[:-k]
Use k % len(nums) first, so k can be bigger than the list.
"""

nums = [1, 2, 3, 4, 5]

# Program 1: Rotate left by 2
k = 2
print(nums[k:] + nums[:k])              # [3, 4, 5, 1, 2]

# Program 2: Rotate right by 2
print(nums[-k:] + nums[:-k])            # [4, 5, 1, 2, 3]

# Program 3: Any k
for k in (0, 2, 5, 7):
    shift = k % len(nums)
    print(k, nums[-shift:] + nums[:-shift])     # 0 and 5 give the same list, 7 acts like 2

# Program 4: In place with slice assignment
data = nums.copy()
data[:] = data[2:] + data[:2]
print(data)                             # [3, 4, 5, 1, 2]

# Program 5: One step at a time with pop() and insert()
data = nums.copy()
for _ in range(2):
    data.insert(0, data.pop())          # right
print(data)                             # [4, 5, 1, 2, 3]
data = nums.copy()
for _ in range(2):
    data.append(data.pop(0))            # left
print(data)                             # [3, 4, 5, 1, 2]

# Program 6: An empty list must not be divided by its length
data = []
k = 3
if data:
    k = k % len(data)
print(data, k)                          # [] 3 (no division happened)


# =====================================================
# Problem 13: Move All Zeros to the End
# =====================================================
"""
Problem:
Move every 0 to the end and keep the order of the other items.
Idea:
Two pointers: "read" looks at every item, "write" marks where the
next non-zero item goes.
"""

# Program 1: A new list
nums = [0, 1, 0, 3, 12]
non_zero = [x for x in nums if x != 0]
print(non_zero + [0] * (len(nums) - len(non_zero)))     # [1, 3, 12, 0, 0]

# Program 2: In place, copy then fill with zeros
data = nums.copy()
write = 0
for read in range(len(data)):
    if data[read] != 0:
        data[write] = data[read]
        write += 1
for i in range(write, len(data)):
    data[i] = 0
print(data)                             # [1, 3, 12, 0, 0]

# Program 3: In place with swaps (one pass)
data = nums.copy()
write = 0
for read in range(len(data)):
    if data[read] != 0:
        data[write], data[read] = data[read], data[write]
        write += 1
print(data)                             # [1, 3, 12, 0, 0]

# Program 4: A stable sort with a key (False comes before True)
data = nums.copy()
data.sort(key=lambda x: x == 0)
print(data)                             # [1, 3, 12, 0, 0]


# =====================================================
# Problem 14: Two Sum
# =====================================================
"""
Problem:
Find two items whose sum is the target, and tell their positions.
Idea:
Brute force checks all pairs (slow for big lists). One pass with a
dictionary value -> index asks: "did I already see target - n?".
For a SORTED list, two pointers also work.
"""

nums = [2, 7, 11, 15]
target = 9

# Program 1: Brute force
found = False
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)                 # 0 1
            found = True
            break
    if found:
        break

# Program 2: One pass with a dictionary
seen = {}
for i, n in enumerate(nums):
    need = target - n
    if need in seen:
        print(seen[need], i)            # 0 1
        break
    seen[n] = i

# Program 3: All pairs with the sum 7 (the values)
data = [1, 2, 3, 4, 5, 6]
print([(a, b) for i, a in enumerate(data) for b in data[i + 1:] if a + b == 7])
# [(1, 6), (2, 5), (3, 4)]

# Program 4: Two equal values
seen = {}
for i, n in enumerate([3, 3]):
    if 6 - n in seen:
        print(seen[6 - n], i)           # 0 1
        break
    seen[n] = i

# Program 5: Two pointers on a sorted list
data = [1, 3, 4, 6, 8]
target = 10
left, right = 0, len(data) - 1
while left < right:
    s = data[left] + data[right]
    if s == target:
        print(data[left], data[right])  # 4 6
        break
    elif s < target:
        left += 1
    else:
        right -= 1
else:
    print("no pair")

# Program 6: No pair exists
for i, a in enumerate([1, 2, 3]):
    if any(a + b == 100 for b in [1, 2, 3][i + 1:]):
        print("found")
        break
else:
    print("no pair with the sum 100")


# =====================================================
# Problem 15: Running Totals (Prefix Sums)
# =====================================================
"""
Problem:
Build the running total after every item, and use it to get the sum
of any part of the list quickly.
Idea:
prefix[i] is the sum of the first i items. The sum of nums[a:b] is
prefix[b] - prefix[a].
"""

nums = [1, 2, 3, 4]

# Program 1: A loop
running = []
current = 0
for n in nums:
    current += n
    running.append(current)
print(running)                          # [1, 3, 6, 10]

# Program 2: itertools.accumulate
print(list(itertools.accumulate(nums))) # [1, 3, 6, 10]

# Program 3: The sum of a part
prefix = [0] + running
print(prefix)                           # [0, 1, 3, 6, 10]
print(prefix[4] - prefix[1], sum(nums[1:4]))    # 9 9

# Program 4: A balance after every transaction
balance = 100
balances = []
for change in [-30, 50, -20]:
    balance += change
    balances.append(balance)
print(balances)                         # [70, 120, 100]


# =====================================================
# Problem 16: Maximum Subarray Sum (Kadane)
# =====================================================
"""
Problem:
Find the biggest sum of consecutive items (a "subarray").
Idea (Kadane's algorithm):
current = the best sum of a subarray that ENDS at this item.
At every item you either extend the old one, or start again here.
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Program 1: Kadane
best = current = nums[0]
for n in nums[1:]:
    current = max(n, current + n)
    best = max(best, current)
print(best)                             # 6

# Program 2: Also find which items make that sum
best = current = nums[0]
start = best_start = best_end = 0
for i in range(1, len(nums)):
    n = nums[i]
    if n > current + n:
        current = n
        start = i
    else:
        current += n
    if current > best:
        best = current
        best_start = start
        best_end = i
print(best, nums[best_start:best_end + 1])      # 6 [4, -1, 2, 1]

# Program 3: A slow check of all subarrays gives the same answer
print(max(sum(nums[i:j]) for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)))      # 6

# Program 4: All items negative, the answer is the least negative one
data = [-3, -1, -2]
best = current = data[0]
for n in data[1:]:
    current = max(n, current + n)
    best = max(best, current)
print(best)                             # -1


# =====================================================
# Problem 17: Searching (Linear and Binary)
# =====================================================
"""
Problem:
Find the position of a value.
Idea:
Linear search looks at every item (works on any list).
Binary search needs a SORTED list: look at the middle and throw away
half of the list at every step. The bisect module does it for you.
"""

# Program 1: Linear search with for-else
data = [5, 3, 8, 1]
for target in (8, 9):
    for i, x in enumerate(data):
        if x == target:
            print(target, "found at", i)        # 8 found at 2
            break
    else:
        print(target, "not found")              # 9 not found

# Program 2: Binary search by hand
data = [1, 3, 5, 7, 9, 11]
for target in (7, 4):
    low, high = 0, len(data) - 1
    steps = 0
    index = -1
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if data[mid] == target:
            index = mid
            break
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    print(target, "->", index, "in", steps, "steps")    # 7 -> 3 in 3 steps   4 -> -1 in 3 steps

# Program 3: bisect
print(bisect.bisect_left(data, 7))      # 3
position = bisect.bisect_left(data, 4)
print(position, position < len(data) and data[position] == 4)   # 2 False
updated = data.copy()
bisect.insort(updated, 6)
print(updated)                          # [1, 3, 5, 6, 7, 9, 11]

# Program 4: Binary search on an UNSORTED list gives a wrong answer
data = [5, 1, 4, 2, 3]
target = 5
low, high = 0, len(data) - 1
index = -1
while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
        index = mid
        break
    elif data[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(index, target in data)            # -1 True (the value IS in the list)


# =====================================================
# Problem 18: Sorting by Hand
# =====================================================
"""
Problem:
Sort a list without sort(). Interviewers ask this to test your logic.
In real code always use sort() or sorted().
Idea:
Bubble sort:    swap neighbours that are in the wrong order.
Selection sort: pick the smallest of the rest and move it forward.
Insertion sort: take the next item and slide it into its place in
                the already sorted part.
"""

nums = [64, 34, 25, 12, 22, 11, 90]

# Program 1: Bubble sort (it stops early when nothing moved)
data = nums.copy()
for p in range(len(data) - 1):
    swapped = False
    for j in range(len(data) - 1 - p):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True
    if not swapped:
        break
print(data)                             # [11, 12, 22, 25, 34, 64, 90]

# Program 2: Selection sort
data = nums.copy()
for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
        if data[j] < data[min_index]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]
print(data)                             # [11, 12, 22, 25, 34, 64, 90]

# Program 3: Insertion sort
data = nums.copy()
for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and data[j] > key:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
print(data == sorted(nums))             # True

# Program 4: The number of swaps in bubble sort equals the number of inversions
data = nums.copy()
swaps = 0
for p in range(len(data) - 1):
    for j in range(len(data) - 1 - p):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swaps += 1
print(swaps)                            # 14

# Program 5: Watch the passes of a bubble sort
data = [4, 3, 2, 1]
for p in range(len(data) - 1):
    swapped = False
    for j in range(len(data) - 1 - p):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True
    print("pass", p + 1, data)          # [3, 2, 1, 4]  [2, 1, 3, 4]  [1, 2, 3, 4]
    if not swapped:
        break

# Program 6: An already sorted list stops after ONE pass
data = [1, 2, 3, 4]
for p in range(len(data) - 1):
    swapped = False
    for j in range(len(data) - 1 - p):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
            swapped = True
    print("pass", p + 1, data)          # pass 1 [1, 2, 3, 4]
    if not swapped:
        break

# Program 7: Descending order, only the comparison changes
data = nums.copy()
for p in range(len(data) - 1):
    for j in range(len(data) - 1 - p):
        if data[j] < data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)                             # [90, 64, 34, 25, 22, 12, 11]


# =====================================================
# Problem 19: Is the List Sorted? (and Inversions)
# =====================================================
"""
Problem:
Check if a list is sorted, find the first place where the order
breaks, and count the "inversions" (pairs in the wrong order).
Idea:
Compare every item with its neighbour. zip(data, data[1:]) gives the
neighbour pairs.
"""

# Program 1: Ascending and strictly ascending
for data in ([1, 2, 2, 5], [3, 1]):
    print(data, all(a <= b for a, b in zip(data, data[1:])))    # True / False
data = [1, 2, 2, 5]
print(all(a < b for a, b in zip(data, data[1:])))               # False (2 and 2 are equal)

# Program 2: Descending
data = [9, 5, 5, 1]
print(all(a >= b for a, b in zip(data, data[1:])))              # True

# Program 3: The first place where the order breaks
data = [1, 3, 2, 4]
for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        print("breaks at positions", i, "and", i + 1)           # 1 and 2
        break

# Program 4: Compare with a sorted copy
print(data == sorted(data))             # False

# Program 5: Count the inversions
data = [2, 4, 1, 3, 5]
inversions = 0
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > data[j]:
            inversions += 1
print(inversions)                       # 3


# =====================================================
# Problem 20: Chunks, Windows and Grouping
# =====================================================
"""
Problem:
Split a list into pieces of a given size, take a page of a list, look
at every window of 3 items, and group items by a rule.
Idea:
Slices with a step through the start positions. For grouping use a
dictionary of lists with setdefault().
"""

data = list(range(1, 11))

# Program 1: Chunks of 3 (the last one is shorter)
print([data[i:i + 3] for i in range(0, len(data), 3)])  # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]

# Program 2: Two halves
mid = len(data) // 2
print(data[:mid], data[mid:])           # [1, 2, 3, 4, 5] [6, 7, 8, 9, 10]

# Program 3: One page
page, size = 2, 4
start = (page - 1) * size
print(data[start:start + size])         # [5, 6, 7, 8]
print((len(data) + size - 1) // size)   # 3 pages

# Program 4: Windows of 3 and their averages
windows = [data[i:i + 3] for i in range(len(data) - 2)]
print(len(windows), windows[0], windows[-1])    # 8 [1, 2, 3] [8, 9, 10]
print([sum(w) / 3 for w in windows])    # [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

# Program 5: Group into even and odd
groups = {"even": [], "odd": []}
for n in data:
    groups["even" if n % 2 == 0 else "odd"].append(n)
print(groups)                           # {'even': [2, 4, 6, 8, 10], 'odd': [1, 3, 5, 7, 9]}

# Program 6: Group words by length
words = ["to", "be", "or", "not", "ok", "yes"]
by_length = {}
for w in words:
    by_length.setdefault(len(w), []).append(w)
print(by_length)                        # {2: ['to', 'be', 'or', 'ok'], 3: ['not', 'yes']}

# Program 7: Group the anagrams (same letters, another order)
words = ["listen", "silent", "enlist", "google", "gogole", "cat", "act"]
anagrams = {}
for w in words:
    anagrams.setdefault("".join(sorted(w)), []).append(w)
print(list(anagrams.values()))
# [['listen', 'silent', 'enlist'], ['google', 'gogole'], ['cat', 'act']]


# =====================================================
# Problem 21: Number Lists (Fibonacci, Primes, Factorials, Digits)
# =====================================================
"""
Problem:
Build the classic number lists.
Idea:
Fibonacci: every number is the sum of the previous two.
Prime: only divisible by 1 and itself, so test the divisors up to its
square root. The Sieve of Eratosthenes crosses out the multiples.
"""

# Program 1: The first 10 Fibonacci numbers
fib = [0, 1]
while len(fib) < 10:
    fib.append(fib[-1] + fib[-2])
print(fib)                              # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Program 2: Prime numbers up to 30
primes = []
for n in range(2, 31):
    if all(n % d != 0 for d in range(2, int(n ** 0.5) + 1)):
        primes.append(n)
print(primes)                           # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Program 3: The Sieve of Eratosthenes
limit = 30
sieve = [True] * (limit + 1)
sieve[0] = sieve[1] = False
for i in range(2, int(limit ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * i, limit + 1, i):
            sieve[j] = False
print([i for i, is_prime in enumerate(sieve) if is_prime])      # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

# Program 4: Factorials
fact = [1]
for n in range(1, 6):
    fact.append(fact[-1] * n)
print(fact)                             # [1, 1, 2, 6, 24, 120]

# Program 5: A multiplication table
print([7 * i for i in range(1, 11)])    # [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# Program 6: The digits of a number
number = 4821
digits = [int(c) for c in str(number)]
print(digits, sum(digits))              # [4, 8, 2, 1] 15
print(int("".join(map(str, digits))))   # 4821 (back to the number)

# Program 7: The digits without str()
m = 4821
digits2 = []
while m:
    m, d = divmod(m, 10)
    digits2.append(d)
digits2.reverse()
print(digits2)                          # [4, 8, 2, 1]


# =====================================================
# Problem 22: Text Problems with Lists
# =====================================================
"""
Problem:
Words, vowels, frequencies, compressing and anagrams. A text becomes
a list with split() or list(), and goes back with join().
Idea:
Turn the text into a list, solve it as a list problem, join the result.
"""

text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# Program 1: Longest and shortest word (a tie goes to the first one)
print(len(words), max(words, key=len), min(words, key=len))     # 9 quick the

# Program 2: Unique words, sorted
print(sorted(set(words)), len(set(words)))      # ['brown', 'dog', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the'] 8

# Program 3: Words that appear more than once
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1
print([w for w, c in freq.items() if c > 1])    # ['the']

# Program 4: Capitalize every word
print(" ".join(w.capitalize() for w in words))  # The Quick Brown Fox Jumps Over The Lazy Dog

# Program 5: Reverse every word, and the order of the words
print(" ".join(w[::-1] for w in "I love Python".split()))   # I evol nohtyP
print(" ".join("I love Python".split()[::-1]))              # Python love I

# Program 6: Remove the vowels
print("".join(c for c in "automation" if c not in "aeiou"))     # tmtn

# Program 7: Count vowels and consonants
vowels = consonants = 0
for c in "Hello World":
    if c.isalpha():
        if c.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
print(vowels, consonants)               # 3 7

# Program 8: Run-length encoding
s = "aaabccdd"
result = []
i = 0
while i < len(s):
    j = i
    while j < len(s) and s[j] == s[i]:
        j += 1
    result.append(s[i] + str(j - i))
    i = j
print("".join(result))                  # a3b1c2d2

# Program 9: Anagram check (ignore case and spaces)
for first, second in (("Dormitory", "Dirty room"), ("hello", "world")):
    a = sorted(first.replace(" ", "").lower())
    b = sorted(second.replace(" ", "").lower())
    print(first, "|", second, "->", a == b)     # True / False


# =====================================================
# Problem 23: Stack Problems
# =====================================================
"""
Problem:
Use a list as a stack (append to push, pop to take the last item) for
balanced brackets, undo/redo and postfix calculation.
Idea:
The LAST item pushed is the FIRST one taken out (LIFO).
"""

# Program 1: Balanced brackets
pairs = {")": "(", "]": "[", "}": "{"}
for text in ["([]{})", "([)]", "((("]:
    stack = []
    ok = True
    for ch in text:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                ok = False
                break
    if ok and stack:
        ok = False
    print(text, ok)                     # True / False / False

# Program 2: Reverse a text with a stack
stack = list("hello")
reversed_text = ""
while stack:
    reversed_text += stack.pop()
print(reversed_text)                    # olleh

# Program 3: Undo and redo
history = ["type A", "type B", "type C"]
redo = []
redo.append(history.pop())
redo.append(history.pop())
print(history, redo)                    # ['type A'] ['type C', 'type B']
history.append(redo.pop())
print(history, redo)                    # ['type A', 'type B'] ['type C']

# Program 4: Postfix calculation (3 4 + 2 *) = (3 + 4) * 2
tokens = ["3", "4", "+", "2", "*"]
stack = []
for t in tokens:
    if t in ("+", "-", "*"):
        right = stack.pop()
        left = stack.pop()
        if t == "+":
            stack.append(left + right)
        elif t == "-":
            stack.append(left - right)
        else:
            stack.append(left * right)
    else:
        stack.append(int(t))
print(stack[0])                         # 14


# =====================================================
# Problem 24: Matrix Problems
# =====================================================
"""
Problem:
Transpose, rotate, add the diagonals, find the row with the biggest
sum and read the matrix in spiral order.
Idea:
zip(*m) gives the columns. Rotating clockwise = reverse the rows,
then transpose.
"""

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Program 1: Transpose
print([list(col) for col in zip(*m)])   # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

# Program 2: Rotate 90 degrees clockwise
print([list(col) for col in zip(*m[::-1])])    # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Program 3: The two diagonals
n = len(m)
print(sum(m[i][i] for i in range(n)), sum(m[i][n - 1 - i] for i in range(n)))   # 15 15

# Program 4: The row with the biggest sum
print(max(m, key=sum))                  # [7, 8, 9]

# Program 5: Spiral order
mat = [row[:] for row in m]
spiral = []
while mat:
    spiral += mat.pop(0)
    mat = [list(col) for col in zip(*mat)][::-1]
print(spiral)                           # [1, 2, 3, 6, 9, 8, 7, 4, 5]


# =====================================================
# Problem 25: Streaks and Runs
# =====================================================
"""
Problem:
Find the majority element, the longest streak of one value, the
longest increasing run, and remove consecutive duplicates.
Idea:
One pass with a "current run" counter that is reset when the pattern breaks.
"""

# Program 1: Majority element (more than half of the items), Boyer-Moore
data = [2, 2, 1, 1, 2, 2, 2]
candidate = None
count = 0
for n in data:
    if count == 0:
        candidate = n
    count += 1 if n == candidate else -1
print(candidate, data.count(candidate) > len(data) // 2)        # 2 True

# Program 2: The longest streak of PASS
statuses = ["PASS", "PASS", "FAIL", "PASS", "PASS", "PASS", "FAIL"]
best = current = 0
for s in statuses:
    if s == "PASS":
        current += 1
        best = max(best, current)
    else:
        current = 0
print(best)                             # 3

# Program 3: Remove consecutive duplicates
data = [1, 1, 2, 2, 2, 3, 1, 1]
result = [data[0]]
for x in data[1:]:
    if x != result[-1]:
        result.append(x)
print(result)                           # [1, 2, 3, 1]

# Program 4: The longest increasing run
data = [1, 2, 3, 1, 2, 3, 4, 0]
best = current = 1
for i in range(1, len(data)):
    if data[i] > data[i - 1]:
        current += 1
    else:
        current = 1
    best = max(best, current)
print(best)                             # 4


# =====================================================
# Problem 26: Common Mistakes in Problem Solving
# =====================================================
"""
Problem:
The mistakes that cost the most marks in tests and interviews.
Idea:
Always test your code on: an empty list, one item, all equal items,
negative numbers and a list that is already in the final state.
"""

# Program 1: An empty list
data = []
try:
    print(max(data))
except ValueError as e:
    print(type(e).__name__)             # ValueError
print(max(data, default=None))          # None

# Program 2: Starting the minimum with 0
data = [5, 3, 8]
smallest = 0
for n in data:
    if n < smallest:
        smallest = n
print(smallest)                         # 0 (wrong, it should be 3)
print(min(data))                        # 3

# Program 3: Storing the result of sort()
a = [3, 1, 2]
b = a.sort()
print(b, a)                             # None [1, 2, 3]
print(sorted([3, 1, 2]))                # [1, 2, 3]

# Program 4: Off by one
data = [1, 2, 3]
for i in range(len(data) - 1):
    print(data[i], end=" ")             # 1 2  (the last item is skipped)
print()
for i in range(len(data)):
    print(data[i], end=" ")             # 1 2 3
print()

# Program 5: Binary search needs a sorted list (see Problem 17)
data = [5, 1, 4, 2, 3]
print(data == sorted(data))             # False, so do not use binary search here

# Program 6: A list and a set give the same answer, a set is faster
seen_list = []
seen_set = set()
for x in [1, 2, 1, 3, 2]:
    if x not in seen_list:
        seen_list.append(x)
    seen_set.add(x)
print(seen_list, sorted(seen_set))      # [1, 2, 3] [1, 2, 3]

# Program 7: Changing a list while looping over it
data = [1, 2, 2, 3, 2, 4]
for x in data:
    if x == 2:
        data.remove(x)
print(data)                             # [1, 3, 2, 4] (a 2 is left)
data = [1, 2, 2, 3, 2, 4]
print([x for x in data if x != 2])      # [1, 3, 4]


# =====================================================
# Problem 27: Practical Problems in SQA Automation
# =====================================================
"""
Problem:
Real questions of a test team, solved with the lists you know:
flaky tests, missing ids, group failures by module, compare
expected and actual, balance work over parallel workers, check
pagination and sorting, check a cart total, analyse a log and compare
two runs.
Idea:
Every one of them is a list problem in disguise.
"""

# Program 1: A flaky test passes and fails in different runs
runs = {
    "login": ["PASS", "PASS", "PASS"],
    "cart": ["PASS", "FAIL", "PASS"],
    "search": ["FAIL", "FAIL", "FAIL"],
}
flaky = [name for name, st in runs.items() if len(set(st)) > 1]
always_fail = [name for name, st in runs.items() if set(st) == {"FAIL"}]
print("flaky:", flaky)                  # ['cart']
print("always failing:", always_fail)   # ['search']

# Program 2: Missing test ids in a numbered sequence
ids = ["TC_001", "TC_002", "TC_004", "TC_007"]
numbers = [int(i.split("_")[1]) for i in ids]
missing = [n for n in range(min(numbers), max(numbers) + 1) if n not in numbers]
print([f"TC_{n:03}" for n in missing])  # ['TC_003', 'TC_005', 'TC_006']

# Program 3: Duplicated test ids
ids = ["TC_001", "TC_002", "TC_001", "TC_003", "TC_002", "TC_001"]
seen = set()
dupes = []
for i in ids:
    if i in seen and i not in dupes:
        dupes.append(i)
    seen.add(i)
print(dupes)                            # ['TC_001', 'TC_002']

# Program 4: Group the failures by module
tests = ["LOGIN_01:PASS", "LOGIN_02:FAIL", "CART_01:FAIL", "CART_02:FAIL", "SEARCH_01:PASS"]
failures = {}
for item in tests:
    name, _, status = item.partition(":")
    if status == "FAIL":
        failures.setdefault(name.split("_")[0], []).append(name)
print(failures)                         # {'LOGIN': ['LOGIN_02'], 'CART': ['CART_01', 'CART_02']}
print({module: len(names) for module, names in failures.items()})       # {'LOGIN': 1, 'CART': 2}

# Program 5: Expected against actual, what exactly is wrong?
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Contact", "Products", "Blog"]
print("missing:", [x for x in expected if x not in actual])    # []
print("extra:", [x for x in actual if x not in expected])      # ['Blog']
in_expected_only = [x for x in actual if x in expected]
print("order correct:", in_expected_only == expected)          # False

# Program 6: Share the tests between 2 workers, the longest tests first
tests = [("a", 8), ("b", 7), ("c", 6), ("d", 5), ("e", 4)]
workers = 2
loads = [0] * workers
assignment = [[] for _ in range(workers)]
for name, seconds in sorted(tests, key=lambda t: t[1], reverse=True):
    w = loads.index(min(loads))         # the worker with the least work so far
    assignment[w].append(name)
    loads[w] += seconds
print(assignment, loads)                # [['a', 'd', 'e'], ['b', 'c']] [17, 13]

# Program 7: Pagination, no item may appear on two pages
page1 = list(range(1, 11))
page2 = list(range(10, 20))             # a bug: it starts with 10 again
page3 = list(range(20, 23))
all_items = page1 + page2 + page3
seen = set()
repeated = []
for x in all_items:
    if x in seen:
        repeated.append(x)
    seen.add(x)
print(len(all_items), len(seen), repeated)      # 23 22 [10]

# Program 8: Sorting on a page, where does the order break?
prices = [9.99, 199.0, 45.0, 1234.5]
for i, (a, b) in enumerate(zip(prices, prices[1:])):
    if a > b:
        print(f"FAIL: item {i + 1} ({a}) is followed by the smaller item {i + 2} ({b})")
        break

# Program 9: Does the displayed total match the items?
texts = ["$9.99", "$45.00", "$1,234.50"]
displayed_total = "$1,289.49"
values = [float(t.replace("$", "").replace(",", "")) for t in texts]
shown = float(displayed_total.replace("$", "").replace(",", ""))
print(round(sum(values), 2) == shown)   # True (floats are rounded before they are compared)

# Program 10: Analyse a log
log = [
    "2026-10-17 10:00:01 [PASS] login ok",
    "2026-10-17 10:00:05 [ERROR] database down",
    "2026-10-17 10:00:10 [WARNING] slow response 3.8s",
    "2026-10-17 10:00:15 [FAIL] cart button missing",
    "2026-10-17 10:00:20 [PASS] logout ok",
]
line_pattern = re.compile(r"(\S+) (\S+) \[(\w+)\] (.*)")
parsed = [line_pattern.fullmatch(line).groups() for line in log]
counts = {}
for date, time_text, level, message in parsed:
    counts[level] = counts.get(level, 0) + 1
print(counts)                           # {'PASS': 2, 'ERROR': 1, 'WARNING': 1, 'FAIL': 1}
print(next((p for p in parsed if p[2] == "ERROR"), None))   # ('2026-10-17', '10:00:05', 'ERROR', 'database down')
print([(p[1], p[3]) for p in parsed if p[2] in ("ERROR", "FAIL")])
# [('10:00:05', 'database down'), ('10:00:15', 'cart button missing')]
first_h, first_m, first_s = map(int, parsed[0][1].split(":"))
last_h, last_m, last_s = map(int, parsed[-1][1].split(":"))
print((last_h * 3600 + last_m * 60 + last_s) - (first_h * 3600 + first_m * 60 + first_s), "seconds")    # 19 seconds

# Program 11: Compare the failures of two runs
previous_failed = ["cart", "payment"]
current_failed = ["cart", "search"]
print("new failures:", [t for t in current_failed if t not in previous_failed])     # ['search']
print("fixed:", [t for t in previous_failed if t not in current_failed])            # ['payment']
print("still failing:", [t for t in current_failed if t in previous_failed])        # ['cart']

# Program 12: A test matrix without the combinations you do not support
browsers = ["chromium", "firefox", "webkit"]
widths = [320, 1280]
matrix = [(b, w) for b in browsers for w in widths if not (b == "webkit" and w == 320)]
print(len(matrix), matrix[-1])          # 5 ('webkit', 1280)

# Program 13: The three slowest tests
timings = [("login", 2.3), ("cart", 5.1), ("search", 1.4), ("payment", 8.7), ("logout", 0.9)]
for name, seconds in sorted(timings, key=lambda t: t[1], reverse=True)[:3]:
    print(f"{name:<8}{seconds:>5.1f}s")     # payment 8.7s, cart 5.1s, login 2.3s

# Program 14: Longest streak of failed tests in the order they ran
statuses = ["PASS", "FAIL", "FAIL", "PASS", "FAIL", "FAIL", "FAIL", "PASS"]
best = current = 0
for s in statuses:
    current = current + 1 if s == "FAIL" else 0
    best = max(best, current)
print(best)                             # 3

# Program 15: Are all expected items on the page, and is the number right?
page_items = ["Pen", "Notebook", "Bag"]
required = ["Pen", "Bag"]
print(all(item in page_items for item in required), len(page_items) == 3)       # True True