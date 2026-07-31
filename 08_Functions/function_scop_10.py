name = "Ali"          # global variable — bahar bana hai

def show():
    print(name)          # function ke andar se global ko PADH sakte hain

show()                  # Output: Ali

def greet():
    message = "Hello"     # local variable — sirf is function ke andar zinda hai

greet()
print(message)              # ❌ ERROR! 'message' function ke bahar exist hi nahi karta


print("-------Local vs Global--------")

city = "Karachi"           # global variable

def show_city():
    print("Inside function:", city)     # can READ the global variable

show_city()
print("Outside function:", city)

print("-------Local Variable Error--------")

def calculate():
    result = 100          # local variable, sirf is function ke andar hai
    print("Inside function:", result)

calculate()

try:
    print("Outside function:", result)      # this will fail
except NameError as e:
    print("Error:", e)


print("-------Same Name, Different Scope--------")

number = 10                  # global

def change_number():
    number = 50                # this creates a NEW local variable, doesn't touch the global one
    print("Inside function:", number)

change_number()
print("Outside function:", number)     # still 10, unaffected




print("-------Using global keyword--------")

balance = 1000

def deposit(amount):
    global balance             # this tells Python: "use the GLOBAL balance, don't make a new local one"
    balance += amount

deposit(500)
print("Balance after deposit:", balance)