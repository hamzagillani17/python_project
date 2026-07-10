

'''
Comparison operators in Python are very important in Python's conditional statements (if, else and elif)a
nd looping statements (while and for loops). The comparison operators also called relational operators.
Some of the well known operators are "<" stands for less than, and ">" stands for greater than operator.

<	Less than	a<b
>	Greater than	a>b
<=	Less than or equal to	a<=b
>=	Greater than or equal to	a>=b
==	Is equal to	a==b
!=	Is not equal to	a!=b

Comparison operators are binary in nature, requiring two operands.
An expression involving a comparison operator is called a Boolean expression,
and always returns either True or False.

'''

a = 46    # Initializing the value of a      
b = 4     # Initializing the value of b      
    
print("For a =", a, "and b =", b,"\nCheck the following:")

# printing different results  
  
print('1. Two numbers are equal or not:', a == b)      
print('2. Two numbers are not equal or not:', a != b)      
print('3. a is less than or equal to b:', a <= b)      
print('4. a is greater than or equal to b:', a >= b)      
print('5. a is greater than b:', a > b)      
print('6. a is less than b:', a < b)

# Comparison of Complex numbers

a=10+1j
b=10.-1j
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

# print ("a=",a, "b=",b,"a>b is",a>b) TypeError: '>' not supported between instances of 'complex' and 'complex'
# print ("a=",a, "b=",b,"a>b is",a>b)


print("\nComparison of Booleans")

'''Boolean objects in Python are really integers: True is 1 and False is 0. In fact,
Python treats any non-zero number as True. In Python,
comparison of Boolean objects is possible. "False < True" is True!'''

a = True
b = False

print ("a=",a, "b=",b,"a < b is",a<b)
print("a = {} b = {} a > b is {}".format(a,b,a>b))
print("a = {} b = {} a == b {}".format(a,b,a==b))
print("a = {} b = {} a != b {}".format(a,b,a!=b))
print("a = {} b = {} a >= b {}".format(a,b,a>=b))
print("a = {} b = {} b >= a {}".format(a,b,b>=a))



'''# Comparison of Sequence Types
print("=========comparison of different sequence types=========")
a=(1,2,3)
b=[1,2,3]
print ("a=",a, "b=",b,"a<b is",a<b)
TypeError: '<' not supported between instances of 'tuple' and 'list'
'''


print ("\n=======comparison of strings=======")

a='BAT'
b='BALL'
print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a>b is",a>b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)

print ("\n=========comparison of tuples========")

a = (1,2,3,4)
b = (1,2,3,5)

print ("a=",a, "b=",b,"a<b is",a<b)
print ("a=",a, "b=",b,"a>b is",a>b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)
print("a = {} b = {} a >= b {}".format(a,b,a>=b))
print("a = {} b = {} b >= a {}".format(a,b,b>=a))

print("=====Comparison of Dictionary Objects======")
# Python dictionaries are simply compared by length.
# The use of "<" and ">" operators for Python's dictionary is not defined.

a = {1:1 ,2:2, 3:3, 4:4}
b = {1:1, 2:2, 3:3}

# print ("a=",a, "b=",b,"a<b is",a<b)
# print ("a=",a, "b=",b,"a>b is",a>b)
print ("a=",a, "b=",b,"a==b is",a==b)
print ("a=",a, "b=",b,"a!=b is",a!=b)
# print("a = {} b = {} a >= b {}".format(a,b,a>=b))
# print("a = {} b = {} b >= a {}".format(a,b,b>=a))



