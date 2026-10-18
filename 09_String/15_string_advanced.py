r"""
====================================================
09_Strings / 15_string_advanced.py
====================================================
Topic: Advanced String Techniques
====================================================
Notes before you run this file:
1) removeprefix() and removesuffix() need Python 3.9 or newer.
2) Results marked "typical" depend on how CPython works internally.
   Never base the logic of a real program on them.
3) Timing numbers differ on every computer. Compare them, don't
   memorise them.
"""

import sys
import copy
import time
import re
import string
import random
import difflib
import textwrap
import unicodedata


# =====================================================
# Concept 1: Concatenation Performance
# =====================================================
"""
Definition:
Every + creates a NEW string object (strings are immutable), so
building a big string with += in a loop copies the growing text again
and again. CPython sometimes optimizes this, but you cannot rely on it.
For a few pieces + is fine. For many pieces, collect them in a list
and use join() once.
"""

# Program 1: Build the same text in two ways and time both
count = 50000

start = time.perf_counter()
result_plus = ""
for i in range(count):
    result_plus += "x"
time_plus = time.perf_counter() - start

start = time.perf_counter()
pieces = []
for i in range(count):
    pieces.append("x")
result_join = "".join(pieces)
time_join = time.perf_counter() - start

print(f"+= : {time_plus:.4f}s | join: {time_join:.4f}s")
print(result_plus == result_join)       # True (same final text)

# Program 2: Show how many different objects += creates
text = ""
ids = set()
for i in range(5):
    text += "ab"
    ids.add(id(text))
print(len(ids))                         # 5 (typical): a new object at every step

# Program 3: For a few pieces, + and f-strings are both fine
name = "Ali"
city = "Lahore"
print(name + " lives in " + city)
print(f"{name} lives in {city}")        # usually the most readable choice


# =====================================================
# Concept 2: Why join() is Better
# =====================================================
"""
Definition:
join() first looks at all the pieces, calculates the final size, and
builds the result in ONE step. It accepts any iterable of strings
(list, tuple, dict keys, a generator). The separator is written
before .join( ). Every item must be a string.
"""

# Program 1: join() with a generator
print(",".join(str(i) for i in range(5)))       # 0,1,2,3,4

# Program 2: join() over a dictionary joins its KEYS
data = {"a": 1, "b": 2}
print(",".join(data))                   # a,b

# Program 3: Sort the pieces first, then join
print(", ".join(sorted(["pear", "apple", "fig"])))      # apple, fig, pear

# Program 4: Edge cases
print(repr(",".join([])))               # ''
print(",".join(["only"]))               # only

# Program 5: Non-string items raise TypeError
try:
    ",".join([1, 2, 3])
except TypeError as e:
    print(type(e).__name__)             # TypeError

# Program 6: join() never leaves a trailing separator
result = ""
for word in ["a", "b", "c"]:
    result += word + ","
print(result)                           # a,b,c,   (extra comma at the end)
print(",".join(["a", "b", "c"]))        # a,b,c


# =====================================================
# Concept 3: String Copying
# =====================================================
"""
Definition:
Because a string can never change, Python does not need to create a
real copy. [:], str(), copy.copy() and copy.deepcopy() all normally
return the SAME object. Real copying matters for mutable types such
as lists. You only get a new object when you build a new string.
"""

# Program 1: Every "copy" is the same object (typical)
original = "Python" * 10
print(original[:] is original)          # True
print(str(original) is original)        # True
print(copy.copy(original) is original)  # True
print(copy.deepcopy(original) is original)      # True

# Program 2: Force a new object with equal value
new_object = (original + "!")[:-1]
print(new_object == original)           # True  (same value)
print(new_object is original)           # False (different object)

# Program 3: Lists are different: [:] creates a new list
numbers = [1, [2, 3]]
shallow = numbers[:]
deep = copy.deepcopy(numbers)
print(shallow is numbers)               # False
print(shallow[1] is numbers[1])         # True  (inner list is shared)
print(deep[1] is numbers[1])            # False (everything copied)

# Program 4: Why a string copy is not needed
a = "Ali"
b = a
b = b + " Khan"                         # b gets a new object, a is untouched
print(a, "|", b)                        # Ali | Ali Khan


# =====================================================
# Concept 4: String Comparison
# =====================================================
"""
Definition:
Strings are compared by the Unicode number of their characters, from
left to right, until the first difference. Sorting, min() and max()
use the same rule, so capitals come before lowercase letters, and
"10" is smaller than "9" because "1" is smaller than "9".
"""

# Program 1: Default sorting is case-sensitive
words = ["banana", "Cherry", "apple", "Banana"]
print(sorted(words))                    # ['Banana', 'Cherry', 'apple', 'banana']

# Program 2: Case-insensitive sorting with a key
print(sorted(words, key=str.casefold))  # ['apple', 'banana', 'Banana', 'Cherry']

# Program 3: Sort by length (equal lengths keep their original order)
print(sorted(["pear", "fig", "banana", "kiwi"], key=len))   # ['fig', 'pear', 'kiwi', 'banana']

# Program 4: min() and max()
fruits = ["apple", "banana", "cherry"]
print(min(fruits), max(fruits))         # apple cherry
print(max(fruits, key=len))             # banana (first of the longest)

# Program 5: Numbers stored as text compare like text
print("10" < "9")                       # True
print(int("10") < int("9"))             # False
files = ["file10", "file2", "file1"]
print(sorted(files))                    # ['file1', 'file10', 'file2']
print(sorted(files, key=lambda f: int(f[4:])))      # ['file1', 'file2', 'file10']

# Program 6: Chained comparison and different types
print("a" < "b" < "c")                  # True
print("5" == 5)                         # False (different types are never equal)


# =====================================================
# Concept 5: Case-Insensitive Comparison
# =====================================================
"""
Definition:
== is case-sensitive. To ignore the case, convert BOTH sides first
(lower() or casefold()), or use re.IGNORECASE. Never convert only
one side.
"""

# Program 1: Compare after lower()
print("Passed" == "PASSED")             # False
print("Passed".lower() == "PASSED".lower())     # True

# Program 2: Case-insensitive search with 'in'
text = "I love PYTHON programming"
print("python" in text.lower())         # True

# Program 3: Case-insensitive startswith and endswith
filename = "Report.PDF"
print(filename.lower().endswith(".pdf"))        # True
print(filename.casefold().startswith("report")) # True

# Program 4: Case-insensitive match with a regular expression
print(re.search("python", text, re.IGNORECASE) is not None)     # True

# Program 5: Check a value against a list of allowed values
allowed = ["PASS", "FAIL", "SKIP"]
status = "pass"
print(status.upper() in allowed)        # True


# =====================================================
# Concept 6: casefold()
# =====================================================
"""
Definition:
casefold() is a stronger lower(), designed for comparing text.
It knows special rules of other languages, for example the German
"ß" becomes "ss" and the Greek final sigma "ς" becomes "σ".
Use it for comparing, not for showing text to users.
"""

# Program 1: German sharp s
print("ß".lower(), "ß".casefold())      # ß ss

# Program 2: Greek final sigma
print("ς".lower() == "σ")               # False
print("ς".casefold() == "σ")            # True

# Program 3: Compare two spellings
print("STRASSE".lower() == "straße".lower())            # False
print("STRASSE".casefold() == "straße".casefold())      # True

# Program 4: For English text lower() and casefold() agree
print("Hello".lower() == "Hello".casefold())            # True

# Program 5: A careful comparison: normalize + strip + casefold
expected = "Café"
actual = "  CAFE\u0301 "                # E + combining accent, with extra spaces
a = unicodedata.normalize("NFC", expected.strip()).casefold()
b = unicodedata.normalize("NFC", actual.strip()).casefold()
print(a == b)                           # True


# =====================================================
# Concept 7: partition()
# =====================================================
"""
Definition:
partition(sep) splits at the FIRST separator and always returns a
tuple of exactly three items: (before, separator, after).
If the separator is missing, you get (whole string, "", "").
"""

# Program 1: Split an email
user, at, domain = "ali@example.com".partition("@")
print(user, at, domain)                 # ali @ example.com

# Program 2: A missing separator
print("hello".partition("@"))           # ('hello', '', '')

# Program 3: Read config lines and detect a missing value
lines = ["host=localhost", "port=8080", "debug"]
for line in lines:
    key, sep, value = line.partition("=")
    if sep == "":
        print(f"{key}: no value given")
    else:
        print(f"{key} -> {value}")

# Program 4: Split a URL at ://
print("https://example.com/path".partition("://"))      # ('https', '://', 'example.com/path')

# Program 5: partition() vs split() with maxsplit 1
print("a=b=c".partition("="))           # ('a', '=', 'b=c')
print("a=b=c".split("=", 1))            # ['a', 'b=c']


# =====================================================
# Concept 8: rpartition()
# =====================================================
"""
Definition:
rpartition(sep) splits at the LAST separator and returns
(before, separator, after). If the separator is missing, the whole
string ends up in the LAST item: ("", "", whole string).
"""

# Program 1: Get the file name from a path
folder, sep, filename = "C:/data/reports/final.xlsx".rpartition("/")
print(folder)                           # C:/data/reports
print(filename)                         # final.xlsx

# Program 2: A missing separator (note: opposite of partition)
print("hello".rpartition("/"))          # ('', '', 'hello')

# Program 3: File extension of a name with several dots
print("archive.tar.gz".rpartition("."))         # ('archive.tar', '.', 'gz')

# Program 4: The last part of a domain
print("ali@mail.example.co.uk".rpartition(".")[2])      # uk


# =====================================================
# Concept 9: splitlines()
# =====================================================
r"""
Definition:
splitlines() breaks text at every kind of line ending (\n, \r\n, \r
and a few more) and returns a list of lines. A final line ending does
not create an extra empty item. keepends=True keeps the endings.
"""

# Program 1: Mixed line endings
print("a\nb\r\nc\rd".splitlines())       # ['a', 'b', 'c', 'd']

# Program 2: Why split("\n") is not enough
print("a\r\nb".split("\n"))             # ['a\r', 'b']
print("a\r\nb".splitlines())            # ['a', 'b']

# Program 3: Keep the line endings
print("a\nb\n".splitlines(keepends=True))       # ['a\n', 'b\n']

# Program 4: Empty and almost empty text
print("".splitlines())                   # []
print("\n".splitlines())                 # ['']
print("a\n".splitlines())                # ['a']
print("a\n".split("\n"))                 # ['a', '']

# Program 5: Count the non-blank lines of a log
log = """[PASS] Login
[FAIL] Cart

[PASS] Logout"""
non_blank = 0
for line in log.splitlines():
    if line.strip() == "":
        continue
    non_blank += 1
print(non_blank)                         # 3


# =====================================================
# Concept 10: removeprefix() and removesuffix()
# =====================================================
"""
Definition:
removeprefix(text) removes an exact piece of text from the START,
removesuffix(text) from the END, but only ONE time and only if it is
really there. strip(chars) is different: it removes any characters of
a SET, as many times as they appear.
"""

# Program 1: Basic use
print("test_login.py".removeprefix("test_"))        # login.py
print("test_login.py".removesuffix(".py"))          # test_login

# Program 2: Only one occurrence is removed
print("testtest_a".removeprefix("test"))            # test_a

# Program 3: Difference from lstrip()
print("aaab".lstrip("a"))                           # b
print("aaab".removeprefix("a"))                     # aab

# Program 4: Clean a list of file names
files = ["test_login.py", "test_cart.py", "helper.py"]
for f in files:
    if f.startswith("test_") and f.endswith(".py"):
        print(f.removeprefix("test_").removesuffix(".py"))      # login  cart

# Program 5: Clean a URL step by step
url = "https://www.example.com"
print(url.removeprefix("https://").removeprefix("www."))        # example.com

# Program 6: Check the Python version
print(sys.version_info >= (3, 9))       # True if these methods are available


# =====================================================
# Concept 11: expandtabs()
# =====================================================
r"""
Definition:
expandtabs(tabsize=8) replaces every tab (\t) with spaces so that the
text continues at the next "tab stop" (a multiple of tabsize). The
number of spaces depends on the current column, and the column count
restarts after every new line.
"""

# Program 1: Different tab sizes
print(repr("Hi\tAli".expandtabs(4)))     # 'Hi  Ali'
print(repr("Hi\tAli".expandtabs()))      # 'Hi      Ali'  (default is 8)

# Program 2: A tab at an exact tab stop moves to the NEXT stop
print(repr("abcd\tx".expandtabs(4)))     # 'abcd    x'

# Program 3: Align a small table
table = "Name\tScore\nAli\t95\nSara\t88"
print(table.expandtabs(8))

# Program 4: Special tab sizes
print("a\tb".expandtabs(0))              # ab  (tabs are removed)
print("a\tb".expandtabs(1))              # a b

# Program 5: The same tab gives different gaps in different columns
for word in ["A", "AB", "ABC"]:
    print(repr((word + "\t|").expandtabs(4)))


# =====================================================
# Concept 12: center()
# =====================================================
"""
Definition:
center(width, fillchar=" ") puts the string in the middle of a field
of the given width. fillchar must be exactly ONE character.
If width is smaller than the string, nothing changes.
If the padding is odd, one side gets one extra character.
"""

# Program 1: Default fill is a space
print("[" + "Hi".center(10) + "]")       # [    Hi    ]

# Program 2: Custom fill character
print("Hi".center(10, "*"))              # ****Hi****

# Program 3: Width smaller than the text
print("Hello".center(3))                 # Hello

# Program 4: A report heading
print(" REPORT ".center(30, "="))        # =========== REPORT ===========

# Program 5: The fill character must be one character
try:
    "Hi".center(10, "ab")
except TypeError as e:
    print(type(e).__name__)              # TypeError

# Program 6: Odd padding (one side gets the extra character)
print("Hi".center(5, "*"))               # typical: **Hi*


# =====================================================
# Concept 13: ljust() and rjust()
# =====================================================
"""
Definition:
ljust(width, fillchar) pads on the RIGHT, so the text stays on the left.
rjust(width, fillchar) pads on the LEFT, so the text stays on the right.
They never cut the text. Numbers must be converted with str() first.
"""

# Program 1: Basic use
print("Hi".ljust(6, "."))                # Hi....
print("Hi".rjust(6, "."))                # ....Hi

# Program 2: A table with aligned columns
rows = [("Ali", 95), ("Sara", 88), ("Bilal", 79)]
print("Name".ljust(10) + "Score".rjust(7))
print("-" * 17)
for name, score in rows:
    print(name.ljust(10) + str(score).rjust(7))

# Program 3: A menu with dotted lines
print("Coffee".ljust(15, ".") + "$3.50")
print("Sandwich".ljust(15, ".") + "$6.00")

# Program 4: A number needs str() first
try:
    (5).rjust(3)
except AttributeError as e:
    print(type(e).__name__)              # AttributeError
print(str(5).rjust(3, "0"))              # 005

# Program 5: Same result as the f-string alignment
print("Hi".ljust(6, ".") == f"{'Hi':.<6}")      # True
print("Hi".rjust(6, ".") == f"{'Hi':.>6}")      # True

# Program 6: Text longer than the width is never cut
print("Automation".ljust(5))             # Automation


# =====================================================
# Concept 14: zfill()
# =====================================================
"""
Definition:
zfill(width) pads the string on the left with zeros up to the given
width. It understands a leading + or - sign and keeps the sign in
front. It also works on any string, not only digits.
"""

# Program 1: Basic use
print("5".zfill(3))                      # 005
print("42".zfill(5))                     # 00042

# Program 2: The sign stays in front
print("-5".zfill(4))                     # -005
print("+5".zfill(4))                     # +005

# Program 3: Compare with rjust("0")
print("-5".rjust(4, "0"))                # 00-5  (the minus sign is in the wrong place)
print("-5".zfill(4))                     # -005

# Program 4: Width smaller than the text
print("12345".zfill(3))                  # 12345

# Program 5: It pads any string with zeros
print("abc".zfill(6))                    # 000abc

# Program 6: Invoice number and clock time
print("INV-" + str(42).zfill(6))         # INV-000042
print(str(5).zfill(2) + ":" + str(9).zfill(2))      # 05:09

# Program 7: The f-string equivalent
print(f"{42:06}", f"{-5:04}")            # 000042 -005


# =====================================================
# Concept 15: textwrap (Wrapping Long Text)
# =====================================================
"""
Definition:
The textwrap module formats long text:
wrap() -> list of lines no longer than width
fill() -> the same, joined into one string with new lines
shorten() -> cuts to a width and adds " [...]"
dedent() -> removes the common indentation
indent() -> adds a prefix to every line
"""

# Program 1: wrap() and fill()
text = "Python is a powerful programming language for automation"
print(textwrap.wrap(text, width=20))    # ['Python is a powerful', 'programming language', 'for automation']
print(textwrap.fill(text, width=20))

# Program 2: shorten() for long messages in a report
message = "Hello world this is long"
print(textwrap.shorten(message, width=15))      # Hello [...]

# Program 3: dedent() for a text written inside an indented block
if True:
    banner = """
        Test Run Started
        Environment: staging
    """
    print(textwrap.dedent(banner).strip())

# Program 4: indent() adds a prefix to every line
print(textwrap.indent("line one\nline two", "> "))      # > line one / > line two


# =====================================================
# Concept 16: difflib (Finding Differences)
# =====================================================
"""
Definition:
The difflib module compares texts.
SequenceMatcher(...).ratio() gives a similarity from 0.0 to 1.0.
unified_diff() shows which lines changed.
get_close_matches() suggests the closest words for a typo.
"""

# Program 1: How similar are two texts?
ratio = difflib.SequenceMatcher(None, "Login Page", "Login Pge").ratio()
print(f"{ratio:.2f}")                    # 0.95

# Program 2: Show the differences between expected and actual lines
expected_lines = ["Login", "Welcome Ali", "Logout"]
actual_lines = ["Login", "Welcome Alia", "Logout"]
for line in difflib.unified_diff(expected_lines, actual_lines,
                                 fromfile="expected", tofile="actual", lineterm=""):
    print(line)
# --- expected
# +++ actual
# @@ -1,3 +1,3 @@
#  Login
# -Welcome Ali
# +Welcome Alia
#  Logout

# Program 3: Suggest the closest word for a typo
print(difflib.get_close_matches("aple", ["apple", "banana", "cherry"]))     # ['apple']

# Program 4: Identical texts have a ratio of 1.0
print(difflib.SequenceMatcher(None, "abc", "abc").ratio())      # 1.0


# =====================================================
# Concept 17: The string Module
# =====================================================
"""
Definition:
The string module contains ready-made character sets and helpers:
ascii_lowercase, ascii_uppercase, ascii_letters, digits, punctuation,
whitespace, capwords() and Template.
"""

# Program 1: The constants
print(string.ascii_lowercase)            # abcdefghijklmnopqrstuvwxyz
print(string.digits)                     # 0123456789
print(len(string.ascii_letters), len(string.punctuation))      # 52 32

# Program 2: Count the kinds of characters in a text
text = "Test@123 OK!"
letters = digits = punct = spaces = 0
for ch in text:
    if ch in string.ascii_letters:
        letters += 1
    elif ch in string.digits:
        digits += 1
    elif ch in string.punctuation:
        punct += 1
    elif ch in string.whitespace:
        spaces += 1
print(letters, digits, punct, spaces)    # 6 3 2 1

# Program 3: Generate a random test password
chars = string.ascii_letters + string.digits + string.punctuation
pieces = []
for _ in range(12):
    pieces.append(random.choice(chars))
password = "".join(pieces)
print(len(password))                     # 12

# Program 4: capwords() and Template
print(string.capwords("hello   wORLD"))                          # Hello World
template = string.Template("Hello $name, you are $age")
print(template.substitute(name="Ali", age=22))                   # Hello Ali, you are 22
print(template.safe_substitute(name="Ali"))                      # Hello Ali, you are $age


# =====================================================
# Concept 18: Advanced Techniques in SQA Automation
# =====================================================
"""
Definition:
Reports, test IDs, parsing, cleaning and comparing texts from web
pages use the techniques of this whole file together.
"""

# Program 1: A formatted test summary
results = [("Login", "PASS", 2.31), ("Checkout", "FAIL", 5.07), ("Logout", "PASS", 0.84)]
print(" TEST SUMMARY ".center(36, "="))
print("Test".ljust(14) + "Status".ljust(8) + "Time".rjust(8))
print("-" * 36)
for name, status, seconds in results:
    print(name.ljust(14) + status.ljust(8) + f"{seconds:.2f}s".rjust(8))
print("=" * 36)

# Program 2: Generate test case IDs
for number in range(1, 4):
    print("TC_LOGIN_" + str(number).zfill(3))     # TC_LOGIN_001  002  003

# Program 3: Robust expected vs actual comparison
pairs = [("Login Page", "  login\xa0PAGE "), ("Welcome", "Welcome!")]
for expected, actual in pairs:
    cleaned_actual = " ".join(actual.split()).casefold()
    cleaned_expected = " ".join(expected.split()).casefold()
    print(repr(actual), "->", cleaned_actual == cleaned_expected)   # True / False

# Program 4: Read header lines of a test report with partition
header = ["Browser: Chrome 120", "Env: staging", "Tester: Ali"]
info = {}
for line in header:
    key, sep, value = line.partition(":")
    info[key.strip()] = value.strip()
print(info)         # {'Browser': 'Chrome 120', 'Env': 'staging', 'Tester': 'Ali'}

# Program 5: Turn file names into test names
files = ["test_login.py", "test_cart.py", "conftest.py"]
for f in files:
    if f.startswith("test_"):
        print(f.removeprefix("test_").removesuffix(".py").replace("_", " ").title())

# Program 6: Show a long error message in a short form in the report
error = "ElementNotFoundException: could not locate the submit button on the checkout page"
print(textwrap.shorten(error, width=45))

# Program 7: Suggest the right status when a typo is found in test data
valid_statuses = ["PASS", "FAIL", "SKIP", "ERROR"]
typo = "PAS"
print(difflib.get_close_matches(typo.upper(), valid_statuses, n=1))     # ['PASS']