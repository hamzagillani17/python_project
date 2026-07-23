print("======= Input Function =======")

name = input("Enter Your Name: ")
age = input("Enter Your age Please: ")

print("\nThanks")

print("yor name is: ",name ,"\n", "Your are ",age," Year old")

#Taking Numeric Input in Python
width = input("Enter width : ")
w= int(width)
height = input("Enter height : ")
h= int(height)
area = w*h
print ("Area of rectangle = ", area)
#special trick handel for float value
width = input("Enter width : ")
w = float(width)
height = input("Enter height : ")
h = float(height)
area = w * h

if area.is_integer():
    print("Area of rectangle = ", int(area))   # whole number hai to int dikhao
else:
    print("Area of rectangle = ", area)          # decimal hai to float hi dikhao

amount = float(input("Enter Amount : "))
rate = float(input("Enter rate of interest : "))

interest = amount*rate/100
print ("Amount: ", amount, "Interest: ", interest)

#! /usr/bin/python3.11

city="Lahore"
state="punjab"
country="Pakistan"
print(city, state, country, sep=',')

print("City:", city, end=" ")
print("State:", state)
