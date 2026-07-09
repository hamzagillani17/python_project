''' What are Python Operators?
Python operators are symbols used to perform specific operations on values and variables.
The values or variables on which the operators work are called operands.
Operators are important because they help in writing conditions, calculations, and logic in a program.

Types of Python Operators
Different types of Operators used in Python are as follows:

1- Arithmetic Operators
2- Comparison Operators
3- Assignment Operators
4- Logical Operators
5- Bitwise Operators
6- Membership Operators
7- Identity Operators'''

print("\n============ 1- Arithmetic Operators=============")

# Python Arithmetic Operators
'''Python arithmetic operators are used to perform mathematical operations such as
addition, subtraction, multiplication, division, and more on numbers.
Arithmetic operators are binary operators in the sense they operate on two operands.
Python fully supports mixed arithmetic. That is, the two operands can be of two different number types.
In such a situation. ''' 

int_a = 10
int_b = 5
float_a = 30.40
complx_a = 10+3j

add_integer_ver = int_a + int_b
sub_int_ver = int_a - int_b
div_ver = int_a / int_b
mul_ver = int_a * int_b 
mod_ver = int_a % int_b
exp_ver = int_a ** int_b

add_complx_integer = int_a + complx_a
add_complx_float = complx_a + float_a
sub_integer_complx = int_a - complx_a 

print("a plus b = ",add_integer_ver)
print("a subtraction b = ", sub_int_ver)
print("a divide b = ",div_ver)
print("a multiply b = ",mul_ver)
print(" a moduls b = ", mod_ver)
print("a Exponents b ", exp_ver)
print("a add complx = ",add_complx_integer, type(add_complx_integer))
print("a add")

print("\n")
# Using format () method
print("a: {} b: {} a + b = {}  ".format(int_a,int_b,add_integer_ver))
print("a: {} b: {} a-b = {}".format(int_a,int_b,sub_int_ver))
print("a: {} b: {} a / b = {}".format(int_a,int_b,div_ver))
print("a: {} b: {} a * b = {}".format(int_a,int_b,mul_ver))
print("a: {} b: {} a % b = {} ".format(int_a,int_b,mod_ver))
print("a: {} b:{} a**b = {}".format(int_a,int_b,exp_ver))












