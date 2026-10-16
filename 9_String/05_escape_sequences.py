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

































