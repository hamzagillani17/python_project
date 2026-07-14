print("\n======if else======")

'''The if-else statement in Python is used to execute a block of code 
when the condition in the if statement is true,
and another block of code when the condition is false.'''

vote_age = int(input("Enter your age: "))
if vote_age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")    

# mit Logical AND 

age_ver = int(input("Enter Your age: "))
id_ver = input("You have ID ? Please type (yes or no): ")

if (age_ver >=18 and id_ver == "yes"):
    print("Yor are eligible for Vote")
else:
    print("You are not eligible")  

# mit Logical Not

is_raining = input("Kya baarish ho rahi hai? (yes/no): ")

if not (is_raining == "yes"):
    print("Bahar jaa sakte hain, mausam theek hai")
else:
    print("Ghar par rahein, baarish ho rahi hai")

username = input("Username enter: ")
password = input("Password enter: ")
is_blocked = input("Kya account blocked hai? (yes/no): ")

if (username == "admin" and password == "12345") and not (is_blocked == "yes"):
    print("Login Successful")
else:
    print("Login Failed - Wronge credentials or account blocked") 

marks = int(input("Enter Your Marrks: "))
attendance_ver = int(input("Attendence %: "))

if marks >= 50 and attendance_ver >= 60 :
    print("pass")
else:
    print("fail")    


# discount calculate

amount_ver = int(input("Enter Amount: "))
print("Your entered:", amount_ver)

if amount_ver >= 10000:
    discount = amount_ver * 20 / 100     # 20% discount
else:
    if amount_ver >= 5000:
        discount = amount_ver * 10 / 100  # 10% discount
    else:
        if amount_ver >= 1000:
            discount = amount_ver * 5 / 100   # 5% discount (ye pehle se sahi tha)
        else:
            discount = 0

print("Payable amount = ", amount_ver - discount)             


