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
day = int(input("Enter Day Number (1-7): "))

if day == 1:
    print("Monday")
    if 

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