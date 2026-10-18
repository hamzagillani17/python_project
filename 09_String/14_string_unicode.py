"""
====================================================
09_Strings / 14_string_unicode.py
====================================================
Topic: Built-in Functions for Strings + Unicode + Encoding
====================================================
Notes before you run this file:
1) Run it in a real terminal (VS Code terminal, PowerShell or Windows
   Terminal). If you see ? or boxes, that is the terminal font, not Python.
   If Windows raises UnicodeEncodeError while printing, run:  set PYTHONUTF8=1
2) Urdu/Arabic is written right-to-left. Some terminals show it visually
   reversed or joined strangely. In memory the characters are always
   stored in logical (typing) order, so len(), indexing and slicing
   work on that order.
3) The file is saved as UTF-8, so Urdu text can be written directly
   inside the code.
"""

import sys
import os
import ast
import json
import locale
import unicodedata
from urllib.parse import quote, unquote


# =====================================================
# Concept 1: len()
# =====================================================
"""
Definition:
len() returns the number of CHARACTERS (code points) in a string.
Spaces count too. It does not return the number of bytes.
"""

# Program 1: Basic lengths
print(len("Hello"))                    # 5
print(len("Hello World"))              # 11
print(len(""))                         # 0

# Program 2: len() counts characters, not bytes
print(len("سلام"))                     # 4 characters
print(len("سلام".encode("utf-8")))     # 8 bytes

# Program 3: len() works on other types, but not on numbers
print(len([1, 2, 3]), len((1, 2)), len({"a": 1}))   # 3 2 1
try:
    len(5)
except TypeError as e:
    print("Error:", e)                 # object of type 'int' has no len()


# =====================================================
# Concept 2: str()
# =====================================================
"""
Definition:
str() converts any object into its readable text form (a string).
str(bytes, encoding) decodes bytes into text.
"""

# Program 1: Convert numbers and other objects
print(str(25), type(str(25)))          # 25 <class 'str'>
print(str(3.14), str(True), str(None)) # 3.14 True None
print(str([1, 2, 3]))                  # [1, 2, 3]

# Program 2: str() is needed to join text with a number
age = 25
print("Age: " + str(age))              # Age: 25

# Program 3: str() on bytes vs decoding bytes
data = b"abc"
print(str(data))                       # b'abc' (looks like the bytes literal)
print(str(data, "utf-8"))              # abc    (real decoding)



# =====================================================
# Concept 3: repr()
# =====================================================
r"""
Definition:
repr() returns the "developer view" of an object: a string that shows
exactly what is inside, including quotes and hidden characters such
as \n, \t and \xa0. It is the best tool for debugging text.
"""

# Program 1: print() vs repr() with a new line
text = "Hello\nWorld"
print(text)                            # two lines
print(repr(text))                      # 'Hello\nWorld'

# Program 2: Find hidden whitespace
for s in ["Pass", "Pass ", "Pass\n", "Pass\xa0"]:
    print(repr(s))                     # all look the same in print(), not in repr()

# Program 3: Quotes inside text, and the !r shortcut in f-strings
print(repr("It's"))                    # "It's"
print(repr('He said "hi"'))            # 'He said "hi"'
print(repr("It's \"ok\""))             # 'It\'s "ok"'
name = "Ali"
print(f"{name!r}")                     # 'Ali'


# =====================================================
# Concept 4: str() vs repr()
# =====================================================
"""
Definition:
str()  -> readable text for users.
repr() -> exact text for developers (a string that looks like code).
print() uses str(). Items inside a list are shown with repr().
"""

# Program 1: Same value, two views
value = "Ali"
print(str(value), repr(value))         # Ali 'Ali'

# Program 2: Lists show their items with repr()
names = ["Ali", "Sara"]
print(names)                           # ['Ali', 'Sara']
print(str(names) == repr(names))       # True

# Program 3: repr() of a string can be turned back into the same string safely
original = "Hi\n"
restored = ast.literal_eval(repr(original))
print(restored == original)            # True


# =====================================================
# Concept 5: ascii()
# =====================================================
r"""
Definition:
ascii() works like repr(), but it also escapes every non-ASCII
character: \xNN, \uNNNN or \UNNNNNNNN. The result contains only
plain ASCII characters, which is safe to put in logs.
"""

# Program 1: Plain English text is unchanged
print(ascii("Hello"))                  # 'Hello'

# Program 2: Accented, Urdu and emoji characters are escaped
print(ascii("Héllo"))                  # 'H\xe9llo'
print(ascii("علی"))                    # '\u0639\u0644\u06cc'
print(ascii("😀"))                     # '\U0001f600'

# Program 3: repr() vs ascii()
print(repr("é"))                       # 'é'
print(ascii("é"))                      # '\xe9'


# =====================================================
# Concept 6: format()
# =====================================================
"""
Definition:
format(value, spec) turns a value into a string using the same format
specifier language as f-strings:  f"{value:spec}" calls
format(value, "spec") internally.
"""

# Program 1: Decimals, thousands separator and percentage
print(format(3.14159, ".2f"))          # 3.14
print(format(1234567, ","))            # 1,234,567
print(format(0.256, ".1%"))            # 25.6%

# Program 2: Number systems
print(format(255, "b"))                # 11111111 (binary)
print(format(255, "o"))                # 377      (octal)
print(format(255, "x"), format(255, "X"))   # ff FF (hex)

# Program 3: Width, alignment and padding
print("[" + format("Hi", "^10") + "]") # [    Hi    ]
print(format(5, "03"))                 # 005
print(format("Hi", "*>6"))             # ****Hi

# Program 4: format() and f-strings give the same result
print(format(3.14159, ".2f") == f"{3.14159:.2f}")   # True


# =====================================================
# Concept 7: ASCII
# =====================================================
"""
Definition:
ASCII is an old character table with only 128 characters (codes 0 to 127):
English letters, digits, punctuation and control characters.
It has no place for Urdu, Arabic, accented letters or emoji.
Codes 32 to 126 are printable, 0 to 31 and 127 are control characters.
"""

# Program 1: Important ASCII codes
print(ord("A"), ord("Z"), ord("a"), ord("z"))   # 65 90 97 122
print(ord("0"), ord("9"), ord(" "))             # 48 57 32
print(ord("\n"), ord("\t"))                     # 10 9

# Program 2: A small ASCII table (decimal, hex, binary)
print(f"{'Char':<6}{'Dec':<6}{'Hex':<7}{'Binary'}")
for code in range(65, 71):
    print(f"{chr(code):<6}{code:<6}{code:<#7x}{code:08b}")

# Program 3: The gap between a lowercase letter and its capital is 32
print(ord("a") - ord("A"))                      # 32
print(chr(ord("a") - 32))                       # A (manual upper())

# Program 4: Check whether a text is pure ASCII
print("Hello".isascii(), "Héllo".isascii(), "علی".isascii())   # True False False


# =====================================================
# Concept 8: ord()
# =====================================================
"""
Definition:
ord(character) returns the Unicode number (code point) of ONE
character. It raises a TypeError if the text is not exactly one
character long.
"""

# Program 1: Code points of different characters
print(ord("A"))                        # 65
print(ord("ا"))                        # 1575  (Urdu/Arabic alif)
print(ord("😀"))                       # 128512

# Program 2: The same number in hexadecimal (the U+ notation)
print(hex(ord("ا")))                   # 0x627
print(hex(ord("😀")))                  # 0x1f600
print(hex(ord("€")))                   # 0x20ac

# Program 3: ord() of every character of a word
for ch in "Hi!":
    print(ch, ord(ch))

# Program 4: ord() needs exactly one character
for bad in ["AB", ""]:
    try:
        ord(bad)
    except TypeError as e:
        print("Error:", e)


# =====================================================
# Concept 9: chr()
# =====================================================
"""
Definition:
chr(number) is the opposite of ord(): it returns the character that
belongs to a Unicode number. Valid numbers are 0 to 1114111 (0x10FFFF).
"""

# Program 1: Numbers to characters
print(chr(65), chr(97), chr(48))       # A a 0
print(chr(1575))                       # ا
print(chr(128512))                     # 😀
print(chr(0x20AC))                     # €

# Program 2: ord() and chr() undo each other
print(chr(ord("x")) == "x")            # True
print(ord(chr(1575)) == 1575)          # True

# Program 3: Generate the lowercase alphabet
letters = ""
for code in range(ord("a"), ord("z") + 1):
    letters += chr(code)
print(letters)                         # abcdefghijklmnopqrstuvwxyz

# Program 4: The valid range
print(0x10FFFF)                        # 1114111 (largest valid code point)
try:
    chr(1114112)
except ValueError as e:
    print("Error:", e)                 # chr() arg not in range(0x110000)


# =====================================================
# Concept 10: ord() and chr() in Practice
# =====================================================
"""
Definition:
Because characters are numbers, you can do maths on them: shift
letters (Caesar cipher), convert digit characters to numbers,
sort by code, or build a simple checksum.
"""

# Program 1: Caesar cipher (shift lowercase letters by 3)
text = "hello world"
shift = 3
encrypted = ""
for ch in text:
    if "a" <= ch <= "z":
        encrypted += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        encrypted += ch
print(encrypted)                       # khoor zruog

# Program 2: Decrypt it again (shift in the opposite direction)
decrypted = ""
for ch in encrypted:
    if "a" <= ch <= "z":
        decrypted += chr((ord(ch) - ord("a") - shift) % 26 + ord("a"))
    else:
        decrypted += ch
print(decrypted)                       # hello world

# Program 3: Convert digit characters to a number without int()
number = 0
for ch in "472":
    number = number * 10 + (ord(ch) - ord("0"))
print(number, number + 1)              # 472 473

# Program 4: Sorting follows code points, capitals come first
print(sorted(["b", "a", "B", "A"]))                # ['A', 'B', 'a', 'b']
print(sorted(["b", "a", "B", "A"], key=str.casefold))   # case-insensitive order

# Program 5: A simple checksum (sum of all codes)
total = 0
for ch in "abc":
    total += ord(ch)
print(total)                           # 294


# =====================================================
# Concept 11: Unicode
# =====================================================
"""
Definition:
Unicode is one universal table that gives every character of every
language (and emoji) a unique number called a CODE POINT, written as
U+ followed by hex digits, for example U+0041 is "A".
The first 128 code points are exactly the ASCII table.
Python strings are sequences of Unicode code points.
"""

# Program 1: Code point and official name of different characters
for ch in ["A", "é", "ا", "€", "😀"]:
    print(f"{ch}  U+{ord(ch):04X}  {ord(ch):>6}  {unicodedata.name(ch)}")

# Program 2: Write a character using its code point inside a string
print("\x41")                          # A  (2 hex digits)
print("\u0627")                        # ا  (4 hex digits)
print("\U0001F600")                    # 😀 (8 hex digits)
print("\N{EURO SIGN}")                 # €  (by name)

# Program 3: Character categories
for ch in ["A", "a", "5", " ", "ا", "😀"]:
    print(repr(ch), unicodedata.category(ch))   # Lu Ll Nd Zs Lo So

# Program 4: ASCII is the first part of Unicode
all_ascii = True
for code in range(128):
    if not chr(code).isascii():
        all_ascii = False
print(all_ascii)                       # True
print(0x110000, "code points are available in total")


# =====================================================
# Concept 12: UTF-8
# =====================================================
"""
Definition:
Unicode gives characters numbers. UTF-8 is a way to STORE those numbers
as bytes. It uses 1 to 4 bytes per character:
  ASCII characters    -> 1 byte
  Urdu/Arabic/Latin accents -> 2 bytes
  Most Asian characters, € -> 3 bytes
  Emoji               -> 4 bytes
UTF-8 is the standard encoding of the web, files and APIs.
"""

# Program 1: Bytes used by different characters
for ch in ["A", "é", "ا", "€", "😀"]:
    data = ch.encode("utf-8")
    print(ch, data, len(data), "byte(s)")

# Program 2: Look at the bits of a 2-byte character
data = "é".encode("utf-8")
for byte in data:
    print(f"{byte:08b}")               # 11000011 then 10101001
# First byte starts with 110 (start of a 2-byte character),
# the next byte starts with 10 (a continuation byte).

# Program 3: Characters vs bytes in a mixed text
text = "Hello 😀"
print(len(text), len(text.encode("utf-8")))     # 7 10

# Program 4: UTF-8 is compatible with ASCII
print("Hello".encode("utf-8") == "Hello".encode("ascii"))   # True
print(sys.getdefaultencoding())        # utf-8


# =====================================================
# Concept 13: Urdu / Arabic Characters
# =====================================================
"""
Definition:
Python 3 strings are fully Unicode, so Urdu and Arabic text works with
the same tools as English text: len(), indexing, slicing, split(),
find(), count(), isalpha() and so on.
Urdu has no uppercase/lowercase, so upper() and lower() change nothing.
"""

# Program 1: Look inside an Urdu word
name = "علی"
print(len(name))                       # 3
for ch in name:
    print(ch, hex(ord(ch)), unicodedata.name(ch))

# Program 2: Normal string operations on Urdu
sentence = "پاکستان زندہ باد"
words = sentence.split()
print(words, len(words))               # 3 words
print("پاکستان".count("ا"))            # 2
print("پاکستان".find("ک"))             # 2
print("پاکستان".startswith("پا"))      # True

# Program 3: Indexing and slicing use the logical (typing) order
word = "پاکستان"
print(word[0])                         # پ (the first letter typed)
print(word[:3])                        # first 3 letters

# Program 4: Letters, case and digits
print("علی".isalpha())                 # True
print("علی".upper() == "علی")          # True (no case in Urdu)
print(int("\u06f1\u06f2\u06f3"))       # 123 (Urdu digits ۱۲۳)
print(int("\u0661\u0662\u0663"))       # 123 (Arabic-Indic digits ١٢٣)
print("\u06f1\u06f2\u06f3".isdecimal())   # True


# =====================================================
# Concept 14: Emoji and Multi-Code-Point Characters
# =====================================================
"""
Definition:
An emoji is a normal Unicode character (usually code point above
U+1F000). Some things that look like ONE symbol are really several
code points joined together (skin tone, family, flags). len() counts
code points, not what your eyes see.
"""

# Program 1: A simple emoji
smile = "\U0001F600"
print(smile, len(smile), ord(smile), smile.encode("utf-8"))

# Program 2: One symbol, several code points
thumbs = "\U0001F44D\U0001F3FD"                    # thumbs up + skin tone
family = "\U0001F468\u200d\U0001F469\u200d\U0001F467"   # man + woman + girl joined
flag = "\U0001F1F5\U0001F1F0"                      # two regional letters
print(thumbs, len(thumbs))             # 2
print(family, len(family))             # 5
print(flag, len(flag))                 # 2

# Program 3: Bytes of those emoji in UTF-8
print(len(family.encode("utf-8")))     # 18

# Program 4: Emoji inside a test message, and removing them
message = "Test Passed \u2705 done"
print(message, len(message))
only_ascii = ""
for ch in message:
    if ch.isascii():
        only_ascii += ch
print(only_ascii)                      # Test Passed  done


# =====================================================
# Concept 15: Encoding vs Decoding
# =====================================================
"""
Definition:
Computers store and send BYTES, not characters.
Encoding = text (str) -> bytes
Decoding = bytes -> text (str)
        str  --encode-->  bytes  --decode-->  str
The encoding name (for example utf-8) is the rule used in BOTH
directions, so it must be the same on both sides.
"""

# Program 1: str and bytes are different types
text = "Hi"
data = text.encode("utf-8")
print(type(text), type(data))          # <class 'str'> <class 'bytes'>
print(text[0], data[0])                # H 72 (indexing bytes gives numbers)

# Program 2: str and bytes cannot be mixed
print("abc" == b"abc")                 # False
try:
    print("abc" + b"def")
except TypeError as e:
    print("Error:", e)

# Program 3: A full round trip with Urdu text
original = "پاکستان"
encoded = original.encode("utf-8")
decoded = encoded.decode("utf-8")
print(encoded)
print(decoded)
print(original == decoded)             # True


# =====================================================
# Concept 16: encode()
# =====================================================
"""
Definition:
str.encode(encoding="utf-8", errors="strict") returns a bytes object.
If you write nothing, UTF-8 is used.
"""

# Program 1: Default encoding
print("Hello".encode())                # b'Hello'
print("سلام".encode())                 # b'\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85'

# Program 2: Bytes as numbers and as hex text
print(list("Hi".encode()))             # [72, 105]
print("Hi".encode().hex())             # 4869
print(bytes.fromhex("4869"))           # b'Hi'

# Program 3: The same character gives different bytes in different encodings
print("é".encode("utf-8"))             # b'\xc3\xa9'
print("é".encode("latin-1"))           # b'\xe9'
print("é".encode("utf-16-le"))         # b'\xe9\x00'


# =====================================================
# Concept 17: decode()
# =====================================================
"""
Definition:
bytes.decode(encoding="utf-8", errors="strict") returns a str.
You must use the same encoding that was used to create the bytes.
"""

# Program 1: Decode simple and Urdu bytes
print(b"Hello".decode())               # Hello
print(b"\xd8\xb3\xd9\x84\xd8\xa7\xd9\x85".decode("utf-8"))    # سلام

# Program 2: Build bytes from numbers and decode them
print(bytes([72, 105]).decode())       # Hi
print(bytearray(b"abc").decode())      # abc

# Program 3: Invalid bytes raise an error
try:
    b"\xff".decode("utf-8")
except UnicodeDecodeError as e:
    print(type(e).__name__)            # UnicodeDecodeError
    print(e)


# =====================================================
# Concept 18: Encoding Errors and Garbled Text (Mojibake)
# =====================================================
"""
Definition:
UnicodeEncodeError: a character does not exist in the target encoding.
UnicodeDecodeError: the bytes are not valid for that encoding.
The errors= argument decides what to do: "strict" (raise an error,
the default), "ignore", "replace", "xmlcharrefreplace", "backslashreplace".
Mojibake = unreadable text caused by decoding with the WRONG encoding.
"""

# Program 1: ASCII cannot store é
try:
    "café".encode("ascii")
except UnicodeEncodeError as e:
    print(type(e).__name__)            # UnicodeEncodeError

# Program 2: Choosing a strategy with errors=
print("café".encode("ascii", errors="ignore"))              # b'caf'
print("café".encode("ascii", errors="replace"))             # b'caf?'
print("café".encode("ascii", errors="xmlcharrefreplace"))   # b'caf&#233;'
print("café".encode("ascii", errors="backslashreplace"))    # b'caf\\xe9'

# Program 3: Decoding with errors=
broken = b"caf\xe9"                    # latin-1 bytes, not valid UTF-8
print(broken.decode("utf-8", errors="replace"))     # caf with a replacement symbol
print(broken.decode("utf-8", errors="ignore"))      # caf
print(broken.decode("latin-1"))                     # café (correct encoding)

# Program 4: Mojibake and how to repair it
good = "é"
garbled = good.encode("utf-8").decode("latin-1")
print(garbled)                         # Ã©
repaired = garbled.encode("latin-1").decode("utf-8")
print(repaired, repaired == good)      # é True
print(repr("سلام".encode("utf-8").decode("latin-1")))     # unreadable text


# =====================================================
# Concept 19: Other Encodings and the BOM
# =====================================================
"""
Definition:
ascii    : 128 characters, 1 byte each.
latin-1  : 256 characters (Western European), 1 byte each.
utf-8    : all of Unicode, 1 to 4 bytes (variable).
utf-16   : all of Unicode, 2 or 4 bytes. utf-32: always 4 bytes.
BOM (Byte Order Mark) is a few extra bytes at the start of a file that
mark the encoding. "utf-8-sig" adds/removes a BOM; Excel often needs
it for UTF-8 CSV files that contain Urdu or accents.
"""

# Program 1: Bytes needed per character in each encoding
print(f"{'Char':<6}{'utf-8':<8}{'utf-16':<8}{'utf-32':<8}")
for ch in ["A", "é", "ا", "😀"]:
    print(f"{ch:<6}{len(ch.encode('utf-8')):<8}"
          f"{len(ch.encode('utf-16-le')):<8}{len(ch.encode('utf-32-le')):<8}")

# Program 2: utf-16 adds a BOM when you do not choose a byte order
print(len("A".encode("utf-16")))       # 4 (2 BOM bytes + 2 character bytes)
print(len("A".encode("utf-16-le")))    # 2

# Program 3: utf-8-sig and the invisible BOM character
with_bom = "A".encode("utf-8-sig")
print(with_bom)                        # b'\xef\xbb\xbfA'
print(repr(with_bom.decode("utf-8")))      # '\ufeffA'  (BOM left inside the text!)
print(repr(with_bom.decode("utf-8-sig")))  # 'A'


# =====================================================
# Concept 20: Files and Encoding
# =====================================================
"""
Definition:
A file stores bytes. When you open a file in text mode, Python
encodes/decodes for you using the encoding you give. If you do not
give one, Python uses the computer's default, which may NOT be UTF-8
(often cp1252 on Windows). Always write encoding="utf-8".
The 'with' statement closes the file automatically.
"""

filename = "unicode_demo.txt"

# Program 1: Write and read Urdu text with UTF-8
with open(filename, "w", encoding="utf-8") as f:
    f.write("سلام Hello")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())                    # سلام Hello

# Program 2: See the raw bytes stored in the file
with open(filename, "rb") as f:
    raw = f.read()
print(raw)
print(len(raw))                        # 14 (8 bytes Urdu + 1 space + 5 English)

# Program 3: Reading with the wrong encoding gives garbled text
with open(filename, "r", encoding="latin-1") as f:
    print(repr(f.read()))              # unreadable text

# Program 4: The computer's default encoding
print(locale.getpreferredencoding(False))    # may print cp1252 on Windows

# Program 5: Writing Urdu with ascii fails
try:
    with open(filename, "w", encoding="ascii") as f:
        f.write("سلام")
except UnicodeEncodeError as e:
    print("Error:", type(e).__name__)

if os.path.exists(filename):
    os.remove(filename)                # clean up the demo file


# =====================================================
# Concept 21: Unicode Normalization
# =====================================================
"""
Definition:
The same visible character can be stored in more than one way.
Example: "é" can be ONE code point (U+00E9) or TWO code points
(e + a combining accent U+0301). They look identical but are not
equal with ==. unicodedata.normalize() converts texts to one standard
form: NFC (composed, usually best for comparing), NFD (decomposed),
NFKC (also converts "compatibility" characters like full-width letters).
"""

# Program 1: Two ways to write é
a = "\u00e9"
b = "e\u0301"
print(a, b)                            # look the same
print(a == b)                          # False
print(len(a), len(b))                  # 1 2

# Program 2: Normalize before comparing
print(unicodedata.normalize("NFC", a) == unicodedata.normalize("NFC", b))   # True

# Program 3: Remove accents from a text
text = "Café résumé"
result = ""
for ch in unicodedata.normalize("NFD", text):
    if unicodedata.category(ch) != "Mn":     # Mn = combining mark
        result += ch
print(result)                          # Cafe resume

# Program 4: NFKC fixes compatibility characters
print(unicodedata.normalize("NFKC", "\uff21\uff22\uff23"))   # ABC (from full-width ＡＢＣ)
print(unicodedata.normalize("NFKC", "\ufb01"))               # fi  (from the ligature)


# =====================================================
# Concept 22: Unicode in SQA Automation
# =====================================================
"""
Definition:
Test data and web pages often contain Urdu, accents, emoji, hidden
spaces and zero-width characters. Compare texts after cleaning and
normalizing, know the difference between characters and bytes
(field limits), and know how JSON and URLs encode non-ASCII text.
"""

# Program 1: Expected vs actual Urdu text from a web page
expected = "خوش آمدید"
actual = "  خوش آمدید\xa0"              # extra spaces and a non-breaking space
cleaned = unicodedata.normalize("NFC", actual.strip())
print(repr(actual))
print(cleaned == unicodedata.normalize("NFC", expected))     # True

# Program 2: JSON escapes non-ASCII text by default
data = {"message": "سلام", "status": "ok"}
escaped = json.dumps(data)
readable = json.dumps(data, ensure_ascii=False)
print(escaped)                         # {"message": "\u0633\u0644...", "status": "ok"}
print(readable)                        # {"message": "سلام", "status": "ok"}
print(json.loads(escaped) == data)     # True
print(json.loads(readable) == data)    # True

# Program 3: URLs percent-encode the UTF-8 bytes
encoded_url_text = quote("سلام")
print(encoded_url_text)                # %D8%B3%D9%84%D8%A7%D9%85
print(unquote(encoded_url_text))       # سلام
print(quote("hello world"))            # hello%20world

# Program 4: Test names with different scripts (characters vs bytes)
for name in ["Ali", "José", "علی", "李雷", "😀"]:
    print(f"{name:<6} chars={len(name):<3} bytes={len(name.encode('utf-8')):<3} ascii={name.isascii()}")

# Program 5: A field limit may be in BYTES, not characters
username = "علی" * 4                   # 12 characters
print(len(username), len(username.encode("utf-8")))    # 12 24
print("Fits in 20 bytes?", len(username.encode("utf-8")) <= 20)    # False

# Program 6: Zero-width space is invisible and strip() does NOT remove it
text = "Login\u200b"
print(text == "Login")                 # False
print(len(text), len(text.strip()))    # 6 6
print(text.replace("\u200b", "") == "Login")      # True
for ch in text:
    if not ch.isprintable() or unicodedata.category(ch) == "Cf":
        print("Hidden character found:", hex(ord(ch)), unicodedata.name(ch))




























































































































































































































