r"""
====================================================
09_Strings / 12_string_immutability.py
====================================================
Topic: String Immutability
====================================================
Core idea: a string OBJECT can never change after it is created.
A variable is only a label (reference) pointing to an object.
"Changing" a string always means creating a NEW object and pointing
the variable to it. The old object is left untouched.
(id() numbers are different on every computer and every run,
so compare them with == and never rely on the exact numbers.)
"""

# =====================================================
# Concept 1: What is Immutable?
# =====================================================
"""
Definition:
Immutable means "cannot be changed after creation". The characters
inside a string object can never be modified. Only the variable
(the label) can be pointed to a different object.
"""

# Program 1: Create a string and look at it
name = "Ali"
print(name, type(name))                 # Ali <class 'str'>

# Program 2: The type is str, which is an immutable type
print(isinstance(name, str))            # True

# Program 3: Pointing the variable elsewhere does not change the old object
a = "Ali"
b = a                                   # b points to the same object
a = "Ahmed"                             # a now points to a NEW object
print(a, b)                             # Ahmed Ali (b is still safe)


# =====================================================
# Concept 2: Why a String Cannot Be Changed Directly
# =====================================================
"""
Definition:
The str type does not support item assignment (s[0] = "x"),
item deletion (del s[0]) or slice assignment (s[0:2] = "xx").
Python raises a TypeError for all three.
"""

# Program 1: Item assignment
text = "Hello"
try:
    text[0] = "J"
except TypeError as e:
    print("Error:", e)                  # 'str' object does not support item assignment

# Program 2: Item deletion
try:
    del text[0]
except TypeError as e:
    print("Error:", e)                  # 'str' object doesn't support item deletion

# Program 3: Slice assignment
try:
    text[0:2] = "xx"
except TypeError as e:
    print("Error:", e)


# =====================================================
# Concept 3: Why s[0] = "H" Gives an Error (Compare with a List)
# =====================================================
"""
Definition:
A list supports item assignment, so list[0] = "J" works.
A string and a tuple do not, so the same line raises a TypeError.
This is the exact difference between mutable and immutable types.
"""

# Program 1: A list can be changed in place
letters = ["H", "e", "l", "l", "o"]
letters[0] = "J"
print(letters)                          # ['J', 'e', 'l', 'l', 'o']

# Program 2: A tuple is immutable like a string
numbers = (1, 2, 3)
try:
    numbers[0] = 9
except TypeError as e:
    print("Error:", e)                  # 'tuple' object does not support item assignment

# Program 3: Print the error type and message separately
try:
    "Hello"[0] = "J"
except TypeError as e:
    print("Error type:", type(e).__name__)
    print("Message:", e)


# =====================================================
# Concept 4: How a New String is Created
# =====================================================
"""
Definition:
Every operation that seems to change a string (+, upper(), replace(),
slicing and so on) builds a brand-new string object.
Trick to PROVE it: keep a second reference ("old") to the original
object before the change, then compare both afterwards.
"""

# Program 1: Concatenation creates a new string
original = "Ali"
changed = original + " Khan"
print(original, "|", changed)           # Ali | Ali Khan

# Program 2: Prove it with id() and a second reference
name = "Ali"
old = name                              # second label on the same object
print(id(name) == id(old))              # True  (same object)
name = name + " Khan"                   # new object is created
print(id(name) == id(old))              # False (different object)
print(old)                              # Ali       (old object untouched)
print(name)                             # Ali Khan

# Program 3: A method also returns a new object
text = "hello"
upper_text = text.upper()
print(text, upper_text)                 # hello HELLO
print(id(text) == id(upper_text))       # False


# =====================================================
# Concept 5: String Reassignment
# =====================================================
"""
Definition:
Reassignment means making the variable point to a different object.
It is NOT a change of the string. Think of the variable as an arrow:
reassignment turns the arrow, the object itself never changes.
"""

# Program 1: The arrow moves to a new object
x = "Hello"
id_before = id(x)
x = "World"
print(id_before == id(x))               # False (x now points elsewhere)

# Program 2: Other variables keep pointing to the old object
a = "cat"
b = a
a = a + "s"
print(a, b)                             # cats cat

# Program 3: A loop that reassigns the variable at every step
word = "a"
for i in range(3):
    word = word + "a"
    print(word)                         # aa  aaa  aaaa


# =====================================================
# Concept 6: Mutable vs Immutable
# =====================================================
"""
Definition:
Mutable objects (list, dict, set) can be changed in place, so the
same object stays alive and every label sees the change.
Immutable objects (str, int, float, tuple, bool) can never be
changed, so every "change" produces a new object.
"""

# Program 1: A list keeps the same id after append()
items = [1, 2, 3]
before = id(items)
items.append(4)
print(before == id(items))              # True (same object, modified in place)

# Program 2: Two labels on a list vs two labels on a string
list_a = [1, 2]
list_b = list_a
list_a.append(3)
print(list_a, list_b)                   # [1, 2, 3] [1, 2, 3] (shared object changed)

text_a = "abc"
text_b = text_a
text_a += "d"
print(text_a, text_b)                   # abcd abc (b is unaffected)

# Program 3: Which types are immutable? (hashable is a good hint)
samples = ["text", 42, 3.5, (1, 2), [1, 2], {"a": 1}, {1, 2}]
for obj in samples:
    try:
        hash(obj)
        kind = "immutable (hashable)"
    except TypeError:
        kind = "mutable (unhashable)"
    print(f"{type(obj).__name__:<8} -> {kind}")


# =====================================================
# Concept 7: Understanding Memory with id() and is
# =====================================================
"""
Definition:
id(obj) gives the identity (memory address) of an object.
a is b is True when both labels point to the SAME object.
Equal values (==) do not always mean the same object (is).
"""

# Program 1: Two labels, one object
a = "Ali"
b = a
print(a is b)                           # True
print(id(a) == id(b))                   # True

# Program 2: Compare the id behaviour of a list and a string
numbers = [1, 2, 3]
word = "abc"
numbers_id = id(numbers)
word_id = id(word)
numbers.append(4)
word = word + "d"
print("List id same after change:  ", numbers_id == id(numbers))    # True
print("String id same after change:", word_id == id(word))          # False

# Program 3: Equal text can come from two different objects
part1 = "hel"
part2 = "lo"
joined = part1 + part2                  # built while the program runs
print(joined == "hello")                # True  (values are equal)
# print(joined is "hello")              # Not reliable, never use 'is' to compare text


# =====================================================
# Concept 8: String Methods Return New Strings
# =====================================================
"""
Definition:
No string method changes the original string. Each one returns a new
value. If you do not store the returned value, it is lost.
This is the most common beginner mistake.
"""

# Program 1: strip() returns a cleaned copy
text = "  hello  "
cleaned = text.strip()
print(repr(text), repr(cleaned))        # '  hello  ' 'hello'

# Program 2: Forgetting to store the result
text = "hello"
text.replace("h", "J")                  # result is thrown away
print(text)                             # hello (unchanged)
text = text.replace("h", "J")           # store it back
print(text)                             # Jello

# Program 3: Chain methods, every step returns a new string
raw = "  pYTHON  "
print(raw.strip().lower().capitalize()) # Python
print(repr(raw))                        # '  pYTHON  ' (original is still the same)


# =====================================================
# Concept 9: Operations That LOOK Like Modification
# =====================================================
"""
Definition:
+=, slicing plus concatenation and replace() all look like they edit
the string, but each one creates a new object and then reassigns
the variable.
"""

# Program 1: += is concatenation plus reassignment
title = "Test"
title += " Report"                      # same as title = title + " Report"
print(title)                            # Test Report

# Program 2: "Change" the first letter with slicing
name = "Ali"
name = "M" + name[1:]
print(name)                             # Mli

# Program 3: "Change" the character at any index
text = "hello"
index = 1
new_text = text[:index] + "a" + text[index + 1:]
print(new_text)                         # hallo
print(text)                             # hello (original untouched)


# =====================================================
# Concept 10: Ways to "Modify" a String Properly
# =====================================================
"""
Definition:
When you need many character-level edits, convert the string to a
list of characters (mutable), edit the list, then join it back.
bytearray is a mutable sequence of bytes and also works for
ASCII-style text.
"""

# Program 1: Replace the first character using a list
chars = list("hello")
chars[0] = "J"
print("".join(chars))                   # Jello

# Program 2: Reverse in place using a list
chars = list("python")
chars.reverse()
print("".join(chars))                   # nohtyp

# Program 3: Swap the first and last characters
chars = list("abcd")
chars[0], chars[3] = chars[3], chars[0]
print("".join(chars))                   # dbca

# Program 4: bytearray is mutable (bytes are numbers, ord() gives the number)
data = bytearray(b"hello")
data[0] = ord("J")
print(data.decode())                    # Jello


# =====================================================
# Concept 11: Immutability Makes Functions Safe
# =====================================================
"""
Definition:
A function cannot change the caller's string. Reassigning the
parameter inside the function only moves the LOCAL label.
A list passed to a function CAN be changed by it, which is why
immutable data is safer to pass around.
"""

# Program 1: The original string is protected
def make_upper(text):
    text = text.upper()                 # local label points to a new object
    return text

original = "ali"
result = make_upper(original)
print(original, result)                 # ali ALI

# Program 2: A list can be changed by a function
def add_item(items):
    items.append("x")                   # modifies the caller's list in place

data = ["a"]
add_item(data)
print(data)                             # ['a', 'x']

# Program 3: The function receives the very same object (no copy)
def get_id(value):
    return id(value)

word = "Ali"
print(get_id(word) == id(word))         # True


# =====================================================
# Concept 12: Hashing and Dictionary Keys
# =====================================================
"""
Definition:
Only hashable (practically: immutable) objects can be dictionary keys
or set items. A string never changes, so its hash never changes,
which makes it a safe key. (Hash numbers differ between runs.)
"""

# Program 1: Strings as dictionary keys
results = {"test_login": "Passed", "test_logout": "Failed"}
print(results["test_login"])            # Passed

# Program 2: Equal strings always have equal hashes (within one run)
print(hash("abc") == hash("abc"))       # True

# Program 3: A list cannot be a key
try:
    broken = {[1, 2]: "value"}
except TypeError as e:
    print("Error:", e)                  # unhashable type: 'list'

# Program 4: A set removes duplicate strings
names = ["ali", "sara", "ali", "bilal", "sara"]
print(set(names), len(set(names)))      # (3 unique names, order may vary)


# =====================================================
# Concept 13: Building Strings Efficiently
# =====================================================
"""
Definition:
Because every += can create a new string, building a very large
string step by step can be slow. Collect the pieces in a list and
call "".join() once. Timing depends on your computer and Python
version (CPython sometimes optimizes +=), but join() is always the
safe, recommended style.
"""

import time

# Program 1: Build the same text in two ways and time both
start = time.perf_counter()
result_plus = ""
for i in range(50000):
    result_plus += "x"
time_plus = time.perf_counter() - start

start = time.perf_counter()
pieces = []
for i in range(50000):
    pieces.append("x")
result_join = "".join(pieces)
time_join = time.perf_counter() - start

print(f"+= : {time_plus:.4f}s | join: {time_join:.4f}s")
print(result_plus == result_join)       # True (same final text)

# Program 2: Build a numbered report with join()
lines = []
for number in range(1, 4):
    lines.append(f"Line {number}")
print("\n".join(lines))

# Program 3: Build a comma separated string without a trailing comma
values = ["10", "20", "30"]
print(",".join(values))                 # 10,20,30


# =====================================================
# Concept 14: Immutability in SQA Automation
# =====================================================
"""
Definition:
Expected values (titles, URLs, messages) stored as strings cannot be
changed by accident, test data can safely be used as dictionary keys,
and cleaning a value creates a new string, so the raw value stays
available for your report.
"""

# Program 1: The expected value stays safe while the actual value is cleaned
expected_title = "Login Page"
raw_title = "  login page \xa0"
actual_title = raw_title.strip().title()
print(repr(raw_title))                  # raw text exactly as the page gave it
print(repr(actual_title))               # 'Login Page'
print("Match:", expected_title == actual_title)     # True
print("Expected still:", expected_title)            # Login Page

# Program 2: Test case IDs as dictionary keys
test_results = {"TC_LOGIN_001": "PASS", "TC_LOGIN_002": "FAIL", "TC_CART_001": "PASS"}
for test_id, status in test_results.items():
    print(f"{test_id:<14}{status}")

# Program 3: Normalize an email but keep the raw value for the report
raw_email = "  Admin@Test.COM \n"
normalized = raw_email.strip().lower()
print("Raw:       ", repr(raw_email))
print("Normalized:", repr(normalized))