"""
====================================================
09_Strings / 07_string_methods.py
====================================================
Topic: String Methods (Introduction + Case Conversion)
====================================================
"""

# =====================================================
# Concept 1: What is a String Method?
# =====================================================
"""
Definition:
A method is a function that belongs to a string object.
It is called with a dot: string.method().
Because strings are immutable, a method never changes the original
string. It always RETURNS a new string (or a new value).
"""

# Program 1: Call a method on a string
text = "hello"
print(text.upper())             # HELLO

# Program 2: The original string stays unchanged
text = "hello"
new_text = text.upper()
print("Original:", text)       # hello
print("New:", new_text)         # HELLO

# Program 3: If you do not store the result, it is lost
text = "hello"
text.upper()                    # result is thrown away
print(text)                     # hello (still lowercase)
text = text.upper()             # store the result back in the variable
print(text)                     # HELLO

# =====================================================
# Concept 2: upper()
# =====================================================
"""
Definition:
upper() returns a copy of the string with ALL letters in
capital (uppercase) form. Numbers and symbols stay as they are.
"""

# Program 1: Convert a sentence to uppercase
text = "hello world"
print(text.upper())             # HELLO WORLD

# Program 2: Numbers and symbols are not affected
print("python 3.12 #1".upper()) # PYTHON 3.12 #1

# Program 3: Convert user input to uppercase
user_input = input("Enter your city: ")
print("City in capitals:", user_input.upper())

# =====================================================
# Concept 3: lower()
# =====================================================
"""
Definition:
lower() returns a copy of the string with ALL letters in
small (lowercase) form.
"""
# Program 1: Convert a sentence to lowercase
text = "HELLO WORLD"
print(text.lower())             # hello world

# Program 2: Make a mixed-case word lowercase
print("PyThOn".lower())         # python

# Program 3: Case-insensitive check of a username
username = "Ali"
if username.lower() == "ali":
    print("Username matched")

# =====================================================
# Concept 4: capitalize()
# =====================================================
"""
Definition:
capitalize() makes the FIRST character of the whole string a capital
letter and turns all the other letters into lowercase.
"""

# Program 1: Capitalize a lowercase sentence
text = "python programming"
print(text.capitalize())        # Python programming

# Program 2: The rest of the letters are forced to lowercase
text = "pYTHON PROGRAMMING"
print(text.capitalize())        # Python programming

# Program 3: Only the first letter of the string changes, not every word
print("hello world".capitalize())   # Hello world

# =====================================================
# Concept 5: title()
# =====================================================
"""
Definition:
title() makes the first letter of EVERY word a capital letter and the
rest of each word lowercase.
Note: it treats an apostrophe as a word break, so names like
"it's" can look odd.
"""

# Program 1: Title case for a sentence
text = "python programming language"
print(text.title())             # Python Programming Language

# Program 2: Fix a badly typed name
name = "aLI kHAN"
print(name.title())             # Ali Khan

# Program 3: Show the apostrophe behaviour
print("it's a test".title())    # It'S A Test

# =====================================================
# Concept 6: swapcase()
# =====================================================
"""
Definition:
swapcase() changes uppercase letters to lowercase and lowercase
letters to uppercase at the same time.
"""

# Program 1: Swap the case of a sentence
text = "Hello World"
print(text.swapcase())          # hELLO wORLD

# Program 2: Swapping twice gives the original text back
text = "Python"
print(text.swapcase().swapcase())   # Python

# Program 3: Swap the case of a mixed string with digits
print("AbC123xYz".swapcase())   # aBc123XyZ


# =====================================================
# Concept 7: casefold()
# =====================================================
"""
Definition:
casefold() is a stronger version of lower(), made for case-insensitive
comparison. It also handles special characters of other languages,
for example the German letter ß becomes "ss".
For normal English text, lower() and casefold() give the same result.
"""

# Program 1: Same result as lower() for English text
print("HELLO".casefold())       # hello

# Program 2: casefold() handles the German ß, lower() does not
print("straße".lower())         # straße
print("straße".casefold())      # strasse

# Program 3: Compare two German spellings
word1 = "STRASSE"
word2 = "straße"
print(word1.lower() == word2.lower())           # False
print(word1.casefold() == word2.casefold())     # True



# =====================================================
# Concept 8: Method Chaining
# =====================================================

"""
Definition:
Because every string method returns a new string, you can call
another method straight on the result. This is called chaining,
and it runs from left to right.
"""

# Program 1: Chain two methods
text = "  hello world  "
print(text.strip().upper())     # HELLO WORLD

# Program 2: Chain three methods
text = "  pYTHON is FUN  "
print(text.strip().lower().capitalize())    # Python is fun

# Program 3: Clean and format user input in one line
name = input("Enter your full name: ")
print(name.strip().title())


# =====================================================
# Concept 9: Case-Insensitive Comparison
# =====================================================
"""
Definition:
Comparing strings with == is case-sensitive. To ignore the case,
convert both sides with lower() (or casefold()) before comparing.
"""


# Program 1: Plain comparison fails because of the case
print("PASSED" == "passed")                     # False

# Program 2: Convert both sides first
print("PASSED".lower() == "passed".lower())     # True

# Program 3: Check an expected status against an actual status
expected_status = "PASSED"
actual_status = "Passed"
if expected_status.casefold() == actual_status.casefold():
    print("Status matches")
else:
    print("Status does not match")



# =====================================================
# Concept 10: Checking All Methods Of a String (Bonus)
# =====================================================
"""
Definition:
dir(str) lists every method a string has, and help(str.method)
shows what a method does. This is how you can explore methods
yourself while coding.
"""

# Program 1: Count how many names are available on str
print(len(dir(str)))

# Program 2: Show only the public method names that start with 'is'
print([m for m in dir(str) if m.startswith("is")])

# Program 3: Read the built-in help of one method
help(str.upper)


























































