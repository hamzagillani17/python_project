"""
====================================================
09_Strings / 02_string_indexing.py
====================================================
Topic: Creating & Accessing Strings
====================================================
"""
# =====================================================
# Concept 1: String Creation
# =====================================================

"""
Definition:
Strings can be created directly using quotes, or by converting
another data type into a string using the str() function.
"""

# Program 1: Create a string directly using quotes

name = "Ali"
city = "Frankfurt"

print(name,city)

# Program 2: Create a string using str() from a number

num = 25
string_num = str(num)
print(string_num,type(string_num))

# Program 3: Use str() to join text and a number safely
num = 32

age = "ich bin " + str(num) + " jahre alt"
print(age) 

# =====================================================
# Concept 2: Indexing
# =====================================================
"""
Definition:
Indexing means accessing a single character of a string using its
position number written inside square brackets [].
"""
# Program 1: Access first character using index
word = "Python"
print(word[0])
# Program 2: Access a middle character
print(word[3])
# Program 3: Access character using a variable as index
position = 2 
print(word[position])

# =====================================================
# Concept 3: Positive Indexing
# =====================================================
"""
Definition:
Positive indexing counts characters from left to right, starting at 0.
"""

# Program 1: Print each character using positive index
word = "Python"
print(word[0],word[1],word[2],word[3],word[4],word[5])

# Program 2: Print character at a calculated positive index
word = "Automation"
print(word[5])

# Program 3: Loop through positive indices manually
word = "python"
for i in range(len(word)):
    print("index",i, "->", word[i])

# =====================================================
# Concept 4: Negative Indexing
# =====================================================
"""
Definition:
Negative indexing counts characters from right to left, starting at -1.
It is useful when you need the last character without knowing the length.
"""

# Program 1: Access last character using negative index
word = "Python"
print(word[-1])
print(word[-2])

# Program 3: Compare negative indexing on short and long strings
short_word = "Hi"
long_word = "Automation"
print("Last char of short word:",short_word[-1])
print("Last char of long word:",long_word[-1])

# =====================================================
# Concept 5: len()
# =====================================================
"""
Definition:
len() is a built-in function that returns the total number of
characters in a string, including spaces.
"""

# Program 1: Get length of a simple word
word = "Python"
print(len(word))

# Program 2: Get length of a sentence with spaces
sentence = "Hello World"
print(len(sentence))

# Program 3: Use len() to find the last valid positive index
word = "Python"
print(word[len(word)-1])

# =====================================================
# Concept 6: First / Last Character
# =====================================================
"""
Definition:
The first character is accessed using index 0, and the last character
is best accessed using index -1 (no need to calculate length).
"""

# Program 1: Get first and last character of a word
word = "Python"
print("First:", word[0])
print("Last:", word[-1])

# Program 2: Get first and last character from user input
user_word = input("Enter a word: ")
print("First:", user_word[0])
print("Last:", user_word[-1])


# Program 3: Compare [-1] with len()-1 method (both give same result)
word = "Testing"
print(word[-1] == word[len(word) - 1])

# =====================================================
# Concept 7: Index Out of Range
# =====================================================
"""
Definition:
Accessing an index that does not exist in the string causes an
IndexError. Valid positive indices only go from 0 to length-1.
"""

# Program 1: Trigger and catch an out of range error
word = "Python"

#print(word[10]) #error IndexError: string index out of range 
try:
    print(word[10])
except IndexError as e:
    print("Error", e)    

# Program 2: Show the common off-by-one mistake
word = "Python" # length is 6, valid indices are 0 to 5
try:
   print(word[len(word)]) # this is out of range
except IndexError as e:
    print("Error",e)


# Program 3: Show the correct way using len(word) - 1
word = "Python"
print(word[len(word) - 1])     # this is valid

# =====================================================
# Concept 8: String Iteration with for
# =====================================================
"""
Definition:
A for loop can go through a string character by character,
either directly or using index numbers via range(len()).
"""

# Program 1: Print each character directly using for loop
word = "Python"
for i in word:
    print(i)

# Program 2: Print each character along with its index using range(len())
word = "Python"
for i in range(len(word)):
    print("Index", i, "-> Character:", word[i])

# Program 3: Print only the vowels from a string using a for loop
word = "Automation"
for char in word:
    if char in "aeiou":
        print(char)





        

