print("\n=======Bitwise Operators=======")

'''The bitwise operators are used to compare (or) manipulate the bits of the numbers.
The bitwise operators are used to perform bit-level operations on binary numbers.
The two operands' values are processed bit by bit by the bitwise operators.
There are various Bitwise operators used in Python, such as bitwise OR (|), bitwise AND (&),
bitwise XOR (^), negation (~), Left shift (<<), and Right shift (>>).
'''

print("\nBitwise AND (&) Operator")
a = 10
b = 4
print("a & b = ", a & b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a & b: ", bin(a & b))
print("Decimal of a & b: ", int(bin(a & b), 2))

print("\nBitwise OR (|) Operator")
a = 10
b = 4
print("a | b = ", a | b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a | b: ", bin(a | b))
print("Decimal of a | b: ", int(bin(a | b), 2))

print("\nBitwise XOR (^) Operator")
a = 10
b = 4
print("a ^ b = ", a ^ b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a ^ b: ", bin(a ^ b))
print("Decimal of a ^ b: ", int(bin(a ^ b), 2))


print("\nBitwise NOT (~) Operator")
a = 10
b = 4
print("~a = ", ~a)
print("Binary of a: ", bin(a))
print("Binary of ~a: ", bin(~a))
print("Decimal of ~a: ", int(bin(~a), 2))
print("~b = ", ~b)
print("Binary of b: ", bin(b))
print("Binary of ~b: ", bin(~b))
print("Decimal of ~b: ", int(bin(~b), 2))

print("\nLeft Shift (<<) Operator")
a = 10
b = 4
print("a << b = ", a << b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a << b: ", bin(a << b))
print("Decimal of a << b: ", int(bin(a << b), 2))
print("\nRight Shift (>>) Operator")
a = 10
b = 4
print("a >> b = ", a >> b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a >> b: ", bin(a >> b))
print("Decimal of a >> b: ", int(bin(a >> b), 2))

print("\nBitwise AND (&) Operator with Negative Numbers")
a = -10
b = 4
print("a & b = ", a & b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a & b: ", bin(a & b))
print("Decimal of a & b: ", int(bin(a & b), 2))

print("\nBitwise OR (|) Operator with Negative Numbers")
a = -10
b = 4
print("a | b = ", a | b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a | b: ", bin(a | b))
print("Decimal of a | b: ", int(bin(a | b), 2))

print("\nBitwise XOR (^) Operator with Negative Numbers")
a = -10
b = 4
print("a ^ b = ", a ^ b)
print("Binary of a: ", bin(a))
print("Binary of b: ", bin(b))
print("Binary of a ^ b: ", bin(a ^ b))
print("Decimal of a ^ b: ", int(bin(a ^ b), 2))



print("\n=======End of Bitwise Operators=======")