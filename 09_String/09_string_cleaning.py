r"""
====================================================
09_Strings / 09_string_cleaning.py
====================================================
Topic: String Cleaning (strip, replace, removing unwanted characters)
====================================================
Reminder: strings are immutable, so every cleaning method returns
a NEW string. Store the result in a variable to keep it.
"""

# =====================================================
# Concept 1: strip()
# =====================================================
r"""
Definition:
strip() removes whitespace (spaces, tabs \t, new lines \n) from BOTH
the start and the end of a string. It does not touch the middle.
"""

# Program 1: Remove spaces from both ends
text = "   Hello World   "
print(f"[{text}]")                  # [   Hello World   ]
print(f"[{text.strip()}]")          # [Hello World]

# Program 2: Tabs and new lines are removed too
text = "\t\n  hello  \n"
print(f"[{text.strip()}]")          # [hello]

# Program 3: The middle of the string is not touched
text = "  a   b  "
print(f"[{text.strip()}]")          # [a   b]

# Program 4: Clean user input
username = input("Enter username: ").strip()
print(f"[{username}]")


# =====================================================
# Concept 2: strip() with Characters
# =====================================================
"""
Definition:
strip(chars) removes any of the given characters from both ends,
not only whitespace. IMPORTANT: 'chars' is a SET of characters,
not a word. Python keeps removing while the end character is
inside that set.
"""

# Program 1: Remove a symbol from both ends
print("***Hi***".strip("*"))         # Hi

# Program 2: Remove several different characters
print("xyHelloyx".strip("xy"))       # Hello

# Program 3: It is a set of characters, not a prefix word
print("settings".strip("set"))       # ing  (s, e, t removed from both ends)


# =====================================================
# Concept 3: lstrip()
# =====================================================
"""
Definition:
lstrip() removes characters only from the LEFT (start) side.
"""

# Program 1: Remove leading spaces
text = "   Hello World   "
print(f"[{text.lstrip()}]")          # [Hello World   ]

# Program 2: Remove leading zeros from a number text
print("0001234".lstrip("0"))         # 1234

# Program 3: Remove a leading symbol
print("###Title".lstrip("#"))        # Title


# =====================================================
# Concept 4: rstrip()
# =====================================================
r"""
Definition:
rstrip() removes characters only from the RIGHT (end) side.
It is very common for removing the new line (\n) that is read
at the end of every line of a file.
"""

# Program 1: Remove trailing spaces
text = "   Hello World   "
print(f"[{text.rstrip()}]")          # [   Hello World]

# Program 2: Remove the new line at the end of a line
line = "Test passed\n"
print(repr(line))                    # 'Test passed\n'
print(repr(line.rstrip("\n")))       # 'Test passed'

# Program 3: Remove repeated punctuation at the end
print("Hello!!!".rstrip("!"))        # Hello


# =====================================================
# Concept 5: replace()
# =====================================================
"""
Definition:
replace(old, new) returns a copy where EVERY occurrence of 'old'
is changed to 'new'. It is case-sensitive.
"""

# Program 1: Replace a word
text = "I like Java. Java is good."
print(text.replace("Java", "Python"))   # I like Python. Python is good.

# Program 2: It is case-sensitive
print("Java java".replace("java", "X")) # Java X

# Program 3: Replace a single character
print("2026-10-17".replace("-", "/"))   # 2026/10/17


# =====================================================
# Concept 6: replace() with a Count
# =====================================================
"""
Definition:
replace(old, new, count) changes only the first 'count'
occurrences, counting from the left.
"""

# Program 1: Replace only the first match
print("Java Java Java".replace("Java", "Python", 1))   # Python Java Java

# Program 2: Replace the first two matches
print("a-b-c-d".replace("-", "+", 2))                  # a+b+c-d

# Program 3: A count of 0 changes nothing
print("hello".replace("l", "L", 0))                    # hello


# =====================================================
# Concept 7: Multiple Replacements
# =====================================================
"""
Definition:
For several replacements, chain replace() calls or loop over a
dictionary of old -> new pairs.
Be careful with the order: a later replacement can change the result
of an earlier one.
"""

# Program 1: Chain two replacements
text = "I love cats and dogs"
print(text.replace("cats", "birds").replace("dogs", "fish"))   # I love birds and fish

# Program 2: Loop over a dictionary
text = "I love cats and dogs"
changes = {"cats": "birds", "dogs": "fish"}
for old, new in changes.items():
    text = text.replace(old, new)
print(text)                                                    # I love birds and fish

# Program 3: Swapping two words needs a temporary placeholder
text = "cat dog"
print(text.replace("cat", "dog").replace("dog", "cat"))        # cat cat  (WRONG)
print(text.replace("cat", "@@").replace("dog", "cat").replace("@@", "dog"))   # dog cat (RIGHT)


# =====================================================
# Concept 8: Removing Unwanted Characters
# =====================================================
"""
Definition:
Replacing something with an empty string "" removes it completely.
A for loop with isalnum(), isdigit() or isalpha() can keep only the
characters you want.
"""

# Program 1: Remove all spaces
print("H e l l o".replace(" ", ""))        # Hello

# Program 2: Remove several unwanted symbols with a loop
text = "Price: $99.99!!!"
for char in "$!:":
    text = text.replace(char, "")
print(text)                                # Price 99.99

# Program 3: Keep only letters and digits
text = "Hello, World! 123"
clean = ""
for char in text:
    if char.isalnum():
        clean += char
print(clean)                               # HelloWorld123

# Program 4: Keep only the digits of a phone number
phone = "+49 (151) 234-567"
digits = ""
for char in phone:
    if char.isdigit():
        digits += char
print(digits)                              # 49151234567


# =====================================================
# Concept 9: translate() and maketrans()
# =====================================================
"""
Definition:
str.maketrans() builds a translation table and translate() applies it
to the whole string in one go.
maketrans("abc", "123")  -> a becomes 1, b becomes 2, c becomes 3
maketrans("", "", "xyz") -> the third argument lists characters to DELETE
"""

# Program 1: Delete several characters in one step
table = str.maketrans("", "", "$!:")
print("Price: $99.99!!!".translate(table))  # Price 99.99

# Program 2: Replace characters one-to-one
table = str.maketrans("abc", "123")
print("aabbcc".translate(table))            # 112233

# Program 3: Remove vowels from a word
table = str.maketrans("", "", "aeiouAEIOU")
print("Automation".translate(table))        # tmtn


# =====================================================
# Concept 10: removeprefix() and removesuffix()
# =====================================================
"""
Definition:
removeprefix(text) removes the given text from the START only if the
string really starts with it. removesuffix(text) does the same for the
END. Unlike strip(), they remove an exact piece of text, not a set of
characters. (Python 3.9 or newer)
"""

# Program 1: Remove a prefix and a suffix
filename = "test_login.py"
print(filename.removeprefix("test_"))       # login.py
print(filename.removesuffix(".py"))         # test_login

# Program 2: If the text does not match, nothing happens
print("main_app.py".removeprefix("test_"))  # main_app.py

# Program 3: Compare with strip() on the same text
print("settings".strip("set"))              # ing
print("settings".removeprefix("set"))       # tings


# =====================================================
# Concept 11: Normalizing Extra Spaces
# =====================================================
"""
Definition:
split() with no argument splits on any run of whitespace and ignores
the empty parts. Joining the pieces back with a single space removes
all the extra spaces, including the ones in the middle.
"""

# Program 1: Collapse repeated spaces
text = "  too    many   spaces  "
print(" ".join(text.split()))                # too many spaces

# Program 2: Clean a sentence typed carelessly
text = "Python   is\tfun\nand  easy"
print(" ".join(text.split()))                # Python is fun and easy

# Program 3: Compare with strip(), which only cleans the two ends
print(f"[{text.strip()}]")


# =====================================================
# Concept 12: Hidden Whitespace (Non-breaking Space)
# =====================================================
r"""
Definition:
Text copied from web pages can contain a non-breaking space (\xa0),
which looks like a normal space. strip() and split() treat it as
whitespace, but replace(" ", "") does NOT remove it.
"""

# Program 1: strip() removes it from the ends
button_text = "Submit\xa0"
print(repr(button_text))                    # 'Submit\xa0'
print(repr(button_text.strip()))            # 'Submit'

# Program 2: A normal space does not equal a non-breaking space
print(" " == "\xa0")                        # False

# Program 3: Replace it explicitly
text = "Hello\xa0World"
print(text.replace("\xa0", " "))            # Hello World


# =====================================================
# Concept 13: A Real Cleaning Workflow
# =====================================================
"""
Definition:
In real projects, several cleaning steps are combined: strip the
ends, fix the case, remove unwanted characters, normalize spaces.
"""

# Program 1: Clean an email address
raw_email = "  Ali.Khan@Example.COM \n"
print(raw_email.strip().lower())            # ali.khan@example.com

# Program 2: Clean a list of names with a loop
raw_names = ["  ali khan ", "SARA   ahmed", "\tbilal\n"]
for name in raw_names:
    cleaned = " ".join(name.split()).title()
    print(f"[{cleaned}]")                   # [Ali Khan] [Sara Ahmed] [Bilal]

# Program 3: Clean log lines before analysing them
log_lines = ["  [PASS] Login test\n", "[FAIL]  Checkout test  \n", "\n"]
for line in log_lines:
    line = line.strip()
    if line == "":
        continue                            # skip empty lines
    print(line)



































    