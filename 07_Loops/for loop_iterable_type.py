print("=======iterable type in for loop=======")

'''In Python, an iterable is any object capable of returning its members one at a time, permitting it to be iterated over in a for-loop.
An iterable object implements the __iter__() method, which returns an iterator object. The iterator object implements the __next__() method, which returns the next item in the sequence. When there are no more items to return, it raises a StopIteration exception.
'''
#List
print("\n-----List-----")
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
print(reversed_list)

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

print("Has duplicates?", has_duplicate)