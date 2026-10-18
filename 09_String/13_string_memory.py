"""
====================================================
09_Strings / 13_string_memory.py
====================================================
Topic: String Memory, References and Interning
====================================================
Important notes before you run this file:
1) The id() numbers are different on every computer and every run.
   Never depend on the exact numbers, only compare them.
2) Interning is an internal CPython optimization. Results marked
   "typical" can differ between Python versions, or when you run
   the same lines in the interactive shell instead of a .py file.
   This is exactly why we NEVER compare text with 'is'.
3) To build a string while the program runs (so Python cannot
   share it), we use "".join([...]).
"""

import sys

# =====================================================
# Concept 1: String Objects and References
# =====================================================
"""
Definition:
A string is an OBJECT stored in memory. A variable is only a label
(a reference) that points to that object. Several labels can point
to the same object.
"""

# Program 1: Two labels, one object
a = "Ali"
b = a                                   # b points to the SAME object
print(a is b)                           # True

# Program 2: Three labels on one object
x = "data"
y = x
z = y
print(x is y is z)                      # True

# Program 3: Reassignment moves only one label
first = "cat"
second = first
first = first + "s"                     # first now points to a NEW object
print(first, second)                    # cats cat
print(first is second)                  # False


# =====================================================
# Concept 2: id() - Identity of an Object
# =====================================================
"""
Definition:
id(obj) returns an integer that identifies the object while it
is alive. In CPython it is the memory address of the object.
Two labels with the same id point to the same object.
"""

# Program 1: id() returns an integer
name = "Ali"
print(type(id(name)))                   # <class 'int'>

# Program 2: The same label always gives the same id
print(id(name) == id(name))             # True

# Program 3: Look at the id as a hexadecimal address (number differs on each PC)
print(hex(id(name)))


# =====================================================
# Concept 3: == vs is
# =====================================================
"""
Definition:
==  asks: "do both objects have the same VALUE?"
is  asks: "are both labels pointing to the SAME OBJECT?"
Equal values do not guarantee the same object.
"""

# Program 1: Lists make the difference very clear
list_a = [1, 2]
list_b = [1, 2]
list_c = list_a
print(list_a == list_b)                 # True  (same values)
print(list_a is list_b)                 # False (two different objects)
print(list_a is list_c)                 # True  (same object)

# Program 2: Two equal strings built while the program runs
s1 = "".join(["he", "llo"])
s2 = "".join(["he", "llo"])
print(s1 == s2)                         # True
print(s1 is s2)                         # False (typical: two separate objects)

# Program 3: The one place where 'is' is the right tool: None
value = None
print(value is None)                    # True


# =====================================================
# Concept 4: String Interning
# =====================================================
"""
Definition:
Interning means keeping ONE shared copy of a string in a special
pool, so equal strings reuse the same object instead of creating
duplicates. CPython interns some strings automatically.
sys.intern(s) lets you intern a string yourself, and its result is
guaranteed: equal strings always give the same object.
"""

# Program 1: Two equal runtime strings become one object after intern()
s1 = "".join(["py", "thon"])
s2 = "".join(["py", "thon"])
print(s1 is s2)                         # False (typical)
i1 = sys.intern(s1)
i2 = sys.intern(s2)
print(i1 is i2)                         # True (guaranteed)

# Program 2: Interning returns the already interned shared copy
literal = "hello"                       # identifier-like literals are interned automatically
built = "".join(["he", "llo"])
print(built is literal)                 # False (typical)
print(sys.intern(built) is literal)     # True (typical: shares the literal's object)

# Program 3: Only strings can be interned
try:
    sys.intern(5)
except TypeError as e:
    print("Error:", e)


# =====================================================
# Concept 5: Why Some Strings Share One Object
# =====================================================
"""
Definition:
CPython reuses string objects in three common cases:
1) Equal string literals in the same file are merged by the compiler.
2) Literals that look like identifiers (letters, digits, underscore)
   are interned automatically.
3) Empty string and single characters are cached and reused.
All three are optimizations, not rules of the language.
"""

# Program 1: Equal literals written twice in one file
text1 = "hello world"
text2 = "hello world"
print(text1 is text2)                   # True in a .py file (typical); may be False in the shell

# Program 2: Identifier-like literals
name1 = "test_login"
name2 = "test_login"
print(name1 is name2)                   # True (typical)

# Program 3: Single characters and the empty string
c1 = chr(104)                           # 'h' created at runtime
c2 = chr(104)
e1 = "".join([])
e2 = "".join([])
print(c1 is c2)                         # True (typical)
print(e1 is e2)                         # True (typical)

# Program 4: Normal runtime strings are NOT shared
r1 = ",".join(["a", "b", "c"])
r2 = ",".join(["a", "b", "c"])
print(r1 == r2, r1 is r2)               # True False (typical)


# =====================================================
# Concept 6: Small Strings and Identifiers
# =====================================================
"""
Definition:
Only string literals that appear in the source code are interned
automatically. A string built at runtime is NOT interned, even if
it looks like an identifier. Short does not mean shared.
"""

# Program 1: A runtime string and a literal with the same text
built = "".join(["py", "thon"])
literal = "python"
print(built == literal)                 # True
print(built is literal)                 # False (typical)

# Program 2: After intern() they become the same object
print(sys.intern(built) is literal)     # True (typical)

# Program 3: Dictionary lookup uses == (and hash), not 'is'
settings = {"status": "ok"}
key = "".join(["sta", "tus"])           # a different object with equal value
print(key is "status" if False else settings[key])   # ok (lookup still works)


# =====================================================
# Concept 7: Why Not Use 'is' to Compare Strings
# =====================================================
"""
Definition:
Whether two equal strings are the same object depends on interning,
which is an internal detail that can change. So 'is' on text can
give True on your computer and False on another. Python 3.8+ even
prints a SyntaxWarning for code like  x is "abc".
Always use == for text. Use 'is' only for None, True and False.
"""

# Program 1: 'is' gives a WRONG answer for equal text
username = "".join(["ad", "min"])
expected = "admin"
print(username == expected)             # True  (correct)
print(username is expected)             # False (typical) -> misleading!

# Program 2: The correct login check
if username == expected:
    print("Welcome Admin")
else:
    print("Access Denied")

# Program 3: The right uses of 'is'
result = None
flag = True
if result is None:
    print("No result yet")
if flag is True:
    print("Flag is True")


# =====================================================
# Concept 8: Memory Size of Strings (sys.getsizeof)
# =====================================================
"""
Definition:
sys.getsizeof(obj) returns the size of the object itself in bytes.
It is SHALLOW: it does not include objects stored inside a container.
The exact numbers depend on the Python version, so compare them
instead of memorising them.
Python stores a string with 1, 2 or 4 bytes per character, depending
on the widest character inside it.
"""

# Program 1: A longer string needs more memory
print(sys.getsizeof("") < sys.getsizeof("a") < sys.getsizeof("a" * 100))   # True

# Program 2: Wider characters need more bytes per character
english = "a" * 100                     # 1 byte per character
urdu = "ا" * 100                        # 2 bytes per character
emoji = "😀" * 100                       # 4 bytes per character
print(sys.getsizeof(english), sys.getsizeof(urdu), sys.getsizeof(emoji))
print(sys.getsizeof(english) < sys.getsizeof(urdu) < sys.getsizeof(emoji))  # True

# Program 3: getsizeof is shallow, a list does not count its items' size
big_text = "a" * 1000
one_item_list = [big_text]
print(sys.getsizeof(one_item_list) < sys.getsizeof(big_text))   # True


# =====================================================
# Concept 9: Memory Optimization with Interning
# =====================================================
"""
Definition:
If a program holds thousands of equal strings (for example the same
status text in every log line), each one is a separate object and
wastes memory. Interning lets all of them share one object.
"""

# Program 1: A list that repeats ONE object
same = ["PASS"] * 1000
print(len(set(map(id, same))))          # 1 (one object, 1000 references)

# Program 2: A list of 1000 equal but separate objects
distinct = ["".join(["PA", "SS"]) for _ in range(1000)]
print(len(set(map(id, distinct))))      # 1000 (typical)

# Program 3: Intern them to remove the duplicates
interned = [sys.intern(s) for s in distinct]
print(len(set(map(id, interned))))      # 1
print("Approx. memory saved:", sys.getsizeof(distinct[0]) * 999, "bytes")


# =====================================================
# Concept 10: Reference Counting and del
# =====================================================
"""
Definition:
CPython counts how many labels point to each object (its reference
count). When the count reaches zero, the object is freed.
del removes a LABEL, not the object itself.
sys.getrefcount() always shows one extra, because passing the object
as an argument is also a reference, so compare differences only.
"""

# Program 1: A new label increases the count by one
obj = "".join(["ref", "count"])
before = sys.getrefcount(obj)
other = obj
after = sys.getrefcount(obj)
print(after - before)                   # 1

# Program 2: del removes the label, the object stays while another label exists
a = "".join(["da", "ta"])
b = a
del a
print(b)                                # data
try:
    print(a)
except NameError as e:
    print("Error:", e)                  # name 'a' is not defined

# Program 3: del brings the count back down
extra = obj
count_with_extra = sys.getrefcount(obj)
del extra
print(sys.getrefcount(obj) == count_with_extra - 1)     # True


# =====================================================
# Concept 11: String Memory in SQA Automation
# =====================================================
"""
Definition:
Test logs, API responses and web page texts create a huge number of
strings. Cleaning and splitting them always creates NEW objects, so
compare their VALUES with ==, and intern repeated values when you
process very large logs.
"""

# Program 1: Compare a parsed value by value, never by identity
PASS = "[PASS]"
log_line = "[PASS] Login test"
level = log_line.split()[0]             # a brand new string object
print(level == PASS)                    # True  (correct way)
print(level is PASS)                    # False (typical) -> unreliable

# Program 2: Process a big log and share the repeated level texts
statuses = ["[PASS]", "[FAIL]", "[ERROR]"]
lines = [f"{statuses[i % 3]} test {i}" for i in range(1000)]
levels = [line.split()[0] for line in lines]
print("Separate objects before:", len(set(map(id, levels))))    # 1000 (typical)
levels = [sys.intern(lv) for lv in levels]
print("Separate objects after: ", len(set(map(id, levels))))    # 3

# Program 3: Expected vs actual text, cleaned and compared with ==
expected_title = "Login Page"
actual_title = "  Login Page\xa0"        # raw text from a web page
cleaned = actual_title.strip()          # strip() also removes \xa0
print(cleaned == expected_title)        # True