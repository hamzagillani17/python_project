print("======if elif else=======")
amount = 2000
print('Amount = ',amount)
if amount > 10000:
   discount = amount * 20 / 100
elif amount > 5000:
   discount = amount * 10 / 100
elif amount > 1000:
   discount = amount * 5 / 100
else:
   discount=0
print('Payable amount = ',amount - discount)

width = float(input("Enter width: "))
height = float(input("Enter height: "))

area = width * height

if area.is_integer():
    print("area of rectengel: ",int(area))
else:
   print("Area of Rectengal",area)   



# day
day = float(input("Enter Day Number (1-7): "))

if day == 1 and day.is_integer():
    print("Monday")

elif day == 2:
        print("Tuesday")
    
elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Invalid Day")


#p0sitiv negitivee

number = int(input("Enter a number: "))

if number > 0 and number % 2 == 0:
    print("Positive Even")

elif number > 0:
    print("Positive Odd")

elif number < -100:
    print("Bohat Chota Negative")

elif number < 0:
    print("Normal Negative")

else:
    print("Zero")


#
number = float(input("Enter a number: "))

if not(number.is_integer()):
    print("Number is Invalid")
elif number == 0:
    print("Number is Zero")    
elif number % 2 == 0 and number > 0: 
    print("Positive Even")
elif number % 2 ==1 and number > 0:
    print("Number Odd")
elif number < 0 :
    if number < -100:                    # Inner if - sirf tab check hoga jab number negative ho
        print("Bohat Chota Negative")
    else:
        print("Normal Negative")
else:
    print("Zero")    