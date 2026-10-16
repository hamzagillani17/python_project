r"""
====================================================
09_Strings / 05_escape_sequences.py
====================================================
Topic: Escape Sequences
====================================================
"""

# =====================================================
# Concept 1: \n (New Line)
# =====================================================
r"""
Definition:
\n moves the cursor to the next line.
It is stored inside the string as ONE character (a new line).
"""
# Program 1: Print three lines using one print statement
print("LINE 1\nLine 2\nLine 3")

# Program 2: Two \n in a row create an empty line
print("Hallo\n\nWorld")

# Program 3: Prove that \n is only one character
text = "A\nB"
print(text)
print(len(text))    # 3 (A, new line, B)
print(repr(text))    # 'A\nB' (repr shows the escape sequence instead of using it)

# =====================================================
# Concept 2: \t (Tab)
# =====================================================
r"""
Definition:
\t inserts a horizontal tab (a wide gap, usually 4 to 8 spaces).
It is useful for aligning simple output in columns.
"""

# Program 1: Align a label and a value
print("Name:\tAli")
print("Age:\t22")

# Program 2: Separate three words with tabs
print("A\tB\t\tC")

# Program 3: Print a small table using tabs and new lines
print("Item\tprice\nPen\t10\nBook\t50")

# =====================================================
# Concept 3: \\ (Backslash)
# =====================================================
r"""
Definition:
A single backslash starts an escape sequence, so to print an actual
backslash character you must write it twice: \\
"""
# Program 1: Print a Windows folder path
print("D:\\projects\\pyton_code")

# Program 2: Print a single backslash
print("This is a backslash: \\")

# Program 3: Prove that \\ is only one character
print(len("\\"))    #1

# =====================================================
# Concept 4: \' (Single Quote)
# =====================================================
r"""
Definition:
\' puts a single quote (apostrophe) inside a string that is
written with single quotes.
"""

# Program 1: Apostrophe inside a single-quoted string

text = 'It\'s a Sunny day'
print(text)

# Program 2: Use it inside a longer sentence
print("It's a sunny day")
print(text)

# =====================================================
# Concept 5: \" (Double Quote)
# =====================================================
r"""
Definition:
\" puts a double quote inside a string that is written
with double quotes.
"""

# Program 1: Quote inside a double-quoted string
print("He said \"Good morning\" to everyone")

# Program 2: Show a test message with a quoted value
print("Expected title: \"Login page\"")

# Program 3: The same text with single quotes outside needs no escape
print('He said "Good morning" to everyone')

# =====================================================
# Concept 6: \r (Carriage Return)
# =====================================================
r"""
Definition:
\r moves the cursor back to the START of the current line (it does
not start a new line). Text printed after it overwrites the old text.
Note: this is best seen in a real terminal. Some IDE output windows
show it differently.
"""
import time
# Program 1: Overwrite the beginning of a line
print("Hello World\rPython")    #python World

# Program 2: A countdown on a single line
for i in range(5, 0 , -1):
    print("\rCountdown:",i, end="", flush=True)
    time.sleep(1)
print("\rDone!            ")    

# Program 3: A simple loading percentage on one line
for percent in range(0, 101, 25):
    print("\rLoading... " + str(percent) +"%", end="", flush=True)
    time.sleep(0.5)
print()       # move to the next line when finished

# =====================================================
# Concept 7: \b (Backspace)
# =====================================================
r"""
Definition:
\b moves the cursor ONE position to the left. The next character
printed overwrites the character that was there.
Note: it does not delete anything by itself. Some IDE consoles show
\b as a special symbol instead of moving the cursor, so test it in
a real terminal.
"""

# Program 1: The next character overwrites the previous one
print("ABC\bD") # ABD (D overwrites C)

# Program 2: Fix a typo with backspace
print("pythonn\bx") # Python + x overwrites the last n -> Pythonx

# Program 3: Prove that \b is only one character
print(len("\b"))

# =====================================================
# Concept 8: Raw Strings r"..."
# =====================================================
r"""
Definition:
A raw string has the letter r before the opening quote.
Python does NOT process escape sequences inside it, so every
backslash stays exactly as written. Very useful for file paths
and regular expressions.
"""

# Program 1: Normal string vs raw string for a file path
normal_path = "C:\newfolder\test"      # \n and \t are treated as escape characters
raw_path = r"C:\newfolder\test"        # printed exactly as written

print(normal_path)    # 1 (one new line character)
print(raw_path)  # 2 (a backslash and the letter n)

# Program 3: A raw string used as a regex-style pattern
pattern = r"\d+\s\w+"
print(pattern)                         # \d+\s\w+

# Note: a raw string cannot end with a single backslash
# path = r"C:\folder\"   # This would cause a SyntaxError


# =====================================================
# Concept 9: Combining Escape Sequences (Bonus)
# =====================================================
r"""
Definition:
Several escape sequences can be mixed inside one string to build
formatted output such as receipts and reports.
"""

# Program 1: A small receipt using \n and \t
print("Item\tPrice\nPen\t10\nBook\t50")

# Program 2: Quotes, a backslash and a new line in one string
print("File: \"C:\\data\\report.txt\"\nStatus:\tFound")

# Program 3: A formatted test report
print("=" * 25 + "\nTest Report\n" + "=" * 25 + "\nLogin\t\tPassed\nCheckout\tFailed")