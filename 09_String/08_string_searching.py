"""
====================================================
09_Strings / 08_string_searching.py
====================================================
Topic: Searching Methods
====================================================
"""

# =====================================================
# Concept 1: find()
# =====================================================
"""
Definition:
find() looks for a substring and returns the index of its FIRST
occurrence. If the substring is not found, it returns -1 (no error).
Syntax: string.find(substring, start, end)  -> start and end are optional.
"""

# Program 1: Find the first position of a word
text = "Python is fun, Python is easy"
print(text.find("Python"))   # 0
print(text.find("fun"))      # 10

# Program 2: A missing substring returns -1
print(text.find("Java"))   # -1

# Program 3: Search again after the first match using the start argument
first = text.find("Python")
second = text.find("Python", first + 1)
print(first)
print(second)

text2 = "ab ab ab"
first_position = text2.find("ab")
print(first_position)   #0

second_position = text2.find("ab",first_position + 1)
print(second_position)  #3

third_position = text2.find("ab", second_position + 1)
print(third_position)   #6

fourth_position = text2.find("ab", third_position + 1)
print(fourth_position)   # -1

while first_position != -1:
    print(first_position)
    first_position = text2.find("ab", first_position + 1)


# =====================================================
# Concept 2: rfind()
# =====================================================
"""
Definition:
rfind() works like find(), but it searches from the RIGHT side,
so it returns the index of the LAST occurrence.
It also returns -1 when nothing is found.
"""

# Program 1: Find the last occurrence of a word
text = "Python is fun, Python is easy"
print(text.rfind("Python"))         # 15

# Program 2: Compare find() and rfind() on the same text
print(text.find("is"), text.rfind("is"))    # 7 22

# Program 3: A missing substring also returns -1
print(text.rfind("Java"))           # -1


# =====================================================
# Concept 3: index()
# =====================================================
"""
Definition:
index() works like find(), but when the substring is NOT found it
raises a ValueError instead of returning -1.
Use find() when "not found" is a normal case.
Use index() when "not found" means something is wrong.
"""

# Program 1: Find a word with index()
text = "Python is fun"
print(text.index("fun"))            # 10

# Program 2: Catch the error when the word is missing
try:
    print(text.index("Java"))
except ValueError as e:
    print("Error:", e)              # substring not found

# Program 3: Compare find() and index() side by side
print(text.find("Java"))            # -1 (no error)
try:
    text.index("Java")
except ValueError:
    print("index() raised ValueError, find() returned -1")



# =====================================================
# Concept 4: rindex()
# =====================================================
"""
Definition:
rindex() works like rfind() (searches from the right and returns the
LAST occurrence), but it raises a ValueError when nothing is found.
"""

# Program 1: Find the last occurrence
text = "Python is fun, Python is easy"
print(text.rindex("Python"))        # 15

# Program 2: Catch the error for a missing word
try:
    print(text.rindex("Java"))
except ValueError as e:
    print("Error:", e)

# Program 3: Get the file extension using the last dot
filename = "my.report.final.pdf"
last_dot = filename.rindex(".")
print(filename[last_dot + 1:])      # pdf

# =====================================================
# Concept 5: count()
# =====================================================
"""
Definition:
count() returns how many times a substring appears in the string.
The matches do not overlap. Syntax: string.count(sub, start, end)
"""
# Program 1: Count a word in a sentence
text = "Python is fun, Python is easy, Python is powerful"
print(text.count("Python"))         # 3

# Program 2: Count one character
word = "banana"
print(word.count("a"))              # 3

# Program 3: Matches do not overlap
print("aaaa".count("aa"))           # 2 (not 3)

# Program 4: Count vowels using a loop and count()
sentence = "Automation Testing"
total_vowels = 0
for vowel in "aeiou":
    total_vowels += sentence.lower().count(vowel)
print("Total vowels:", total_vowels)       # 7

# =====================================================
# Concept 6: startswith()
# =====================================================
"""
Definition:
startswith() returns True if the string begins with the given text,
otherwise False. A tuple of options can be given to check several
prefixes at once.
"""
# Program 1: Check a prefix
filename = "test_login.py"
print(filename.startswith("test_"))         # True
print(filename.startswith("main_"))         # False

# Program 2: Check several prefixes at once using a tuple
url = "https://example.com"
print(url.startswith(("http://", "https://")))      # True

# Program 3: Case-sensitive check, fixed using lower()
text = "Hello World"
print(text.startswith("hello"))             # False
print(text.lower().startswith("hello"))     # True

# =====================================================
# Concept 7: endswith()
# =====================================================
"""
Definition:
endswith() returns True if the string finishes with the given text,
otherwise False. A tuple of options can be given here too.
"""

# Program 1: Check a file extension
filename = "report.pdf"
print(filename.endswith(".pdf"))            # True
print(filename.endswith(".docx"))           # False

# Program 2: Check several extensions at once
print("photo.png".endswith((".jpg", ".png", ".gif")))   # True

# Program 3: Filter a list of files by extension
files = ["a.py", "b.txt", "c.py", "d.csv"]
for f in files:
    if f.endswith(".py"):
        print("Python file:", f)

# =====================================================
# Concept 8: Searching with start and end limits
# =====================================================
"""
Definition:
find(), index(), count(), startswith() and endswith() can all take
optional start and end positions, so the search happens only in
that part of the string.
"""

# Program 1: Search only inside a part of the string
text = "one two one two one"
print(text.find("one", 4))          # 8 (skips the first "one")

# Program 2: Count only inside a part of the string
print(text.count("one", 0, 7))      # 1

# Program 3: Check a prefix from a given position
print(text.startswith("two", 4))    # True


# =====================================================
# Concept 9: Finding ALL Positions of a Substring
# =====================================================
"""
Definition:
find() only gives one position. To get every position, call it in a
while loop and move the start forward after each match.
"""

# Program 1: Print every position of a letter
text = "banana"
pos = text.find("a")
while pos != -1:
    print("Found at index", pos)
    pos = text.find("a", pos + 1)

# Program 2: Collect every position in a list
text = "one two one two one"
positions = []
pos = text.find("one")
while pos != -1:
    positions.append(pos)
    pos = text.find("one", pos + 1)
print(positions)                    # [0, 8, 16]

# Program 3: Find positions using a for loop and slicing
text = "banana"
for i in range(len(text)):
    if text[i] == "a":
        print("Letter a at index", i)


# =====================================================
# Concept 10: find() vs in Operator
# =====================================================
"""
Definition:
'in' only answers True/False ("is it there?").
find() answers WHERE it is. Use 'in' for a simple check
and find() when you need the position.
"""

# Program 1: Simple existence check with 'in'
text = "Software Testing"
print("Test" in text)               # True

# Program 2: Get the position with find()
print(text.find("Test"))            # 9

# Program 3: Use find() safely, because index 0 is also a valid position
text = "Python"
if text.find("Py") != -1:           # correct check
    print("Found")
# if text.find("Py"):               # WRONG: find returns 0 here, which counts as False






