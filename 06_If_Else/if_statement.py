print("\n=====Python If Statement=====")

'''The if statement in Python evaluates whether a condition is true or false.
It contains a logical expression that compares data, and a decision is made based on the result 
of the comparison.'''

a = 33
b = 200
if b > a:
  print("b is greater than a")

if b < a: print("b is less than a") #it will not print anything because the condition is false

if(b == a):
  print("b is equal to a") #it will not print anything because the condition is false

str = "Hello World"
str1 = "Hello World"
if(str == str1):
  print("str is equal to str1") #it will print because the condition is true

if(10 != 10):
  print("b is not equal to a") #it will print because the condition is true

#using if statement with logical operators
if a > 10 and b > 10:
  print("Both a and b are greater than 10") #it will print because the condition is true  
if a > 10 or b < 10:
  print("Either a is greater than 10 or b is less than 10") #it will print because the condition is true
if not(a > 10 and b < 10):
  print("Either a is not greater than 10 or b is not less than 10") #it will print because the condition is true      

# if statment using input
num = int(input("Enter a number: "))
if num > 20:
  print("The number is greater than 20")
