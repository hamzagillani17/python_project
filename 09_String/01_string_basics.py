'''String is a class that represents a string of characters.
It provides various methods for manipulating and working with strings.
The String class is immutable, meaning that once a String object is created, it cannot be changed.
Any operation that modifies a string will return a new String object.

Definition of the String class and its methods can be found in the string.py file.
there are many methods available in the String class, including methods for concatenation, slicing,
searching, and formatting strings.

'''

# =====================================================
# Concept 1: What is a String?
# =====================================================
"""
Definition:
A string is a sequence of characters (letters, numbers, symbols)
enclosed in quotes. It is Python's data type used to store text.
"""

def concept1_program1():
    '''Create a simple string and check its type'''
    name = "Automation"
    print("Value:", name)

def concept1_program2():
    '''Store different kinds of text in string'''
    word = "Python"
    sentence =  "Testing is important"
    symbol_text = "@#$%"
    print(word, "|", sentence, "|", symbol_text)

def concept1_program3():
    '''program that string is a class/object in python'''
    text = "Hello"
    print(isinstance(text, str))    # True - confirms it's a string object

# =====================================================
# Concept 2: Why Strings Are Needed
# =====================================================

'''Definition:
Strings are needed because every program deals with text data -
names, messages, error texts, file paths, user input, etc.
Without strings, text data cannot be stored or processed.'''   

def concept2_prohram1():
    """Store an error message like in real automation testing"""
    error_message = "Login Faild: Invalid Credentials"
    print(error_message)

def concept2_program2():
    """Store multiple pieces of text data together"""
    username = "test_user"
    password = "Test@123"
    print("Username:", username, "| Password:", password)


# =====================================================
# Concept 3: String vs Character
# =====================================================
"""
Definition:
Python does not have a separate "character" data type like C/Java.
A single character is also treated as a string, just with length 1.
"""

def concept3_program1():
    """Compare type of single character and full word"""
    character = "A"
    word = "Apple"
    print("Character type:", type(character))
    print("Word type:", type(word))
    print("Both are the SAME type: ", type(character) == type(word))

def concept3_program2():
    """Show length difference between character and word"""
    character = "A"
    word = "Apple"
    print("Length of character:", len(character))
    print("Length of word:", len(word))


# =====================================================
# Concept 4: String Literals
# =====================================================
"""
Definition:
A string literal is the actual text written directly inside quotes
(hardcoded text), as opposed to text coming from a variable.
"""
def concept4_program1():
#Use string literals directly inside print
    print("This is a string literal")
    print("This is also a string literal")

def concept4_program2():
    """Store a literal inside a variable"""
    greeting = "Hello"   # "Hello" is the literal, greeting is the variable
    print(greeting)

# =====================================================
# Concept 5: Single Quotes '...'
# =====================================================
"""
Definition:
Strings can be created using single quotes.
Problem: if text contains an apostrophe, single quotes cause an error.
"""
def concept5_program1():
    """Create a string using single quotes"""
    city = 'Lahore'
    print(city)

def concept5_program2():
    """Show why single quotes fail with apostrophe text"""
    # text = 'It's a book'   # This line would cause a SyntaxError
    text = 'It is a book'    # Safe version without apostrophe
    print(text)

# =====================================================
# Concept 6: Double Quotes "..."
# =====================================================
"""
Definition:
Strings can also be created using double quotes.
There is no functional difference from single quotes,
except double quotes can safely contain an apostrophe.
"""

def concept6_program1():
    """Create a string using double quotes"""
    city = "Lahore"
    print(city)

def concept6_program2():
    text = "It's a beautiful day"
    print(text)

def concept6_program3():
    text = 'She said "Hello" to me'
    print(text)


# =====================================================
# Concept 7: Triple Quotes '''...''' / \"\"\"...\"\"\"
# =====================================================
"""
Definition:
Triple quotes are used to create multi-line strings.
They also allow both single and double quotes inside safely.
"""

def concept7_program1():
    """Create a multi-line string using triple quotes"""
    paragraph =  """This is a line one.
    This is line 2
    this is line 3"""
    print(paragraph)

def concept7_program2():
    """Use triple quotes to include both quote types safely"""
    text = """She said "It's a nice day" today."""
    print(text)    

def concept7_program3():
    """Use triple quoates as a docstring inside a function"""
    def add(a, b):
        """This function adds two number"""
        return a + b
    print(add(5, 10))
    print(add.__doc__) #prints the docstring

# =====================================================
# Concept 8: Empty String
# =====================================================
"""
Definition:
An empty string contains no characters at all, just empty quotes.
It is still a valid string object, only its length is zero.
"""

def concept8_program1():
    """Create an empty string and check its length and type"""
    empty = ""
    print("Lenght , len(empty)")
    print("Type", type(empty))

def concept8_program2():
    """Build a string gradually from an empty string using a loop"""
    result = ""
    for i in range(5):
        result += str(i)
        print("After step", i, "->", result)

# =====================================================
# Concept 9: String with Spaces
# =====================================================
"""
Definition:
Spaces are valid characters inside a string and are counted
by Python like any other character.
"""

def concept9_program1():
    """Check length of a string that contains spaces"""
    text = "Hello World"
    print("Length:", len(text))   # includes the space

def concept9_program2():
    """Compare a string of only spaces with an empty string"""
    just_space = "  "
    empty = ""
    print("Length of space string:", len(just_space))
    print("Is spaces string equal to empty string:", just_space == empty)

# =====================================================
# Concept 10: Numbers and Symbols Inside a String
# =====================================================
"""
Definition:
Numbers and symbols placed inside quotes become part of a string,
not actual numeric or symbolic data types.
"""

def concept10_program1():
    """Show that a number inside quotes is a string, not an int"""
    num_as_string = "123"
    actual_num = 123
    print("Type of '123':",type(num_as_string))
    print("Type of 123:", type(actual_num))

def concept10_program2():
    """Show the difference between string concatenation and math addition"""
    num_as_string = "123"
    actual_num = 123
    print("String + String:", num_as_string + num_as_string)   # joins text
    print("Number + Number:", actual_num + actual_num)
    print("number + string using Int()",actual_num + int(num_as_string))

def concept10_program3():
    """Store symbols inside a string without any error"""
    special = "Price: $50 @Shop #Sale!"
    print(special)         

# =====================================================
# Concept 11: Why Strings Are Immutable
# =====================================================
"""
Definition:
Immutable means once a string is created, its existing characters
cannot be changed directly. Any "change" actually creates a brand
new string object; the original stays untouched.
"""

def concept11_program1():
    """Try to change a character directly and catch the resulting error"""
    name = "Ali"
    try:
        name[0] = "M"  #This will raise an error
    except TypeError as e:
        print("Error occurred:", e)    

def concept11_program2():
    """Show the correct way to 'change' a string by building a new one"""
    name = "Ali"
    name = "M" + name[1:]     # creates a new string, does not modify old one
    print(name)        

def concept11_program3():
    """Prove immutability using id() before and after modification"""
    name = "Ali"
    print("ID before:", id(name))

    name = name + " Khan"      # this creates a NEW string object
    print("ID after:", id(name))
    print("Different id means a new object was created, not modified")


# =====================================================
# Run All Programs (for testing one by one)
# =====================================================
if __name__ == "__main__":
    print("\n--- Concept 1 ---")
    concept1_program1()
    concept1_program2()
    concept1_program3()

    print("\n--- Concept 2 ---")
    concept1_program1()
    concept2_program2()

    print("\n--- Concept 3 ---")
    concept3_program1()
    concept3_program2()

    print("\n--- Concept 4 ---")
    concept4_program1()
    concept4_program2()

    print("\n--- Concept 6 ---")

    concept6_program1()
    concept6_program2()
    concept6_program3()

    print("\n--- Concept 7 ---")
    concept7_program1()
    concept7_program2()
    concept7_program3()

    print("\n--- Concept 8 ---")
    concept8_program1()
    concept8_program2()

    print("\n--- Concept 9 ---")
    concept9_program1()
    concept9_program2()

    print("\n--- Concept 10 ---")
    concept10_program1()
    concept10_program2()
    #concept10_program3()

    print("\n--- Concept 11 ---")
    concept11_program1()
    concept11_program2()
    concept11_program3()

