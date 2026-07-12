print("=========Operator Precedence=========")

'''
Operator precedence determines the order in which operators are evaluated in an expression.
Operators with higher precedence are evaluated before operators with lower precedence.

An expression may have multiple operators to be evaluated. The operator precedence defines the order in which operators are evaluated.
In other words, the order of operator evaluation is determined by the operator precedence.'''

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("Value of (a + b) * c / d is ",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ",  e)

e = (a + b) * (c / d);    # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ",  e)

e = a + (b * c) / d;      #  20 + (150/5)
print ("Value of a + (b * c) / d is ",  e)

