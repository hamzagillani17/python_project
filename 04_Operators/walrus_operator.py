print("\n======Walrus Operator (:=)========")
'''The walrus operator (:=) is a new type of assignment operator that was introduced in Python 3.8
The walrus operator allows you to assign values to variables as part of an expression.
The walrus operator is also known as the assignment expression operator.
The walrus operator is used to assign a value to a variable and return that value at the same time.
The walrus operator is used to simplify code and make it more readable.
'''

print("\nExample 1: Using walrus operator in an if statement")
n = 5
if n > 3:
    print(n)
print("\nExample 2: Using walrus operator in an if statement")
if (n := 5) > 3:
    print(n) 


print("\nExample 1: Using walrus operator in a while loop")
# Without walrus operator
data = input("Enter data 1: ")
while data != "quit":
    
    print(f"You entered 1: {data}")
    break

    

# With walrus operator
while (data := input("Enter data: ")) != "quit":
    
    data = input("Enter data: ")
    print(f"You entered: {data}")
    print("Data length:", len(data))
    print("Data in uppercase:", data.upper())
    print("Data in lowercase:", data.lower())
    print("Data reversed:", data[::-1])
    print("Data with spaces removed:", data.replace(" ", ""))
    print("Data with vowels removed:", ''.join([c for c in data if c.lower() not in 'aeiou']))
    print("Data with consonants removed:", ''.join([c for c in data if c.lower() in 'aeiou']))
    break
    #end while loop and next iteration
    

print("\nExample 2: Using walrus operator in a while loop")
# Without walrus operator
numbers = [1, 2, 3, 4, 5]

# Normal tareeqa - len() do baar call ho raha hai
result = [len(str(n)) for n in numbers if len(str(n)) > 0]
print(result)
# Walrus ke sath - ek hi baar calculate hoga
result = [length for n in numbers if (length := len(str(n))) > 0]
print(result)

print("\nExample 3: Using walrus operator in a list comprehension")
# Without walrus operator
import random

if (num := random.randint(1, 10)) > 5:
    print(f"{num} 5 se bara hai")
else:
    print(f"{num} 5 se chota ya barabar hai")

print("\nExample 4: Using walrus operator in a list comprehension")


if n := 5 > 3:      # ❌ Ye galat samjha jayega -> (n := (5>3)) ban jayega
    print(n)        # ❌ Ye print karega True, n=5 assign nahi hoga
if (n := 5) > 3:     # ✅ Ye sahi hai -> (n := 5) ban jayega
    print(n)        # ✅ Ye print karega 5, n=5 assign hogah

