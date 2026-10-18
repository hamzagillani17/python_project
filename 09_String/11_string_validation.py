# =====================================================
# Concept 1: What is String Validation?
# =====================================================
"""
Definition:
Validation means checking whether a string has the format you
expect before you use it (for example: "is this age only digits?").
Python gives many is...() methods for this. They all return a bool
(True or False), so they fit naturally inside if conditions.
"""
# Program 1: A validation method returns True or False
print("Hello".isalpha())                # True

# Program 2: The result type is bool
result = "123".isdigit()
print(result, type(result))             # True <class 'bool'>

# Program 3: Use the result inside an if statement
if "abc".isalpha():
    print("Only letters")

# =====================================================
# Concept 2: isalpha()
# =====================================================
"""
Definition:
isalpha() returns True if the string is not empty and EVERY character
is a letter. Digits, spaces and symbols make it False.
It also works for letters of other languages such as Urdu.
"""
# Program 1: Letters only vs letters mixed with other characters
print("Hello".isalpha())                # True
print("Hello123".isalpha())             # False (digits)
print("Hello World".isalpha())          # False (space)

# Program 2: Urdu letters are letters too
print("علی".isalpha())                  # True

# Program 3: Count the letters in a string using a loop
count = 0
for ch in "a1b2c3":
    if ch.isalpha():
        count += 1
print("Letters:", count)                # 3

# Program 2: Validate an age before converting it
age = input("Enter your age: ")
if age.isdigit():
    print("Age next year:", int(age) + 1)
else:
    print("Please enter numbers only")

# Program 3: Pull only the digits out of a string
code = "Order-4821-X"
digits = ""
for ch in code:
    if ch.isdigit():
        digits += ch
print(digits)                           # 4821


# =====================================================
# Concept 4: isdecimal()
# =====================================================
"""
Definition:
isdecimal() returns True only when every character is a decimal digit
(a digit that can build a normal base-10 number). It is stricter than
isdigit(): special digits such as superscripts are rejected.
Digits of other scripts (for example Arabic-Indic) count as decimal.
"""

# Program 1: Normal digits
print("123".isdecimal())                # True
print("12.3".isdecimal())               # False

# Program 2: A superscript is a digit but NOT decimal
print("²".isdigit())                    # True
print("²".isdecimal())                  # False

# Program 3: Digits from another script are decimal and int() understands them
print("٣".isdecimal())                  # True
print(int("٣"))                         # 3


# =====================================================
# Concept 5: isnumeric()
# =====================================================
"""
Definition:
isnumeric() is the most permissive of the three. It is True for
digits, superscripts, fractions and numeral characters of other
languages. Being numeric does not mean int() can convert it.
"""

# Program 1: Different kinds of numeric characters
print("123".isnumeric())                # True
print("²".isnumeric())                  # True (superscript)
print("½".isnumeric())                  # True (fraction)
print("五".isnumeric())                 # True (Chinese numeral five)

# Program 2: Numeric text that int() cannot convert
try:
    print(int("½"))
except ValueError as e:
    print("Error:", e)

# Program 3: A normal number with a decimal point is not numeric
print("12.5".isnumeric())               # False

# =====================================================
# Concept 6: isdecimal() vs isdigit() vs isnumeric()
# =====================================================
"""
Definition:
Every decimal text is also digit text, and every digit text is also
numeric text, but not the other way round:
isdecimal  <  isdigit  <  isnumeric   (strict -> loose)
For everyday validation of normal numbers, isdecimal() or isdigit()
is enough.
"""


# Program 1: Compare all three on the same samples
samples = ["123", "²", "½", "五", "12.5", "-7"]
print(f"{'text':<6}{'decimal':<9}{'digit':<8}{'numeric':<8}")
for s in samples:
    print(f"{s:<6}{str(s.isdecimal()):<9}{str(s.isdigit()):<8}{str(s.isnumeric()):<8}")

# Program 2: Safe check before int() using isdecimal()
text = "2026"
if text.isdecimal():
    print(int(text) + 1)                # 2027

# Program 3: Accept only plain English digits 0-9
for text in ["123", "٣"]:
    if text.isdecimal() and text.isascii():
        print(text, "-> plain digits")
    else:
        print(text, "-> not plain 0-9 digits")


# =====================================================
# Concept 7: isalnum()
# =====================================================
"""
Definition:
isalnum() returns True if the string is not empty and EVERY character
is a letter or a digit (alphabet + numeric). Spaces, underscores and
symbols make it False.
"""

# Program 1: Letters and digits only
print("Hello123".isalnum())             # True
print("Hello 123".isalnum())            # False (space)
print("Hello@123".isalnum())            # False (symbol)

# Program 2: Underscore is NOT alphanumeric
print("user_123".isalnum())             # False

# Program 3: Simple username check
username = input("Enter username: ")
if username.isalnum():
    print("Username accepted")
else:
    print("Only letters and digits are allowed")


# =====================================================
# Concept 8: isspace()
# =====================================================
r"""
Definition:
isspace() returns True if the string is not empty and contains ONLY
whitespace characters (space, tab \t, new line \n and similar).
"""

# Program 1: Whitespace-only strings
print("   ".isspace())                  # True
print("\t\n".isspace())                 # True
print("Hello".isspace())               # False
print(" a ".isspace())                 # False

# Program 2: An empty string is NOT whitespace
print("".isspace())                    # False

# Program 3: Skip blank lines in a list
lines = ["data", "   ", "", "more data"]
for line in lines:
    if line == "" or line.isspace():
        print("(blank line skipped)")
    else:
        print(line)


# =====================================================
# Concept 9: islower()
# =====================================================
"""
Definition:
islower() returns True if the string has at least one letter that can
have a case, and ALL such letters are lowercase. Digits and symbols
are ignored.
"""

# Program 1: Lowercase checks
print("hello".islower())                # True
print("Hello".islower())                # False

# Program 2: Digits and symbols are ignored
print("hello 123!".islower())           # True

# Program 3: No letters at all gives False
print("123".islower())                  # False


# =====================================================
# Concept 10: isupper()
# =====================================================
"""
Definition:
isupper() returns True if the string has at least one letter that can
have a case, and ALL such letters are uppercase.
"""

# Program 1: Uppercase checks
print("HELLO".isupper())               # True
print("Hello".isupper())               # False

# Program 2: Digits and symbols are ignored
print("HELLO 123!".isupper())          # True

# Program 3: Check a status text that must be written in capitals
status = "PASSED"
if status.isupper():
    print("Status format is correct")


# =====================================================
# Concept 11: istitle()
# =====================================================
"""
Definition:
istitle() returns True if the string is in title case: every word
starts with a capital letter and the rest of that word is lowercase.
"""

# Program 1: Title case checks
print("Python Programming".istitle())   # True
print("python programming".istitle())   # False
print("PYTHON Programming".istitle())   # False

# Program 2: Digits do not break title case
print("Hello World 123".istitle())      # True

# Program 3: An apostrophe splits words, same behaviour as title()
print("It's A Test".istitle())          # False
print("It'S A Test".istitle())          # True


# =====================================================
# Concept 12: isascii()
# =====================================================
"""
Definition:
isascii() returns True if every character is a plain ASCII character
(code 0 to 127: English letters, digits and common symbols).
Accented letters, Urdu letters and emojis make it False.
(Python 3.7 or newer)
"""

# Program 1: English text vs accented text
print("Hello123".isascii())            # True
print("Héllo".isascii())               # False

# Program 2: Urdu text and emoji
print("سلام".isascii())                # False
print("OK 😀".isascii())               # False

# Program 3: Find the non-ASCII characters in a string
text = "Café ✅ Test"
for ch in text:
    if not ch.isascii():
        print("Non-ASCII:", ch, ord(ch))


# =====================================================
# Concept 13: isidentifier() and isprintable() (Bonus)
# =====================================================
r"""
Definition:
isidentifier() is True if the string could be used as a variable name
(letters, digits and underscore, not starting with a digit).
It does not check Python keywords. Use keyword.iskeyword() for that.
isprintable() is True if there are no hidden control characters such
as new line (\n) or tab (\t).
"""

# Program 1: Valid and invalid variable names
print("my_var".isidentifier())          # True
print("2var".isidentifier())            # False (starts with a digit)
print("my var".isidentifier())          # False (space)

# Program 2: A keyword has a valid identifier shape but cannot be a name
import keyword
print("class".isidentifier())           # True
print(keyword.iskeyword("class"))       # True

# Program 3: Detect hidden characters with isprintable()
print("Hello".isprintable())            # True
print("Hello\n".isprintable())          # False
print("Hello\t".isprintable())          # False


# =====================================================
# Concept 14: Empty String Behaviour
# =====================================================
"""
Definition:
Most is...() methods return False for an empty string because they
need at least one character. The exceptions are isascii() and
isprintable(), which return True for an empty string.
Always check for an empty input first.
"""

# Program 1: Results for an empty string
print("".isalpha(), "".isdigit(), "".isalnum(), "".isspace())   # False False False False
print("".islower(), "".isupper(), "".istitle())                 # False False False
print("".isascii(), "".isprintable())                           # True True

# Program 2: A user who presses Enter without typing anything
name = input("Enter your name: ")
if not name.isalpha():
    print("Invalid name (empty or contains non-letters)")

# Program 3: Give a better message by checking empty input first
name = input("Enter your name again: ")
if name == "":
    print("Name cannot be empty")
elif not name.isalpha():
    print("Name must contain letters only")
else:
    print("Name accepted:", name)


# =====================================================
# Concept 15: Validating Numbers Typed by the User
# =====================================================
"""
Definition:
isdigit() cannot recognise negative numbers or decimals, because the
minus sign and the dot are not digits. To validate them you need a
few extra steps, or the simple try/except around float() (a small
preview of error handling).
"""

# Program 1: The problem
print("-5".isdigit(), "12.5".isdigit())   # False False

# Program 2: Accept an optional minus sign for integers
for text in ["42", "-42", "4-2", "-"]:
    body = text[1:] if text.startswith("-") else text
    if body.isdigit():
        print(text, "-> valid integer")
    else:
        print(text, "-> not a valid integer")

# Program 3: Accept decimals by checking both sides of the dot
for text in ["12.5", "12.", "abc", "3.14.15"]:
    parts = text.split(".")
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        print(text, "-> valid decimal")
    else:
        print(text, "-> not a valid decimal")

# Program 4: The simplest way, try float() and catch the error
for text in ["12.5", "abc", "-3", "1e3"]:
    try:
        number = float(text)
        print(text, "-> valid number:", number)
    except ValueError:
        print(text, "-> not a number")


# =====================================================
# Concept 16: Validation with Conditions (Username and Password)
# =====================================================
"""
Definition:
Real validation combines several checks with and / or / not and
loops. Check the cheap and most important rules first, and report
which rule failed.
"""

# Program 1: Username rules: 4 to 12 characters, letters/digits only, starts with a letter
usernames = ["ali123", "12ali", "ab", "ali_khan", "verylongusername123"]
for u in usernames:
    if len(u) < 4 or len(u) > 12:
        print(u, "-> invalid: length must be 4 to 12")
    elif not u.isalnum():
        print(u, "-> invalid: letters and digits only")
    elif not u[0].isalpha():
        print(u, "-> invalid: must start with a letter")
    else:
        print(u, "-> valid")

# Program 2: Password strength check using flags in a loop
passwords = ["Test@123", "weakpass", "SHORT1!"]
for pw in passwords:
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for ch in pw:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum() and not ch.isspace():
            has_symbol = True
    missing = []
    if len(pw) < 8:
        missing.append("8+ characters")
    if not has_upper:
        missing.append("uppercase")
    if not has_lower:
        missing.append("lowercase")
    if not has_digit:
        missing.append("digit")
    if not has_symbol:
        missing.append("symbol")
    if missing:
        print(pw, "-> weak, missing:", ", ".join(missing))
    else:
        print(pw, "-> strong")

# Program 3: Full name may contain letters and spaces only
names = ["Ali Khan", "Ali123", "   ", "Sara"]
for n in names:
    if n.strip() != "" and n.replace(" ", "").isalpha():
        print(repr(n), "-> valid name")
    else:
        print(repr(n), "-> invalid name")


# =====================================================
# Concept 17: Validation in SQA Automation
# =====================================================
"""
Definition:
In test automation, validation methods check test data and texts
read from a web page, a file or an API before they are compared or used.
"""

# Program 1: Validate test case IDs of the format TC_LOGIN_001
test_ids = ["TC_LOGIN_001", "tc_login_001", "TC_LOGIN_1", "TC_LOG1N_002"]
for tid in test_ids:
    parts = tid.split("_")
    valid = (
        len(parts) == 3
        and parts[0] == "TC"
        and parts[1].isalpha() and parts[1].isupper()
        and parts[2].isdigit() and len(parts[2]) == 3
    )
    print(tid, "->", "valid" if valid else "invalid")

# Program 2: Basic email check without regex
emails = ["ali@example.com", "ali@@example.com", "ali@example",
          "@example.com", "ali @example.com", "ali@.com"]
for email in emails:
    local, sep, domain = email.partition("@")
    valid = (
        email.count("@") == 1
        and " " not in email
        and local != ""
        and "." in domain
        and not domain.startswith(".")
        and not domain.endswith(".")
        and domain.rpartition(".")[2].isalpha()
        and len(domain.rpartition(".")[2]) >= 2
    )
    print(email, "->", "valid" if valid else "invalid")

# Program 4: Clean and validate a status text read from a web page
valid_statuses = ("PASS", "FAIL", "SKIP")
raw_status = "  pass\xa0"                 # \xa0 is a hidden non-breaking space
cleaned = raw_status.strip().upper()
print(repr(raw_status), "->", repr(cleaned))
if cleaned.isalpha() and cleaned in valid_statuses:
    print("Status is valid:", cleaned)

# Program 5: Convert a price text from a page into a number safely
price_text = "$1,234.50"
cleaned = price_text.replace("$", "").replace(",", "")
parts = cleaned.split(".")
if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
    print("Price as number:", float(cleaned))       # 1234.5
else:
    print("Price text is not valid:", price_text)
































































