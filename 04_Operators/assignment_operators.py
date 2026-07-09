print("\nAssignment Operators")
'''
a += b: 40
a -= b: 28
a *= b: 204
a /= b: 5.666666666666667
a %= b: 4
a **= b: 1544804416
a //= b: 5
'''

print("\nAugmented Addition Operator (+=)")

a=10
b=5

print("Augmented addition of int and int")
a+=b # equivalent to a=a+b
print ("a =",a, "type(a):", type(a))
b+=1 #equivalent to b=b+1
print("\nb = ",b)

a=10
b=5.5

print ("Augmented addition of int and float")
a+=b  # equivalent to a=a+b
print ("a=",a, "type(a):", type(a))

a=10.50
b=5+6j
print ("Augmented addition of float and complex")
a+=b #equivalent to a=a+b
print ("a=",a, "type(a):", type(a))
b+=1
print(b,"\ntype", type(b))

print("\n-------Augmented Subtraction Operator (-=)---------")






