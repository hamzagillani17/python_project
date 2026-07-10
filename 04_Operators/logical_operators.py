print("\n======Python Logical Operators=====\n")
print("\n-------------And-----------")

print(20 and 10) #10
#In AND OPerator when both condition are true or retuen 1 then last  bject show
print(True and False) #False
print(False and True) #False
print(0 and True)     #0
print(True and 0)     #0
print(1 and 1)        #1
print(True and True)  #True
print("" and "Python") #python
print(None and "Admin") #admin
print([] and 500) #[]

age = 20
print(age >18 and "adult")

age = 16
print(age >18 and "adult")

username = "admin"
password = "Python123"
otp = 4567
print(username == "admin" and password == "Python123" and otp == 4567)

username = "admin"
password = "Python123"
otp = 4567
print(username == "admin" and password == "Python123" and otp == 4567)


print("\n-----------OR-----------")
print(20 or 10) #20
print(True or False) #True
print(False or True) #True
print(0 or True)     #True 
print(True or 0)     #True
print(1 or 1)        #1
print(True or True)  #True
print("" or "Python") #python
print(None or "Admin") #admin
print([] or 500) #[]

email = ""
phone = "03001234567"

print(bool(email) or bool(phone)) #True

browser = "Firefox"
print(browser == "Chrome" or browser == "Edge" or browser == "Firefox") #true

print("\n------------NOT-----------")

is_admin = False
print(not is_admin) #True

is_logged_in = True
print(not is_logged_in) #False

age = 17
print(not (age >= 18)) #True


browser = "Safari"
print(not (browser == "Chrome")) #True


print("\n-----------------------")

print("Python" and "Automation" or "Java") #Automation
print(not (0 or []))                       #True
print(not (10 and "" or 50))               #False
print(5 and 8 and 0 and 10)                #0


x = 10
y = 20
print("x%2 == 0 and y%2 == 0:",x%2 == 0 and y%2 == 0) #True
print ("not (x+y>15):", not (x+y)>15)                 #False

