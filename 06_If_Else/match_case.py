print("=======Match Case=======")
'''Match Case : It is a new feature introduced in Python 3.10 that allows you to match values against patterns 
   and execute code based on the matched pattern.
   The syntax for a match case statement is:
match value:
    case pattern1:
        # code to execute if value matches pattern1
    case pattern2:
        # code to execute if value matches pattern2
    case _:
        # code to execute if value does not match any pattern
        # The underscore (_) is a wildcard pattern that matches any value.
        # You can also use the match case statement with multiple patterns and guards to create more complex matching logic.  
        
        With the release of Python 3.10, a pattern matching technique called match-case has been introduced,
        which is similar to the switch-case construct available in C/C++/Java etc.
        Its basic use is to compare a variable against one or more values.
        It is more similar to pattern matching in languages like Rust or Haskell than a switch statement in C or C++.'''

#if else statement elif
day = int(input("Enter day number: "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
# ... aur aage
else:
    print("Invalid day")

#match case statement
day = int(input("Enter day number: "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")    
    case _:
        print("Invalid day")

#make case statement with multiple patterns
num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

operator = input("Enter Operator (+,-,*,/): ")


match operator:

    case "+":
        print("Result =", num1 + num2)

    case "-":
        print("Result =", num1 - num2)

    case "*":
        print("Result =", num1 * num2)

    case "/":
        print("Result =", num1 / num2)

    case _:
        print("Invalid Operator")        

#using match case with multiple patterns and guards
value = int(input("Enter a number: "))
match value:
    case x if x > 0:
        print("Positive number")
    case x if x < 0:
        print("Negative number")
    case 0:
        print("Zero")
    case _:
        print("Invalid input")

#usking weekend() 

def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
print (weekday(3))
print (weekday(6))
print (weekday(7))        

#access() function using match case
def access(user):
   match user:
      case "admin" | "manager": return "Full access"
      case "Guest": return "Limited access"
      case _: return "No access"
print (access("manager"))
print (access("Guest"))
print (access("Ravi"))

#List as the Argument in Match Case Statement
def greeting(details):
   match details:
      case [time, name]:
         return f'Good {time} {name}!'
      case [time, *names]:
         msg=''
         for name in names:
            msg+=f'Good {time} {name}!\n'
         return msg

print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))


