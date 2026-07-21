print("=======iterable type in for loop=======")

'''In Python, an iterable is any object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
An iterable object implements the __iter__() method, which returns an iterator object. The iterator object implements the __next__() method, which returns the next item in the sequence. When there are no more items to return, it raises a StopIteration exception.
'''
#List
print("\n===============List==============")
fruits = ["Mango", "Orange","Apple","Graps"]
for fruit in fruits :
     print(fruit,"  Fruits ID",id(fruits))   # prints each element of the list one by one


print("\n----Find out Largest NUmber-----")

number_list = [12,34,56,78,90,45,33,100,600]
max_number = number_list[0]
for num in number_list:
     if num > max_number:
          max_number = num
print("Largest number is: ",max_number)

print("\n-----Find the Minimum (Smallest) Number in a List-------")

number_list1 = [0,1,2,3,4,5,6,78,34,23,-1]
small_num = number_list1[0]
for min_num in number_list1:
     if min_num < small_num:
          small_num = min_num
print("small number is: ",small_num)          


print("\n-----add all list numbers----")
numbers_add = [10,20,30,40]
total = 0
for num in numbers_add:
    total += num
print(total)  

print("\n------Count Even Numbers-------")
number_all = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,11,21]
count = 0
for num in number_all :
     if num % 2 == 0:
        count+=1
        print("Even number:",num)          
print("Total Even Numbers:",count)

print("\n-------Count Even and Odd Numbers Separately-------")
number_all1 = [1,2,3,5,6,8,9,10,11,12,13,14,15,16,17,1,1,1,1,3]
even = 0
odd = 0
for num in  number_all1:
     if num % 2 == 0:
          even+=1
          print("even :",num) 
     else:
          odd+=1
          if num % 2 ==1:
            print("odd ",num)
print("Total Even: ",even)
print("Total odd: ",odd)      

print("\n-------Reverse a List (Without Using Built-in reverse())--------")

number_rev = [0,1,2,3,4,5,6]
reversed_list = []   # empty list to build the reversed version
for rev in number_rev:
     reversed_list.insert(0,rev) # insert each new number at the FRONT (position 0)
print(reversed_list) # 

print("\n------Find First & Second Largest Number------")

number_sl = [2,3,4,23,1,-2,34]

largest_num = float('-inf')
second_large_num = float('-inf')
print(number_sl)
for num in number_sl:
    
     if num > largest_num:
        second_large_num = largest_num
        largest_num = num
     elif num > second_large_num and num != largest_num:
        second_large_num = num

print("Largest number: ",largest_num)
print("Second largest number: ",second_large_num) 

print("------Count Occurrences of a Specific Value in a List--------")

numbers = [1, 2, 3, 2, 4, 2, 5, 2]
target = 2       # the value we want to count
occurrence_count = 0

for num in numbers:
    if num == target:          # check if current number matches the target
        occurrence_count += 1

print(f"The number {target} appears {occurrence_count} times")

print("\n-------Separate Positive and Negative Numbers Into Two New Lists-------")

numbers = [10, -5, 3, -8, 22, -1, 0]
positives = []   # empty list to collect positive numbers
negatives = []   # empty list to collect negative numbers

for num in numbers:
    if num > 0:
        positives.append(num)      # add to positives list
    elif num < 0:
        negatives.append(num)      # add to negatives list
    # note: 0 is neither positive nor negative, so it's skipped here

print("Positive numbers:", positives)
print("Negative numbers:", negatives)

print("\n--------Find Sum of Only Even Numbers in a List---------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0   # accumulator for sum of even numbers only

for num in numbers:
    if num % 2 == 0:        # only proceed if the number is even
        even_sum += num        # add it to our running sum

print("Sum of even numbers:", even_sum)

print("\n---------Check if a List Contains Any Duplicate Values-----------")
numbers = [10, 20, 30, 20, 50]
seen = []          # empty list to keep track of numbers we've already seen
has_duplicate = False   # flag to mark if a duplicate is found

for num in numbers:
    if num in seen:              # check if we've already seen this number before
        has_duplicate = True       # if yes, mark that a duplicate exists
    else:
        seen.append(num)           # if not, add it to our "seen" list

print("------Search an Item---------")        

print("Has duplicates?", has_duplicate)
names = ["Ali", "Sara", "Ahmed", "John"]
search = "Sara"
found = False
for name in names:
    if name == search:
        found = True
        break
print(found)






print("\n===================String==================")

str_ver = "ich bin Ali"
for i in str_ver:
    print(i, end='')

print("\n-------Count Vowels in a String--------")

str_text = "my name is ali, i live in lahore"
vowels = "aeiou"
count = 0
found_vowels = []

for letters in str_text:
    if letters in vowels:
        found_vowels.append(letters)
        count += 1
print(found_vowels, end=" ")
print("\n",count, end="") 


print("\n-------Count Digits--------")

str_num_text = "my adress : alber 19, 123, mobile:23232122"
count = 0
num_found = ""

for n in str_num_text:
    if n.isdigit():
     count+=1
print("Text chr:",count)


text = "Ali123Germany45"        # String contains letters and digits.
count = 0                       # Variable to count digits.

for ch in text:                 # Read one character at a time.
    if ch.isdigit():            # Check if character is a digit.
        count += 1              # Increase digit count.
print("Digits:", count)         # Display total digits.   


print("\n-------Count Numbers, Letters & Special Characters--------")

str_num_text = "my adress : alber 19, 123, mobile:23232122"

numbers_found = []   # poore numbers yahan store honge, jesy "19", "123"
temp_num = ""         # chhota buffer — digits ko jodne ke liye

alphabet_count = 0
special_count = 0

for ch in str_num_text:
    if ch.isdigit():
        temp_num += ch          # digit ko buffer mein jodo
    else:
        if temp_num != "":       # agar buffer mein kuch tha, matlab ek number khatam hua
            numbers_found.append(temp_num)
            temp_num = ""        # buffer khaali kardo agle number ke liye

        if ch.isalpha():
            alphabet_count += 1
        elif ch != " ":
            special_count += 1

# loop khatam hone ke baad check karo — agar string number pe hi khatam hoti hai
if temp_num != "":
    numbers_found.append(temp_num)

print("Numbers found:", numbers_found)
print("Total numeric values:", len(numbers_found))
print("Total alphabet characters:", alphabet_count)
print("Total special characters:", special_count)

print("\n-------Search Character--------")

str_chr = "Automation"
find_chr = "n"
target = ""
found = False

for chr in str_chr:
    if chr == find_chr:
        target=chr
        found = True
        break
if found:
    print(f" {found} :",target)
else:
    print("chr is not found",found)


print("\n-------Search Character--------")
text = "hello world"
char_to_find = "w"

result = text.find(char_to_find)

if result == -1:
    print("Character not found")
else:
    print("Character found at index:", result)

print("\n-------Uppercase Count--------")

str_text_u = "Python is Really easily Language"
count = 0
find = []

for chr in str_text_u:
    if chr.isupper():
        count += 1
        find.append(chr)
print(count)
print(find)   

print("\n-------Count Spaces--------")

str_text = "Python is ver easy language"
find = 0
for space in str_text:
   if space == " ":
    find += 1
print(find)    

print("\n-------Reverse String--------")

original_text = "der ist ein Hund"
rev_str = " "

for rev in original_text:
    rev_str = rev + rev_str
print("Original:" ,original_text)    
print("Reverse Text: ",rev_str)

print("\n-------Palindrome Check--------")

p_str = "madam"
rev_p = ""

for rev in p_str:
    rev_p = rev + rev_p

if p_str == rev_p:
     print(f"'{p_str}' is a palindrome")
else:
    print(f"'{rev_p}' is NOT a palindrome")

print("\n-------Character Frequency--------")

text = "banana"
freq = {}   # empty dictionary — will hold each character's count

for ch in text:
    if ch in freq:
        freq[ch] += 1      # character already seen before, so add 1 to its count
    else:
        freq[ch] = 1       # first time seeing this character, start count at 1

print("Frequency:", freq)    


print("\n-------Remove Spaces--------")

sentence = "my name is ali"
no_space = ""   # empty basket — will collect only non-space characters

for ch in sentence:
    if ch != " ":
        no_space += ch    # only add character if it's NOT a space

print("Original:", sentence)
print("Without spaces:", no_space) 

print("\n-------Count Words--------")

sentence = "my name is ali"
word_count = 0
inside_word = False   # tracks whether we are currently inside a word

for ch in sentence:
    if ch != " " and inside_word == False:
        # we just entered a new word (previous char was space or start of string)
        word_count += 1
        inside_word = True
    elif ch == " ":
        # we hit a space, meaning current word has ended
        inside_word = False

print("Sentence:", sentence)
print("Total words:", word_count)

print("\n==========Dictionary=============")

print("-------Dictionary Traversal--------")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78}
print("key")
for name in student_marks.keys():
    print(name)
# Loop through VALUES only
print("Values:")
for marks in student_marks.values():
    print(marks)


print("\n-------Student Marks (Dictionary)--------")
marks = {"Ali": 85, "Sara": 90, "Ahmed": 70, "Zara": 95}
total = 0

for name, score in marks.items():   # dictionary se key(name) aur value(score) dono nikalo
    print(name, "scored", score)
    total += score

average = total / len(marks)
print("Average Marks:", average)

print("-------Search a Key--------")
student_inf = {"ali": 85, "sara": 92, "ahmed": 78}
find_name = "ali"
found = False

for name in student_inf:
    if name == find_name:
        found = True
        break 
if found:
    print(find_name,student_inf[find_name]) 
else:
    print("not found")

print("-------Build Dictionary from List--------")

fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruit_count = {}

for fruit in fruits:
    if fruit in fruit_count:              # logical check: key already exists?
        fruit_count[fruit] += 1           # yes -> increase count
    else:
        fruit_count[fruit] = 1            # no -> create new entry with count 1

print("Fruit counts:", fruit_count) 

print("\n-------Find Highest Scorer--------")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78}

highest_name = ""
highest_marks = float('-inf')     # start with smallest possible value

lowest_name = ""
lowest_marks = float('inf')     # start with smallest possible value


for name, marks in student_marks.items():
    if marks > highest_marks:
        highest_marks = marks
        highest_name = name

    if marks < lowest_marks:
        lowest_marks= marks
        lowest_name = name     

print(highest_name,highest_marks)
print(lowest_name,lowest_marks)        

print("\n-------Merge Two Dictionaries--------")

week1_sales = {"mon": 100, "tue": 150, "wed": 200}
week2_sales = {"wed": 250, "thu": 180, "fri": 220}

combined_sales = {}

for day, amount in week1_sales.items():
    combined_sales[day] = amount

for day, amount in week2_sales.items():
    if day not in combined_sales:
        combined_sales[day] = amount
        print(f"{day} added fresh")
    else:
        combined_sales[day] = amount
        print(f"{day} updated/overwritten")

print(combined_sales)

print("\n-------Nested Dictionary--------")

students = {
    "ali": {"math": 85, "science": 90},
    "sara": {"math": 78, "science": 88}
}

for name, subjects in students.items():        # outer loop: goes through each student
    print(f"Student: {name}")
    for sub,marks in students.items():
        print(sub,marks)

print("\n-------Sort by Value--------")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78}

# sorted() with key=lambda tells Python to sort based on the VALUE, not the key
sorted_items = sorted(student_marks.items(), key=lambda pair: pair[1], reverse=True)

for name, marks in sorted_items:      # now looping through an already-sorted list of pairs
    print(f"{name}: {marks}")

print("\n-------Filter Dictionary--------")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78, "hina": 95}
passed_with_distinction = {}       # empty dictionary — will hold only filtered entries

for name, marks in student_marks.items():
    if marks >= 80:                 # logical condition — only keep entries matching this
        passed_with_distinction[name] = marks

print("Distinction holders:", passed_with_distinction)

print("\n-------Compare Two Dictionaries--------")

week1_sales = {"mon": 100, "tue": 150, "wed": 200}
week2_sales = {"wed": 250, "thu": 180, "tue": 220}

common_days = []      # empty list — will collect days present in BOTH dictionaries

for day in week1_sales:                  # looping over week1's keys
    if day in week2_sales:               # logical check: is this key also in week2?
        common_days.append(day)

print("Common days in both weeks:", common_days)

# bonus: show the difference in sales for common days
for day in common_days:
    diff = week2_sales[day] - week1_sales[day]
    print(f"{day}: week2 changed by {diff}")

print("-------Invert Dictionary--------")

student_marks = {"ali": 85, "sara": 92, "ahmed": 78}
inverted = {}          # empty dictionary — will hold the flipped version

for name, marks in student_marks.items():
    inverted[marks] = name         # value becomes the new key, key becomes the new value

print("Original:", student_marks)
print("Inverted:", inverted) 

print("\n=====Range============")

print("-----simple repeat----")

for i in range(5):
    print("this number repeat 5 time: ",i)  # i just counts 0 to 4, not used meaningfully

print("\n-------Access by Index--------")

furits = ["Mango", "Charry", "Orange", "Apple", "Banana"]
for i in range(len(furits)):
    print(f"Index {i}: {furits[i]}") 

print("---")

# cleaner way with enumerate
for i, fruit in enumerate(fruits):     # gives index AND value directly, no need for fruits[i]
    print(i, fruit)


print("\n-------Reverse Counting (Countdown)--------")

for i in range(20,-1,-1 ):
    print(i, end=" ")  

print("\n-------Reverse a List using range--------")

furits = ["Mango", "Charry", "Orange", "Apple", "Banana"]
for i in range(len(furits)-1,-1,-1):
    print(furits[i],end=" ")

print("\n-------Step Jump--------")

numbers = [10, 20, 30, 40, 50, 60, 70, 80]    

for i in range(0,len(numbers),2): # step=2 means skip every alternate index
    print(i,numbers[i])

print("\n-------Multiplication Table using step--------")

num = 9

for i in range(1,11):
    print(f"{num} x {i} = {num*i}")


print("-------Star Pattern--------")

rows = 5

for i in range(1, rows + 1):        # outer loop controls how many rows
    for j in range(i):              # inner loop controls how many stars in THIS row
        print("*", end="")          # end="" keeps printing on same line
    print()                          # move to next line after inner loop finishes    

print("\n-------Number Pattern--------")

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):       # j goes from 1 to i
        print(j, end=" ")
    print()

print("\n=========Basic Tuple Access=======")

student = ("Ali", 25, "Karachi")   # tuple with name, age, city

for i in student:
    print(i)

print("\n-------Tuple with Index using range--------")

student = ("Ali", 25, "Karachi")   # tuple with name, age, city

for i in range(len(student)):
    print(f"Index {i} : {student[i]}")

print("\n-------Loop with Unpacking--------")

student = [("Ali",95), ("Sara",89), ("Usman", 87),("Bilal", 75)]

for name, marks in student:
    print(f"{name} scored {marks}") 

print("\n-------Sum of Tuple Numbers--------")

number = (2,2,34,45,34,56,2)
total = 0

for add in number:
    total += add    # keep adding each number to total
print(total)

print("\n-------Largest and Smallest in Tuple--------")

numbers = (23, 5, 67, 12, 89, 3,99,54,2,1)
print(numbers)
largest_num = float('-inf')
small_num = float('inf')

for num in numbers:
    if num > largest_num:
        largest_num = num
    if num < small_num:
        small_num = num
print("Largest:", largest_num)
print("Smallest:", small_num)            

print("\n-------Loop Through Nested Tuples--------")

points = ((1, 2), (3, 4), (5, 6))    # tuple of tuples — like coordinate pairs

for x, y in points:
    #x,y = num1
    print(f"X = {x} : Y = {y}")

print("\n-------Count Even Numbers in Tuple--------")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,12,13,23)

even = 0
odd = 0
even_t = []
odd_t = []

for num in numbers:
    if num %2 == 0:
        even+=1
        even_t.append(num)
        
       
    if num % 2 == 1:
        odd+=1
        odd_t.append(num)

print("Total even values: ",even_t,end="\n")
print("Even number",even)
print("Total odd values: ",odd_t,end="\n")
print("odd number: ",odd)

print("\n-------Find Common Items using For Loop--------")

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
comen_list = []
for list in list_a:
    if list in list_b:
        comen_list.append(list)
print(comen_list)        


print("\n============sets============================")


numbers_sets = {1, 2, 2, 3, 4, 4, 4, 5, 1}
print(numbers_sets)

numbers_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
sets_number = set(numbers_list)             #list convert into set with set() function
print(sets_number,"types",type(sets_number))

empty = {}
print(empty, type(empty)) #empty {} considered as a dic

fruits = {"apple", "banana"}
fruits.add("cherry")          # ek item add karo
print(fruits)                  # {'apple', 'banana', 'cherry'}

fruits.remove("banana")        # specific item hatao
print(fruits)                  # {'apple', 'cherry'}

fruits.discard("mango")        # agar item maujood na ho toh error nahi dega (remove() error dega)

print("------------Remove Duplicates using Set-------------\n")

numbers_list = [1, 2, 2, 3, 4, 4, 4, 5, 1,7,9,9,7,7,6]
sets_number = set(numbers_list)             #list convert into set with set() function

for i in sets_number:
    print(i,end=" ")

print("Total unique numbers:",len(sets_number))

print("\n-------Manually Build a Set using For Loop--------")
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5, 1]
manual_set = set()      # start with an empty set

for num in numbers_list:
    if num not in manual_set:      # only add if not already present
        manual_set.add(num)

print("Manual unique set:", manual_set)

print("\n-------Find Common Items (Intersection) using For Loop--------")

list_a = {1, 2, 3, 4, 5}
list_b = {4, 5, 6, 7, 8}

set_b = set(list_b)
comen_list = set()

for list in list_a:
    if list in list_b:
        comen_list.add(list)
print("commen items: ",comen_list)        

print("-------Find Different Items (Difference) using For Loop--------")

list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]

set_b = set(list_b)
only_in_a = set()

for item in list_a:
    if item not in set_b:       # only keep items that do NOT exist in list_b
        only_in_a.add(item)

print("Only in list_a:", only_in_a)

print("-------Common Characters Between Two Strings--------")

word1 = "python"
word2 = "typhoon"

set1 = set(word1)      # unique characters of word1
set2 = set(word2)      # unique characters of word2

common_chars = set()

for ch in set1:
    if ch in set2:
        common_chars.add(ch)

print("Common characters:", common_chars)


print("-------Count Unique Words--------")

sentence = "the cat sat on the mat and the cat ran"
words = sentence.split()      # split() breaks sentence into a list of words

unique_words = set()

for word in words:
    unique_words.add(word)     # duplicates auto-skip because it's a set

print("All words:", words)
print("Unique words:", unique_words)
print("Total unique words:", len(unique_words))

print("-------Check if List has Duplicates--------")

numbers = [1, 2, 3, 4, 2, 5]
seen = set()          # keeps track of numbers we've already encountered
has_duplicate = False

for num in numbers:
    if num in seen:              # if we've seen this number before
        has_duplicate = True
        break
    seen.add(num)                 # otherwise, remember this number for next time

print("Has duplicates:", has_duplicate)


print("++++++++ done ++++++++++")






    