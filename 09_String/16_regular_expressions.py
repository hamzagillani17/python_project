r"""
====================================================
09_Strings / 16_regular_expressions.py
====================================================
Topic: Regular Expressions (the re module)
====================================================
Notes before you run this file:
1) ALWAYS write patterns as raw strings: r"..."
   (in a normal string, "\b" is a backspace and "\d" gives a warning).
2) Most programs print True/False with bool(...), because printing a
   Match object shows <re.Match object; ...> which is hard to read.
3) A regex pattern is a small language inside a string. Read it
   slowly, one piece at a time. Programs marked "limitation" show where
   a simple pattern is NOT enough.
"""

import re


# =====================================================
# Concept 1: What is a Regular Expression?
# =====================================================
r"""
Definition:
A regular expression (regex) is a PATTERN that describes the shape of
text, for example "4 digits, a dash, 7 digits". The re module searches,
checks, extracts and replaces text using such patterns.
Normal string methods (find, replace, in) look for EXACT text.
Regex looks for a SHAPE of text.
"""

# Program 1: A first search
match = re.search(r"\d+", "Order 123")
print(match)                            # <re.Match object; span=(6, 9), match='123'>
print(match.group())                    # 123

# Program 2: Exact text (str method) vs a shape (regex)
text = "Call 0300 or 0321"
print("0300" in text)                   # True  (you must know the exact number)
print(re.findall(r"\d{4}", text))       # ['0300', '0321'] (any 4 digits)

# Program 3: Why raw strings are needed
print(len("\b"), len(r"\b"))            # 1 2  (backspace vs backslash + b)
print("\\d" == r"\d")                   # True (both are backslash + d)
print(re.findall("\bcat\b", "cat"))     # []   (\b became a backspace, wrong)
print(re.findall(r"\bcat\b", "cat"))    # ['cat']

# Program 4: The type of a compiled pattern
print(type(re.compile(r"a")))           # <class 're.Pattern'>


# =====================================================
# Concept 2: Pattern (Literal Characters and Metacharacters)
# =====================================================
r"""
Definition:
In a pattern, most characters match themselves (literals): "cat"
matches the text "cat".
Special characters (metacharacters) have a special meaning:
        .  ^  $  *  +  ?  {  }  [  ]  \  |  (  )
To match one of them literally, put a backslash before it (\.) or use
re.escape().
"""

# Program 1: Literal characters
match = re.search(r"cat", "concatenate")
print(match.group(), match.span())      # cat (3, 6)

# Program 2: A dot is a metacharacter (any character) unless escaped
print(bool(re.search(r"a.c", "abc")))   # True  (dot matches b)
print(bool(re.search(r"a\.c", "abc")))  # False (needs a real dot)
print(bool(re.search(r"a\.c", "a.c")))  # True

# Program 3: re.escape() makes ANY text safe to use inside a pattern
print(re.escape("a.b*c"))               # a\.b\*c
user_text = "price (USD)"
print(bool(re.search(re.escape(user_text), "The price (USD) is 5")))    # True

# Program 4: Characters that need a backslash
print(re.findall(r"\$\d+", "cost $50 and $7"))      # ['$50', '$7']
print(re.findall(r"\(.*?\)", "a (b) c (d)"))        # ['(b)', '(d)']


# =====================================================
# Concept 3: search()
# =====================================================
"""
Definition:
re.search(pattern, text) scans the WHOLE text and returns the FIRST
match as a Match object. If nothing matches it returns None.
Always check for None before using .group().
"""

# Program 1: Find the first number
text = "My order number is 12345"
match = re.search(r"\d+", text)
print(match.group(), match.span())      # 12345 (19, 24)

# Program 2: No match gives None
print(re.search(r"\d+", "no digits"))   # None

# Program 3: Always check before using the result
match = re.search(r"\d+", "no digits here")
if match:
    print("Found:", match.group())
else:
    print("No number found")

# Program 4: search() returns only the FIRST match
print(re.search(r"\d+", "a1 b22 c333").group())     # 1


# =====================================================
# Concept 4: match()
# =====================================================
"""
Definition:
re.match(pattern, text) tries to match ONLY at the very START of the
text. If the pattern does not start at index 0 it returns None, even
if the pattern exists later in the text. The match does NOT have to
reach the end of the text.
"""

# Program 1: Digits at the start
print(re.match(r"\d+", "123abc"))       # <re.Match object; span=(0, 3), match='123'>

# Program 2: Digits not at the start
print(re.match(r"\d+", "abc123"))       # None

# Program 3: The rest of the text is allowed
print(re.match(r"abc", "abcdef").group())       # abc

# Program 4: match() behaves like search() with ^
print(bool(re.match(r"\d+", "7 apples")) == bool(re.search(r"^\d+", "7 apples")))   # True


# =====================================================
# Concept 5: fullmatch()
# =====================================================
"""
Definition:
re.fullmatch(pattern, text) succeeds only if the WHOLE text matches
the pattern, from the first to the last character. It is the best
choice for validation ("is this input exactly an email / a code / a number?").
"""

# Program 1: Whole text must be digits
print(bool(re.fullmatch(r"\d+", "12345")))      # True
print(bool(re.fullmatch(r"\d+", "12345abc")))   # False

# Program 2: Validate a code format: two capitals + three digits
for code in ["AB123", "AB1234", "ab123"]:
    print(code, bool(re.fullmatch(r"[A-Z]{2}\d{3}", code)))     # True False False

# Program 3: A trailing new line fools $, but not fullmatch()
print(bool(re.match(r"\d+$", "123\n")))         # True  (surprise!)
print(bool(re.fullmatch(r"\d+", "123\n")))      # False (correct)


# =====================================================
# Concept 6: search() vs match() vs fullmatch()
# =====================================================
"""
Definition:
search()    -> the pattern may be ANYWHERE in the text
match()     -> the pattern must START at index 0
fullmatch() -> the pattern must cover the WHOLE text
"""

# Program 1: The same pattern with three functions
for text in ["abc123", "123", "123abc"]:
    for func in (re.search, re.match, re.fullmatch):
        print(f"{text:<8}{func.__name__:<10}{bool(func(r'\d+', text))}")

# Program 2: Pick the right function for the job
print(bool(re.search(r"ERROR", "10:00 [ERROR] failed")))    # True  (is it somewhere in the line?)
print(bool(re.match(r"\d{2}:\d{2}", "10:00 [ERROR]")))      # True  (does the line start with a time?)
print(bool(re.fullmatch(r"\d{2}:\d{2}", "10:00")))          # True  (is the whole text a time?)


# =====================================================
# Concept 7: The Match Object
# =====================================================
"""
Definition:
A Match object describes ONE successful match. Useful members:
group()/group(0) -> the whole matched text
group(n)         -> text of group number n (counting "(" from 1)
groups()         -> a tuple of all groups
groupdict()      -> a dict of NAMED groups
start(), end(), span() -> positions in the original text
All group values are STRINGS.
"""

# Program 1: Whole match and groups
text = "Name: Ali, Age: 22"
m = re.search(r"Name: (\w+), Age: (\d+)", text)
print(m.group())                        # Name: Ali, Age: 22
print(m.group(1), m.group(2))           # Ali 22
print(m.groups())                       # ('Ali', '22')
print(m.group(1, 2))                    # ('Ali', '22')

# Program 2: Positions
print(m.start(), m.end(), m.span())     # 0 18 (0, 18)
print(m.span(1), m.span(2))             # (6, 9) (16, 18)

# Program 3: Which text and pattern produced this match?
print(m.string == text)                 # True
print(m.re.pattern)                     # Name: (\w+), Age: (\d+)

# Program 4: Named groups
m = re.search(r"(?P<name>\w+) is (?P<age>\d+)", "Ali is 22")
print(m.groupdict())                    # {'name': 'Ali', 'age': '22'}
print(m["name"], m.group("age"))        # Ali 22

# Program 5: Group values are strings
age = int(m.group("age")) + 1
print(age)                              # 23


# =====================================================
# Concept 8: findall()
# =====================================================
"""
Definition:
re.findall(pattern, text) returns a LIST of ALL non-overlapping
matches. If the pattern has ONE group, the list contains that group's
text. If it has several groups, the list contains TUPLES.
No match gives an empty list [].
"""

# Program 1: All numbers
print(re.findall(r"\d+", "Numbers: 10, 25, 33, 47"))    # ['10', '25', '33', '47']

# Program 2: No match
print(re.findall(r"\d+", "no digits"))                  # []

# Program 3: Groups change what findall() returns
emails = "ali@x.com, sara@y.com"
print(re.findall(r"\w+@\w+\.com", emails))              # ['ali@x.com', 'sara@y.com']
print(re.findall(r"(\w+)@\w+\.com", emails))            # ['ali', 'sara']
print(re.findall(r"(\w+)@(\w+)\.com", emails))          # [('ali', 'x'), ('sara', 'y')]

# Program 4: Count the vowels of a text
print(len(re.findall(r"[aeiou]", "automation testing")))    # 8

# Program 5: Extract order numbers
print(re.findall(r"#(\d+)", "Order #123, Order #456, Order #789"))     # ['123', '456', '789']


# =====================================================
# Concept 9: finditer()
# =====================================================
"""
Definition:
re.finditer(pattern, text) works like findall(), but it gives one
Match object at a time (an iterator). Use it when you need POSITIONS
or groups of every match. An iterator can be used only once.
"""

# Program 1: Print every match with its position
for m in re.finditer(r"\d+", "Numbers: 10, 25, 33"):
    print(m.group(), m.span())          # 10 (9, 11)   25 (13, 15)   33 (17, 19)

# Program 2: Find the position of every word "error"
text = "ok error ok error"
print([m.start() for m in re.finditer(r"error", text)])     # [3, 12]

# Program 3: An iterator is used up after one loop
it = re.finditer(r"\d", "a1b2")
print(len(list(it)))                    # 2
print(list(it))                         # []

# Program 4: Use groups of every match
for m in re.finditer(r"(\w+)=(\d+)", "a=1 b=22 c=333"):
    print(m.group(1), "->", int(m.group(2)))


# =====================================================
# Concept 10: Character Classes
# =====================================================
r"""
Definition:
A character class matches ONE character out of a set.
  [abc]    a, b or c                 [a-z]   any lowercase letter
  [A-Z0-9] capital letter or digit   [^abc]  anything EXCEPT a, b, c
  .        any character except a new line
  \d \D    digit / non-digit         \w \W   word character (letter, digit, _) / non-word
  \s \S    whitespace / non-whitespace
For text (str) patterns, \d and \w also match non-English digits and
letters. The re.ASCII flag limits them to English only.
"""

# Program 1: A set of characters
print(re.findall(r"[aeiou]", "hello world"))            # ['e', 'o', 'o']

# Program 2: Ranges
print(re.findall(r"[a-c]", "abcdef"))                   # ['a', 'b', 'c']
print(re.findall(r"[A-Za-z]+", "Hi, I'm Ali 22"))       # ['Hi', 'I', 'm', 'Ali']

# Program 3: Negation
print(re.findall(r"[^0-9]", "a1b2"))                    # ['a', 'b']

# Program 4: The shortcuts
text = "Ali_22 ok!"
print(re.findall(r"\d", text))                          # ['2', '2']
print(re.findall(r"\w+", text))                         # ['Ali_22', 'ok']
print(re.findall(r"\s", text))                          # [' ']
print(re.findall(r"\W", text))                          # [' ', '!']

# Program 5: The dot does not match a new line
print(re.findall(r"a.c", "abc a-c a\nc"))               # ['abc', 'a-c']

# Program 6: Special characters are normal inside []
print(re.findall(r"[.*+]", "a.b*c+d"))                  # ['.', '*', '+']
print(re.findall(r"[a-]", "a-b"))                       # ['a', '-'] (a dash at the end is literal)

# Program 7: Unicode digits and letters
print(re.findall(r"\d", "12 ١٢"))                       # ['1', '2', '١', '٢']
print(re.findall(r"\d", "12 ١٢", re.ASCII))             # ['1', '2']
print(re.findall(r"\w+", "علی Ali"))                    # ['علی', 'Ali']

# Program 8: An explicit range for Urdu/Arabic letters
print(bool(re.fullmatch(r"[\u0600-\u06FF]+", "علی")))       # True
print(bool(re.fullmatch(r"[\u0600-\u06FF]+", "Ali")))       # False


# =====================================================
# Concept 11: Quantifiers
# =====================================================
"""
Definition:
A quantifier says HOW MANY times the thing before it may repeat.
  *      0 or more        +      1 or more        ?      0 or 1 (optional)
  {n}    exactly n        {n,m}  n to m           {n,}   n or more
By default they are GREEDY (take as much as possible). Add ? after
a quantifier to make it LAZY (take as little as possible): *?  +?  ??
"""

# Program 1: *, + and ?
print(re.findall(r"ab*", "a ab abb abbb"))              # ['a', 'ab', 'abb', 'abbb']
print(re.findall(r"ab+", "a ab abb"))                   # ['ab', 'abb']
print(re.findall(r"colou?r", "color colour"))           # ['color', 'colour']

# Program 2: Counted repeats
print(re.findall(r"\d{3}", "12 345 6789"))              # ['345', '678']
print(re.findall(r"\d{2,4}", "1 22 333 4444 55555"))    # ['22', '333', '4444', '5555']
print(re.findall(r"\d{3,}", "1 22 333 4444"))           # ['333', '4444']

# Program 3: Greedy vs lazy
html = "<b>bold</b> and <i>italic</i>"
print(re.findall(r"<.+>", html))                        # ['<b>bold</b> and <i>italic</i>']
print(re.findall(r"<.+?>", html))                       # ['<b>', '</b>', '<i>', '</i>']

# Program 4: Text between quotes
print(re.findall(r'"(.*?)"', 'say "hi" and "bye"'))     # ['hi', 'bye']

# Program 5: A pattern that can match nothing also matches empty strings
print(re.findall(r"a*", "baac"))                        # ['', 'aa', '', '']
print(re.findall(r"a+", "baac"))                        # ['aa']  (usually what you want)


# =====================================================
# Concept 12: Anchors
# =====================================================
r"""
Definition:
Anchors match a POSITION, not a character.
  ^   start of the text      $   end of the text (also just before a final \n)
  \A  start of the text only \Z  end of the text only
  \b  word boundary (between a \w and a \W, or at the text edge)
  \B  NOT a word boundary
"""

# Program 1: ^ and $
print(bool(re.search(r"^Hello", "Hello World")))        # True
print(bool(re.search(r"^World", "Hello World")))        # False
print(bool(re.search(r"World$", "Hello World")))        # True
print(bool(re.search(r"World$", "World Hello")))        # False

# Program 2: Both anchors make a validation
print(bool(re.search(r"^\d+$", "123")))                 # True
print(bool(re.search(r"^\d+$", "12a")))                 # False

# Program 3: Word boundaries find whole words only
print(re.findall(r"cat", "cat concat cat."))            # ['cat', 'cat', 'cat']
print(re.findall(r"\bcat\b", "cat concat cat."))        # ['cat', 'cat']

# Program 4: $ vs \Z with a trailing new line
print(bool(re.search(r"abc$", "abc\n")))                # True
print(bool(re.search(r"abc\Z", "abc\n")))               # False

# Program 5: Check that a status line starts with a timestamp
print(bool(re.match(r"^\d{2}:\d{2}:\d{2} ", "10:30:15 started")))   # True


# =====================================================
# Concept 13: Alternation (|)
# =====================================================
"""
Definition:
The pipe | means OR. cat|dog matches "cat" or "dog". Put the options
in parentheses to limit the OR to one part of the pattern. The
options are tried from LEFT to right, and the first one that works wins.
"""

# Program 1: Simple OR
print(re.findall(r"cat|dog", "cat dog bird"))           # ['cat', 'dog']

# Program 2: Parentheses limit the OR
print(re.search(r"gr(a|e)y", "grey").group())           # grey
print(re.findall(r"gra|ey", "gray grey"))               # ['gra', 'ey'] (a different meaning!)

# Program 3: Match several statuses
log = "[PASS] a [FAIL] b [WARN] c"
print(re.findall(r"\[(PASS|FAIL|ERROR)\]", log))        # ['PASS', 'FAIL']

# Program 4: The order of the options matters
print(re.search(r"a|ab", "ab").group())                 # a
print(re.search(r"ab|a", "ab").group())                 # ab


# =====================================================
# Concept 14: Groups
# =====================================================
"""
Definition:
Parentheses create a GROUP. Groups let you
 - extract part of a match                    (...)       numbered 1, 2, 3...
 - group without capturing                    (?:...)
 - name a group                               (?P<name>...)
 - repeat the same text again                 \1 \2 (back-reference)
A group that did not take part in the match is None.
"""

# Program 1: Capturing groups
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2026-10-17")
year, month, day = m.groups()
print(year, month, day)                 # 2026 10 17

# Program 2: Non-capturing group (groups the text, but is not returned)
print(re.findall(r"(?:Mr|Ms)\. (\w+)", "Mr. Ali and Ms. Sara"))     # ['Ali', 'Sara']

# Program 3: Named groups
m = re.search(r"(?P<hour>\d{2}):(?P<minute>\d{2})", "Time 10:30")
print(m.group("hour"), m.group("minute"))       # 10 30
print(m.groupdict())                            # {'hour': '10', 'minute': '30'}

# Program 4: Back-references
print(re.search(r"(\w)\1", "hello").group())                    # ll
print(re.findall(r"\b(\w+) \1\b", "this is is a test test"))    # ['is', 'test']

# Program 5: An optional group that did not match
m = re.search(r"(\d+)(px)?", "100")
print(m.groups())                       # ('100', None)
m = re.search(r"(\d+)(px)?", "100px")
print(m.groups())                       # ('100', 'px')


# =====================================================
# Concept 15: Flags
# =====================================================
"""
Definition:
Flags change how a pattern works. Combine them with |.
  re.IGNORECASE (re.I)  ignore upper/lower case
  re.MULTILINE  (re.M)  ^ and $ work on every LINE
  re.DOTALL     (re.S)  the dot also matches a new line
  re.VERBOSE    (re.X)  spaces/comments inside the pattern are ignored
  re.ASCII      (re.A)  \w \d \s \b use English characters only
Inline version: (?i) at the very START of the pattern.
"""

# Program 1: IGNORECASE
print(re.findall(r"python", "Python PYTHON python", re.IGNORECASE))     # ['Python', 'PYTHON', 'python']

# Program 2: MULTILINE
text = "line1\nline2\nline3"
print(re.findall(r"^line\d", text))                     # ['line1']
print(re.findall(r"^line\d", text, re.MULTILINE))       # ['line1', 'line2', 'line3']
print(re.findall(r"\d$", text, re.MULTILINE))           # ['1', '2', '3']

# Program 3: DOTALL
print(re.search(r"a.b", "a\nb"))                        # None
print(bool(re.search(r"a.b", "a\nb", re.DOTALL)))       # True

# Program 4: VERBOSE (write a long pattern with comments)
pattern = re.compile(r"""
    (\d{3})     # three digits
    -           # a dash
    (\d{4})     # four digits
""", re.VERBOSE)
print(pattern.fullmatch("555-1234").groups())           # ('555', '1234')

# Program 5: Combine flags
print(re.findall(r"^error", "Error one\nerror two", re.I | re.M))   # ['Error', 'error']

# Program 6: Inline flag at the start of the pattern
print(re.findall(r"(?i)python", "Python PYTHON"))       # ['Python', 'PYTHON']


# =====================================================
# Concept 16: split()
# =====================================================
"""
Definition:
re.split(pattern, text) cuts the text wherever the pattern matches.
It is a stronger str.split(): you can use several separators at once.
If the pattern has a group, the separators are kept in the result.
Empty strings can appear at the edges.
"""

# Program 1: Several separators at once
print(re.split(r"[,;]\s*", "apple, banana;  cherry,orange"))    # ['apple', 'banana', 'cherry', 'orange']

# Program 2: Runs of spaces (note the empty strings at the edges)
print(re.split(r"\s+", "  a   b  "))                    # ['', 'a', 'b', '']
print("  a   b  ".split())                              # ['a', 'b']

# Program 3: Keep the separators with a group
print(re.split(r"(\d)", "a1b2c"))                       # ['a', '1', 'b', '2', 'c']

# Program 4: maxsplit
print(re.split(r"-", "a-b-c-d", maxsplit=2))            # ['a', 'b', 'c-d']

# Program 5: Split a sentence into words
words = re.split(r"\W+", "Hello, world! How are you?")
print(words)                                            # ['Hello', 'world', 'How', 'are', 'you', '']
print([w for w in words if w])                          # ['Hello', 'world', 'How', 'are', 'you']


# =====================================================
# Concept 17: sub() and subn()
# =====================================================
r"""
Definition:
re.sub(pattern, replacement, text) replaces every match.
The replacement can use groups: \1 \2 or \g<name>.
The replacement can also be a FUNCTION that gets the Match object
and returns the new text.
re.subn() returns (new_text, number_of_replacements).
"""

# Program 1: Replace every digit
print(re.sub(r"\d", "X", "My phone is 0300-1234567"))       # My phone is XXXX-XXXXXXX

# Program 2: Clean up spaces
print(re.sub(r"\s+", " ", "a   b \t c"))                    # a b c

# Program 3: Use groups in the replacement
print(re.sub(r"(\w+)@(\w+)\.com", r"\2: \1", "ali@example.com"))    # example: ali

# Program 4: Named groups, reorder a date
print(re.sub(r"(?P<d>\d{2})/(?P<m>\d{2})/(?P<y>\d{4})", r"\g<y>-\g<m>-\g<d>", "17/10/2026"))   # 2026-10-17

# Program 5: A function as replacement
print(re.sub(r"\d+", lambda m: str(int(m.group()) * 2), "a1 b20 c300"))     # a2 b40 c600

# Program 6: Limit the replacements
print(re.sub(r"a", "X", "banana", count=2))             # bXnXna

# Program 7: subn() also tells how many replacements were made
print(re.subn(r"a", "X", "banana"))                     # ('bXnXnX', 3)

# Program 8: Hide an email address
log = "User email: ali@example.com logged in"
print(re.sub(r"[\w.]+@[\w.]+", "[EMAIL HIDDEN]", log))  # User email: [EMAIL HIDDEN] logged in


# =====================================================
# Concept 18: compile()
# =====================================================
"""
Definition:
re.compile(pattern, flags) returns a reusable Pattern object. It has
the same functions as the re module (search, match, fullmatch,
findall, finditer, split, sub) without repeating the pattern.
Python also caches recently used patterns, so compile() mainly makes
code cleaner and lets you name the pattern.
"""

# Program 1: Compile once, use many times
pattern = re.compile(r"\d+")
print(pattern.search("Order 123").group())      # 123
print(pattern.findall("1 22 333"))              # ['1', '22', '333']
print(pattern.sub("#", "a1 b22"))               # a# b#

# Program 2: Compile with flags
python_word = re.compile(r"python", re.IGNORECASE)
print(python_word.findall("Python PYTHON py"))  # ['Python', 'PYTHON']

# Program 3: Reuse a validation pattern in a loop
code_pattern = re.compile(r"[A-Z]{2}\d{3}")
for code in ["AB123", "ab123", "AB12", "ABC123"]:
    print(code, bool(code_pattern.fullmatch(code)))     # True False False False

# Program 4: Look at the pattern object
p = re.compile(r"(\d+)-(\d+)")
print(p.pattern, p.groups)                      # (\d+)-(\d+) 2

# Program 5: Give a pattern a meaningful name
DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
print(DATE.findall("From 2026-10-01 to 2026-10-17"))    # ['2026-10-01', '2026-10-17']


# =====================================================
# Concept 19: Lookahead and Lookbehind
# =====================================================
"""
Definition:
Lookarounds check what is NEXT TO the position without including it
in the match (they have zero width).
  (?=...)  followed by ...          (?!...)  NOT followed by ...
  (?<=...) preceded by ...          (?<!...) NOT preceded by ...
Lookbehind patterns must have a fixed length.
"""

# Program 1: Followed by
print(re.findall(r"\w+(?=\.py)", "a.py b.txt c.py"))            # ['a', 'c']

# Program 2: Not followed by
print(re.findall(r"\b\w+\.(?!py)\w+", "a.py b.txt c.csv"))      # ['b.txt', 'c.csv']

# Program 3: Preceded by (take the number, but not the dollar sign)
print(re.findall(r"(?<=\$)\d+", "cost $50 and $120"))            # ['50', '120']

# Program 4: Not preceded by
print(re.findall(r"(?<!\$)\b\d+", "$50 and 70"))                # ['70']

# Program 5: Overlapping matches
print([m.start() for m in re.finditer(r"(?=aa)", "aaaa")])      # [0, 1, 2]

# Program 6: Password rules checked in one pattern
rules = r"(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}"
for pw in ["Test@123", "weakpass", "Test1234"]:
    print(pw, bool(re.fullmatch(rules, pw)))                    # True False False


# =====================================================
# Concept 20: Common Mistakes
# =====================================================
"""
Definition:
The mistakes beginners make most often with regex.
Also remember: do not use regex for what a string method does well,
and do not parse full HTML or JSON with regex (use a real parser).
Very nested patterns such as (a+)+b can become extremely slow on
some inputs (catastrophic backtracking), so keep patterns simple.
"""

# Program 1: A normal string instead of a raw string
print(re.findall("\bcat\b", "cat"))             # [] (wrong)
print(re.findall(r"\bcat\b", "cat"))            #