print("=======Ternary (Conditional) Expression=======")

'''Ternary (Conditional) Expression : It is a concise way to write an if-else statement in a single line.
The syntax for a ternary expression is:
value_if_true if condition else value_if_false'''

age = int(input("Enter your age: "))
status = "Eligible to vote" if age >= 18 else "Not eligible to vote"
print(status)

number = int(input("Enter a number: "))
result = "Positive" if number > 0 else "Negative" if number < 0 else "Zero"
print(result)

number1 = int(input("Enter a number: "))
result1 = "Even" if number1 % 2 == 0 else "Odd"
print(result1)

