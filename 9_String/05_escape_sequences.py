"""
====================================================
09_Strings / 04_string_operators.py
====================================================
Topic: String Operators
====================================================
"""

# =====================================================
# Concept 1: + (Concatenation)
# =====================================================
"""
Definition:
The + operator joins two or more strings into one new, longer string.
It works only between strings. A number must be converted with str() first.
"""

# Program 1: Join first name and last name with a space in between
first_name = "Ali"
last_name = "Khan"
full_name = first_name + " " + last_name
print(full_name)                    # Ali Khan

# Program 2: Join text with a number using str()
age = 25
print("Age: " + str(age))           # Age: 25

# Program 3: Show the error when a string and an int are joined directly
try:
    print("Age: " + age)
except TypeError as e:
    print("Error:", e)

# =====================================================
# Concept 2: * (Repetition)
# =====================================================
"""
Definition:
The * operator repeats a string a given number of times.
"""

# Program 1: Create a separator line
line = "-" * 20
print(line)

# Program 2: Repeat a short word
word = "Ab"
print(word * 3)                     # AbAbAb

# Program 3: Print a report heading with separator lines
print("=" * 30)
print("Test Results")
print("=" * 30)


# =====================================================
# Concept 3: in (Membership)
# =====================================================
"""
Definition:
The 'in' operator checks whether a substring exists inside a bigger
string. It returns True or False and is case-sensitive.
"""

# Program 1: Check if a word exists in a sentence
sentence = "I love Python programming"
print("Python" in sentence)         # True
print("Java" in sentence)           # False

# Program 2: Show that 'in' is case-sensitive
print("python" in sentence)         # False (lowercase p)

# Program 3: Make the check case-insensitive using lower()
print("python" in sentence.lower()) # True


# =====================================================
# Concept 4: not in
# =====================================================
"""
Definition:
The 'not in' operator is the opposite of 'in'. It returns True when
the substring does NOT exist inside the string.
"""

# Program 1: Check that a word is missing
sentence = "I love Python programming"
print("Java" not in sentence)       # True
print("Python" not in sentence)     # False

# Program 2: Validate that a password contains no spaces
password = "abc123"
if " " not in password:
    print("Valid password")
else:
    print("Invalid: password contains a space")

# Program 3: Validate that an email contains the @ symbol
email = "userexample.com"
if "@" not in email:
    print("Invalid email: @ is missing")


# =====================================================
# Concept 5: == and !=
# =====================================================
"""
Definition:
== checks whether two strings are exactly the same.
!= checks whether they are different.
Both compare character by character and are case-sensitive.
"""

# Program 1: Compare two identical strings
print("Python" == "Python")         # True

# Program 2: Show that case matters
password1 = "Python123"
password2 = "python123"
print(password1 == password2)       # False
print(password1 != password2)       # True

# Program 3: Simple username check
username = input("Enter username: ")
if username == "admin":
    print("Welcome Admin")
else:
    print("Access Denied")


# =====================================================
# Concept 6: <  >  <=  >=
# =====================================================
"""
Definition:
Strings can be compared with <, >, <= and >=.
The comparison follows dictionary (alphabetical) order, but it is
really based on the Unicode number of each character.
"""

# Program 1: Basic alphabetical comparison
print("apple" < "banana")           # True
print("banana" > "apple")           # True

# Program 2: Equal strings with <= and >=
print("apple" <= "apple")           # True
print("apple" >= "apple")           # True

# Program 3: Strings with the same start are decided by the first difference
print("cat" > "car")                # True ('t' comes after 'r')


# =====================================================
# Concept 7: Lexicographical Comparison
# =====================================================
"""
Definition:
Python compares two strings from left to right, one character at a
time, using each character's Unicode number (ord). It stops at the
first pair of characters that differ.
Important: capital letters (65-90) have SMALLER numbers than
lowercase letters (97-122).
"""

# Program 1: See the Unicode numbers behind the comparison
print(ord("A"), ord("B"), ord("a"))     # 65 66 97

# Program 2: Capital letters are "smaller" than lowercase letters
print("Zebra" < "apple")            # True because ord('Z')=90 < ord('a')=97
print("apple" < "Apple")            # False because ord('a')=97 > ord('A')=65

# Program 3: A shorter string is smaller when it matches the start of a longer one
print("car" < "cart")               # True

# Program 4: Step-by-step comparison shown with a loop
a = "cat"
b = "car"
for i in range(len(a)):
    print(a[i], ord(a[i]), "vs", b[i], ord(b[i]))
    if a[i] != b[i]:
        print("First difference found at index", i)
        break


# =====================================================
# Concept 8: Escape Characters (Quick Introduction)
# =====================================================
"""
Definition:
Escape characters start with a backslash (\\) and let you put special
characters inside a string, such as a new line (\\n) or a tab (\\t).
Full details and more programs are in 05_escape_sequences.py.
"""

# Program 1: New line
print("Line One\nLine Two")

# Program 2: Tab
print("Name:\tAli")

# Program 3: Quote inside a string
print("She said \"Hello\"")


