"""
====================================================
09_Strings / 03_string_slicing.py
====================================================
Topic: String Slicing
====================================================
"""

# =====================================================
# Concept 1: Basic Slicing [start:stop]
# =====================================================
"""
Definition:
Slicing extracts a portion (substring) of a string using the
syntax string[start:stop].
Rule: 'start' is INCLUDED, 'stop' is EXCLUDED.
"""

# Program 1: Slice characters from index 1 up to (not including) 4
word = "python"
print(word[1:4])    #yth

# Program 2: Slice the first three characters
word = "Automation"
print(word[0:3]) #Aut

# Program 3: Slice a middle part of a sentence
sentence = "Software Testing"
print(word[9:16])

# =====================================================
# Concept 2: Start Omitted [:stop]
# =====================================================
"""
Definition:
If 'start' is not written, Python begins from index 0
(the very beginning of the string).
"""

# Program 1: Get the first four characters
word = "Python"
print(word[:4])

# Program 2: Prove that [:4] is the same as [0:4]
print(word[:4] == word[0:4])    #True


# Program 3: Get the first word of a sentence when its length is known
sentence = "Hello World"
print(sentence[:5])     # Hello

# =====================================================
# Concept 3: Stop Omitted [start:]
# =====================================================
"""
Definition:
If 'stop' is not written, Python continues until the very end
of the string.
"""

# Program 1: Get everything from index 2 onwards
word = "Python"
print(word[2:])         # thon

# Program 2: Get the last word of a sentence when its position is known
sentence = "Hello World"
print(sentence[6:])     # World

# Program 3: Omit both start and stop to get the full string
word = "Python"
print(word[:])          # Python

# =====================================================
# Concept 4: Negative Slicing
# =====================================================
"""
Definition:
Negative indices can also be used in slicing. They count from the
right side of the string, where -1 is the last character.
"""

# Program 1: Slice using negative start and negative stop
word = "Python"
print(word[-4:-1])      # tho   (-1 is excluded)

# Program 2: Get the last three characters
print(word[-3:])        # hon

# Program 3: Remove a file extension by excluding the last 4 characters
filename = "document.txt"
print(filename[:-4])    # document

# =====================================================
# Concept 5: Step [start:stop:step]
# =====================================================
"""
Definition:
The third number is the 'step'. It tells Python how many positions
to jump forward after each character. The default step is 1.
"""
# Program 1: Take every second character from index 0 to 5
word = "Python"
print(word[0:6:2])      # Pto

# Program 2: Omit start and stop but keep the step
print(word[::2])        # Pto

# Program 3: Take every third character from a longer string
text = "ABCDEFGHI"
print(text[::3])        # ADG

# =====================================================
# Concept 6: Reverse String
# =====================================================
"""
Definition:
Using a step of -1 makes Python move from the end to the start,
which reverses the whole string: string[::-1].
"""

# Program 1: Reverse a simple word
word = "Python"
print(word[::-1])       # nohtyP

# Program 2: Check whether a word is a palindrome
word = "madam"
if word == word[::-1]:
    print(word, "is a palindrome")
else:
    print(word, "is not a palindrome")

# Program 3: Reverse a user-entered word
user_word = input("Enter a word: ")
print("Reversed:", user_word[::-1])

# =====================================================
# Concept 7: Copying a String Using Slicing
# =====================================================
"""
Definition:
Slicing with [:] gives a full copy of the string.
Because strings are immutable, Python reuses the same object,
so this matters much more for lists (mutable) than for strings.
"""

# Program 1: Copy a string using [:]
original = "Python"
copy_str = original[:]
print(copy_str)
print(copy_str == original)     # True

# Program 2: Check the ids of the original and the copy
print(id(original) == id(copy_str))     # True - same object is reused

# Program 3: Compare with a list, where [:] really creates a new object
original_list = [1, 2, 3]
copy_list = original_list[:]
print(id(original_list) == id(copy_list))   # False - new list object


# =====================================================
# Concept 8: Common Slicing Mistakes
# =====================================================
"""
Definition:
These are the mistakes beginners make most often with slicing:
1) Thinking 'stop' is included
2) Expecting an error for out-of-range slices (there is none)
3) Using start > stop without a negative step
"""

# Program 1: Mistake 1 - 'stop' is excluded, so word[0:3] gives 3 characters
word = "Python"
print(word[0:3])        # Pyt (not Pyth)

# Program 2: Mistake 2 - slicing never raises IndexError, indexing does
print(word[2:100])      # thon (no error)
print(word[10:20])      # empty string (no error)
try:
    print(word[10])     # this one raises an error
except IndexError as e:
    print("Indexing error:", e)

# Program 3: Mistake 3 - start > stop with a positive step gives empty string
print("[" + word[4:1] + "]")       # [] (empty)
print(word[4:1:-1])                # oht (fixed with a negative step)

























































