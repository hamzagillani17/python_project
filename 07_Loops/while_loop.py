print("\n===============While Loop===============")

'''While loop is used to execute a block of code repeatedly as long as a given condition is true.
   The syntax of while loop in Python is:
   while condition:
    # code block'''

print("\n-------Basic Counting--------")

count = 1

while count <= 5:
    print(count)
    count += 1     # Incrementing the count variable by 1 in each iteration
    
    
print("\n-------Countdown--------")

count = 5

while count >= 1:
    print(count, end=" ")
    count -= 1 # Decrementing the count variable by 1 in each iteration

print("\n-------Sum using While Loop--------")

num = 1
total = 0


while num <= 10:
    total += num
    num += 1

print("Sum of 1 to 10:", total)


print("\n-------Access List using While Loop--------")

fruits = ["apple", "banana", "cherry", "mango"]
i = 0                          # manual index counter

while i < len(fruits):
    print(f"Index: {i} : {fruits[i]}")
    i+=1
print("Loop ended because index reached the list length")

print("-------Reverse String using While--------")

text = "hello"
reversed_text = ""
i = len(text) - 1       # start from the LAST index
print(i)

while i >= 0:
    reversed_text += text[i]     # add characters from end to start
    i -= 1

print("Original:", text)
print("Reversed:", reversed_text)


print("\n-------Password Check using While + Break--------")

correct_password = "python123"

while True:                    # infinite loop — will run forever unless stopped
    entered = input("Enter password: ")
    
    if entered == correct_password:
        print("Access granted!")
        break                    # manually stopping the infinite loop
    else:
        print("Wrong password, try again")

print("-------Skip Even Numbers using Continue--------")

num = 0

while num < 10:
    num += 1
    if num % 2 == 0:
        continue           # skip the print, go back to condition check
    print(num)

print("-------Sum of Digits--------")

number = 4523
temp = number
digit_sum = 0

while temp > 0:
    last_digit = temp % 10       # % gives the remainder — that's the last digit
    digit_sum += last_digit
    temp = temp // 10             # remove the last digit

print(f"Sum of digits of {number}: {digit_sum}")

print("-------Guess the Number Game--------")

secret_number = 7
attempts = 0
max_attempts = 3
guessed_correctly = False       # flag variable, jesa pehle seekha tha

while attempts < max_attempts and guessed_correctly == False:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You win!")
        guessed_correctly = True
    elif guess < secret_number:
        print("Too low, try again")
    else:
        print("Too high, try again")

if guessed_correctly == False:
    print(f"Game over! The number was {secret_number}")

print(f"Total attempts used: {attempts}")

print("-------Reverse a Number--------")

number = 1234
temp = number
reversed_num = 0

while temp > 0:
    last_digit = temp % 10               # extract last digit
    reversed_num = reversed_num * 10 + last_digit    # build reversed number
    temp = temp // 10                     # remove last digit

print(f"Original: {number}, Reversed: {reversed_num}")

print("-------Palindrome Number Check--------")

number = 12321
temp = number
reversed_num = 0

while temp > 0:
    last_digit = temp % 10
    reversed_num = reversed_num * 10 + last_digit
    temp = temp // 10

if number == reversed_num:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is NOT a palindrome")

print("-------Binary Search--------")

numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]
target = 23

low = 0
high = len(numbers) - 1
found_index = -1

while low <= high:
    mid = (low + high) // 2      # find the middle index

    if numbers[mid] == target:
        found_index = mid
        break
    elif numbers[mid] < target:
        low = mid + 1              # search in the right half
    else:
        high = mid - 1              # search in the left half

if found_index != -1:
    print(f"{target} found at index {found_index}")
else:
    print(f"{target} not found")

print("-------Simple Menu Program--------")

while True:
    print("\n1. Say Hello")
    print("2. Show Square of a Number")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Hello there!")
    elif choice == "2":
        num = int(input("Enter a number: "))
        print("Square:", num * num)
    elif choice == "3":
        print("Exiting program...")
        break             # this is the only way to stop the infinite loop
    else:
        print("Invalid choice, try again")

print("-------ATM Withdrawal Simulation--------")

balance = 5000
transaction_count = 0

while balance > 0:
    print(f"\nCurrent balance: {balance}")
    amount = int(input("Enter amount to withdraw (or 0 to stop): "))

    if amount == 0:
        print("Session ended by user")
        break

    if amount > balance:
        print("Insufficient balance!")
        continue          # skip the rest, go back and ask again

    balance -= amount
    transaction_count += 1
    print(f"Withdrawn: {amount}, Remaining balance: {balance}")

if balance == 0:
    print("\nBalance fully withdrawn")

print(f"Total transactions: {transaction_count}")                
    
    
    
    
