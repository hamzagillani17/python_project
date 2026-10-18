r"""
====================================================
09_Strings / 10_string_split_join.py
====================================================
Topic: Splitting and Joining Strings
====================================================
Reminder: split() BREAKS a string into a list of pieces.
join() GLUES a list of pieces back into one string.
They are opposites of each other.
"""

# =====================================================
# Concept 1: split() with No Argument
# =====================================================
"""
Definition:
split() with no argument breaks the string on any run of whitespace
(spaces, tabs, new lines) and ignores empty parts.
It ALWAYS returns a list of strings.
"""

# Program 1: Split a sentence into words
sentence = "I love Python programming"
words = sentence.split()
print(words)                    # ['I', 'love', 'Python', 'programming']


# Program 2: Extra spaces are ignored
text = "  too    many   spaces  "
print(text.split())             # ['too', 'many', 'spaces']

# Program 3: Count the words in a sentence
sentence = "Software testing is a great career"
print("Word count:", len(sentence.split()))     # 6

# Program 4: The result is always a list
print(type("a b c".split()))    # <class 'list'>



# =====================================================
# Concept 2: split(separator)
# =====================================================
"""
Definition:
split(sep) breaks the string wherever the exact separator text
appears. The separator itself is removed from the result.
Unlike split() with no argument, empty parts are KEPT.
"""

# Program 1: Split a CSV line on commas
csv_line = "Ali,22,Lahore"
print(csv_line.split(","))      # ['Ali', '22', 'Lahore']

# Program 2: Empty parts are kept when the separator repeats
print("a,b,,c".split(","))      # ['a', 'b', '', 'c']

# Program 3: A separator can be longer than one character
print("one--two--three".split("--"))    # ['one', 'two', 'three']

# Program 4: Splitting an empty string gives different results
print("".split())               # []
print("".split(","))            # ['']

# =====================================================
# Concept 3: split(" ") vs split()
# =====================================================
"""
Definition:
split(" ") treats EVERY single space as a separator, so repeated
spaces create empty strings. split() with no argument treats a whole
run of whitespace as one separator and removes the empty parts.
"""

# Program 1: Compare both on the same text
text = "  a  b "
print(text.split(" "))          # ['', '', 'a', '', 'b', '']
print(text.split())             # ['a', 'b']

# Program 2: Tabs and new lines are split only by split()
text = "A\tB\nC D"
print(text.split(" "))          # ['A\tB\nC', 'D']
print(text.split())             # ['A', 'B', 'C', 'D']

# Program 3: Count words correctly
text = "hello   world"
print(len(text.split(" ")))     # 4 (wrong idea of word count)
print(len(text.split()))        # 2 (correct)


# =====================================================
# Concept 4: split() with maxsplit
# =====================================================
"""
Definition:
split(sep, maxsplit) stops after 'maxsplit' cuts, counting from the
LEFT. The rest of the string stays together in the last piece.
"""

# Program 1: Only one cut
print("a-b-c-d".split("-", 1))  # ['a', 'b-c-d']

# Program 2: Two cuts
print("a-b-c-d".split("-", 2))  # ['a', 'b', 'c-d']

# Program 3: Split a log line into date, time, level and message
log = "2026-10-17 10:30:15 [ERROR] Login failed for user ali"
parts = log.split(" ", 3)
print(parts)    # ['2026-10-17', '10:30:15', '[ERROR]', 'Login failed for user ali']


# =====================================================
# Concept 5: rsplit()
# =====================================================
"""
Definition:
rsplit() works like split(), but when maxsplit is given it cuts from
the RIGHT side. Without maxsplit, split() and rsplit() give the
same result.
"""

# Program 1: Compare split() and rsplit() with maxsplit
text = "a-b-c-d"
print(text.split("-", 1))       # ['a', 'b-c-d']
print(text.rsplit("-", 1))      # ['a-b-c', 'd']

# Program 2: Separate a file name from its extension
filename = "my.document.final.txt"
name, extension = filename.rsplit(".", 1)
print(name)                     # my.document.final
print(extension)                # txt

# Program 3: Without maxsplit both are the same
print("x y z".split() == "x y z".rsplit())      # True


# =====================================================
# Concept 6: splitlines()
# =====================================================
r"""
Definition:
splitlines() breaks a string at line boundaries (\n, \r\n and others)
and returns a list of lines. By default the line ending is removed.
keepends=True keeps the line endings.
"""

# Program 1: Split multi-line text
text = "Line1\nLine2\nLine3"
print(text.splitlines())        # ['Line1', 'Line2', 'Line3']

# Program 2: Keep the line endings
print(text.splitlines(keepends=True))   # ['Line1\n', 'Line2\n', 'Line3']

# Program 3: splitlines() handles a trailing new line better than split("\n")
text = "a\nb\n"
print(text.splitlines())        # ['a', 'b']
print(text.split("\n"))         # ['a', 'b', '']

# Program 4: Process a triple-quoted block line by line
report = """PASS Login
FAIL Checkout
PASS Logout"""
for line in report.splitlines():
    print("Line ->", line)


# =====================================================
# Concept 7: join()
# =====================================================
"""
Definition:
separator.join(list) glues all the strings of a list together, with
the separator between them. The separator is written BEFORE .join,
and the list goes inside the brackets. It returns a new string.
"""

# Program 1: Join words with a space
words = ["I", "love", "Python"]
print(" ".join(words))          # I love Python

# Program 2: Join with a comma (build a CSV line)
data = ["Ali", "22", "Lahore"]
print(",".join(data))           # Ali,22,Lahore

# Program 3: Join with an empty separator
print("".join(["a", "b", "c"])) # abc

# Program 4: Join a path using a slash
print("/".join(["home", "user", "docs"]))       # home/user/docs

# Program 5: A string is also a sequence of characters
print("-".join("abc"))          # a-b-c


# =====================================================
# Concept 8: join() Needs Strings Only
# =====================================================
"""
Definition:
join() works only when EVERY item is a string. If the list has numbers,
you must convert them to strings first with str().
"""

# Program 1: Show the error with numbers
numbers = [1, 2, 3]
try:
    print(",".join(numbers))
except TypeError as e:
    print("Error:", e)

# Program 2: Convert each number with a loop
text_numbers = []
for n in numbers:
    text_numbers.append(str(n))
print(",".join(text_numbers))   # 1,2,3

# Program 3: Convert with map()
print(",".join(map(str, numbers)))      # 1,2,3


# =====================================================
# Concept 9: split() and join() Together
# =====================================================
"""
Definition:
A very common pattern: split a string into a list, change the list,
and join it back into a string.
"""

# Program 1: Capitalize every word
text = "hello world python"
words = text.split()
result = []
for w in words:
    result.append(w.capitalize())
print(" ".join(result))         # Hello World Python

# Program 2: Reverse the order of the words
text = "I love Python"
print(" ".join(text.split()[::-1]))     # Python love I

# Program 3: Reverse each word but keep the word order
text = "I love Python"
reversed_words = []
for w in text.split():
    reversed_words.append(w[::-1])
print(" ".join(reversed_words))         # I evol nohtyP

# Program 4: Change the separator of a string
date = "2026-10-17"
print("/".join(date.split("-")))        # 2026/10/17


# =====================================================
# Concept 10: Unpacking the Result of split()
# =====================================================
"""
Definition:
When you know how many pieces split() returns, you can unpack them
into separate variables in one line. If the number of variables does
not match the number of pieces, Python raises a ValueError.
"""

# Program 1: Unpack a name
first, last = "Ali Khan".split()
print(first, last)              # Ali Khan

# Program 2: Unpack a CSV line
name, age, city = "Ali,22,Lahore".split(",")
print(f"{name} is {age} years old and lives in {city}")

# Program 3: A mismatch raises an error
try:
    first, last = "Ali Ahmed Khan".split()
except ValueError as e:
    print("Error:", e)          # too many values to unpack (expected 2)

# Program 4: Use * to collect the extra middle parts
first, *middle, last = "Ali Ahmed Raza Khan".split()
print(first, middle, last)      # Ali ['Ahmed', 'Raza'] Khan


# =====================================================
# Concept 11: partition() and rpartition()
# =====================================================
"""
Definition:
partition(sep) splits the string at the FIRST separator into exactly
three parts: (before, separator, after). rpartition(sep) does the
same at the LAST separator. If the separator is missing, partition()
returns (whole string, "", "").
"""

# Program 1: Split a key=value text
key, sep, value = "name=Ali".partition("=")
print(key, sep, value)          # name = Ali

# Program 2: First and last separator on the same text
text = "a=b=c"
print(text.partition("="))      # ('a', '=', 'b=c')
print(text.rpartition("="))     # ('a=b', '=', 'c')

# Program 3: A missing separator
print("hello".partition("="))   # ('hello', '', '')

# Program 4: Get the file name from a path
path = "C:/data/reports/final.xlsx"
folder, sep, filename = path.rpartition("/")
print(filename)                 # final.xlsx


# =====================================================
# Concept 12: Converting Split Values to Numbers
# =====================================================
"""
Definition:
split() always returns strings. To calculate with the values, convert
each piece with int() or float().
"""

# Program 1: Sum numbers typed in one line
line = "10,20,30"
total = 0
for item in line.split(","):
    total += int(item)
print("Total:", total)          # 60

# Program 2: Build a list of integers
numbers = []
for item in "5 3 9 1".split():
    numbers.append(int(item))
print(numbers, max(numbers))    # [5, 3, 9, 1] 9

# Program 3: Read several numbers from the user
user_line = input("Enter numbers separated by spaces: ")
values = []
for item in user_line.split():
    values.append(float(item))
print("Average:", sum(values) / len(values))


# =====================================================
# Concept 13: Real-World Parsing
# =====================================================
"""
Definition:
Splitting and joining are used all the time in automation work:
CSV rows, query strings, log lines, file paths and test case IDs.
"""

# Program 1: Parse several CSV rows
csv_data = """Ali,25,ali@test.com,Active
Sara,22,sara@test.com,Inactive
Bilal,30,bilal@test.com,Active"""
for row in csv_data.splitlines():
    name, age, email, status = row.split(",")
    print(f"{name:<8}{age:>4}  {email:<18}{status}")

# Program 2: Turn a query string into a dictionary
query = "name=Ali&age=22&city=Lahore"
params = {}
for pair in query.split("&"):
    key, sep, value = pair.partition("=")
    params[key] = value
print(params)                   # {'name': 'Ali', 'age': '22', 'city': 'Lahore'}

# Program 3: Break a test case ID into parts
test_id = "TC_LOGIN_001"
prefix, module, number = test_id.split("_")
print(f"Module: {module}, Test number: {int(number)}")

# Program 4: Count log levels from a multi-line log
log_text = """[PASS] Login
[FAIL] Checkout
[PASS] Logout
[ERROR] Database"""
counts = {}
for line in log_text.splitlines():
    level = line.split()[0]     # first word, e.g. [PASS]
    counts[level] = counts.get(level, 0) + 1
print(counts)                   # {'[PASS]': 2, '[FAIL]': 1, '[ERROR]': 1}


# =====================================================
# Concept 14: Why join() Beats += in a Loop
# =====================================================
"""
Definition:
Adding strings with += inside a loop creates a new string object at
every step. Collecting the pieces in a list and calling join() once
at the end is faster and cleaner, especially for big data.
"""

# Program 1: Slow style (works, but creates many temporary strings)
result = ""
for i in range(5):
    result += str(i) + ","
print(result)                   # 0,1,2,3,4,

# Program 2: Better style with a list and join()
pieces = []
for i in range(5):
    pieces.append(str(i))
print(",".join(pieces))         # 0,1,2,3,4 (no extra comma at the end)

# Program 3: Build a text report line by line
lines = []
for name, score in [("Ali", 95), ("Sara", 88), ("Bilal", 79)]:
    lines.append(f"{name}: {score}")
print("\n".join(lines))




































