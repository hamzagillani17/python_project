print("\n=======Number system======")

print("\ndecimal number system start 0,1,2,3,4,5,6,7,8,9")

#integer
a_int = 10
b_int = 20
c_int = a_int + b_int

print ("a_int:", a_int, "type:", type(a_int))
print ("c_int:", c_int, "type:", type(c_int))


'''Binary Numbers in Python
A number consisting of only the binary digits (1 and 0) and prefixed with "0b" is a binary number.
If you assign a binary number to a variable, it still is an int variable.

A represent an integer in binary form, store it directly as a literal, or use int() function, in which the base is set to 2'''
print("\nconverion binary to decimal using int() function and binary number using 0b prefix")
a_bin = 0b1010 #10
b_bin = 0b1011 #11
c_bin = a_bin + b_bin
print ("a_bin:", a_bin, "type:", type(a_bin))
print ("b_bin:", b_bin, "type:", type(b_bin))
print ("c_bin:", c_bin, "type:", type(c_bin))

#binary number using int() function
a_bin_to_int= int("0b1010", 2) #10
b_bin_to_int= int("0b1011", 2) #11

print("a_bin_to_int:", a_bin_to_int, "type:", type(a_bin_to_int))
print("b_bin_to_int:", b_bin_to_int, "type:", type(b_bin_to_int))
c_bin_to_int= a_bin_to_int + b_bin_to_int
print ("c_bin_to_int:", c_bin_to_int, "type:", type(c_bin_to_int))

print("\nconverion decimal to binary using bin() function")
a_int_to_bin= bin(10) #0b1010
print("a_int_to_bin:", a_int_to_bin, "type:", type(a_int_to_bin))

print("\nconverion decimal to binary using format() function")
a_int_to_bin= format(10, 'b') #1010
print("a_int_to_bin:", a_int_to_bin, "type:", type(a_int_to_bin))

print("\nconverion decimal to binary using f-string")
a_int_to_bin= f"{10:b}" #1010
print("a_int_to_bin:", a_int_to_bin, "type:", type(a_int_to_bin))

print("\nconverion decimal to binary using string method")
a_int_to_bin= str(bin(10))[2:] #1010
print("a_int_to_bin:", a_int_to_bin, "type:", type(a_int_to_bin))


print("\nBinary to octal conversion using oct() function")

bin_a = 0b1010 #10
bin_to_oct = oct(0b1010) #0o12
print("oct_value:", bin_to_oct, "type:", type(bin_to_oct))

print("\nBinary to hexadecimal conversion using hex() function")
bin_a = 0b1010 #10
bin_to_hex = hex(0b1010) #0xa
print("hex_value:", bin_to_hex, "type:", type(bin_to_hex))

print("\nBinary to decimal conversion using int() function")
bin_a = 0b1010 #10
bin_to_dec = int(0b1010) #10
print("dec_value:", bin_to_dec, "type:", type(bin_to_dec))


