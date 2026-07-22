print("=======pass===continue===break=======")

'''Pass: It is a null statement in Python. It is used when a statement is required syntactically 
    but you do not want any command or code to execute.
   Continue: It is used to skip the current iteration of a loop and continue with the next iteration.
   Break: It is used to terminate the loop entirely and exit from it.'''

print("\n==============Pass Statement=================")
for i in range(5):
    if i == 2:
        pass    # do nothing, just a placeholder
    print(i)        


for num in [1, 2, 3, 4, 5]:
    if num == 3:
        pass              # "abhi kuch nahi karna" — bas jagah bhar di
    else:
        print(num) 

          
print("-------Pass: Empty Function Body--------")

def process_transaction(amount):
    pass          # function is planned but logic not written yet — pass avoids an error

transactions = [100, 200, 300]
i = 0

while i < len(transactions):
    process_transaction(transactions[i])   # calling the empty function — runs without error
    print("Processed transaction:", transactions[i])
    i += 1
print("All transactions processed")

print("-------Pass: Building Conditional Logic--------")

grades = [85, 45, 92, 60, 30]

for grade in grades:
    if grade >= 90:
        print(grade, "-> A grade")
    elif grade >= 75:
        pass              # B grade logic not decided yet, will add later
    elif grade >= 50:
        print(grade, "-> C grade")
    else:
        print(grade, "-> Fail")

print("Grading loop complete")



print("\n===========Continue Statement=============")

for i in range(5):
    if i == 2:
        continue    # skip the rest of the loop for this iteration
    print(i)



print("-------Continue: Sum Only Positive Numbers--------")

numbers = [10, -5, 20, -8, 15]
i = 0
total = 0

while i < len(numbers):
    if numbers[i] < 0:
        i += 1                  # IMPORTANT: increase i BEFORE continue, or infinite loop!
        continue                 # skip adding this negative number, go back to condition
    total += numbers[i]
    i += 1

print("Sum of positive numbers:", total) 

print("-------Continue: Skip Vowels--------")

word = "programming"
vowels = "aeiou"

for ch in word:
    if ch in vowels:
        continue              # skip vowels, only print consonants
    print(ch, end=" ")

print()   # move to next line at the end




print("=============Break: Search in a List=============")

for num in [1, 5, 8, 12, 3, 9]:
    if num == 12:
        print("Found it!")
        break            # loop turant ruk jayega, baaki numbers check hi nahi honge
    print("Checking:", num)

numbers = [4, 8, 15, 16, 23, 42]
target = 16

for num in numbers:
    if num == target:
        print("Target found:", num)
        break            # stop the loop immediately once target is found
    print("Checking:", num)

print("Search complete")

print("-------Break: Stop at First Negative Number--------")

numbers = [5, 12, 8, -3, 9, 20]
i = 0

while i < len(numbers):
    if numbers[i] < 0:
        print("Negative number found, stopping loop")
        break              # exit the while loop as soon as a negative number appears
    print("Positive number:", numbers[i])
    i += 1

print("Loop ended")

print("-------Break: Login System--------")

correct_pin = "4521"
attempts = 0

while True:                     # infinite loop, only break can stop it
    entered_pin = input("Enter your PIN: ")
    attempts += 1

    if entered_pin == correct_pin:
        print("Login successful!")
        break                    # correct pin entered, exit the loop

    if attempts == 3:
        print("Too many failed attempts. Account locked.")
        break                    # max attempts reached, exit the loop

    print("Wrong PIN, try again")

 

