# Task: Applying different types of operations

print("Enter the two numbers: ")

#Taking inputs
a=int (input())
b=int (input())

#Arithmetic operations
print("Sum=",a+b)
print("Difference=",a-b)
print("Product=",a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)

#Bitwise operations
print(a|b)
a_b=bin(a)
print(a_b)
b_b=bin(b)
print(b_b)
print(a&b)
print(~a,~b)
print(a^b)
print(a<<2, a>>2)
print(b<<3, b>>3)

#Comparision Operations
print(a>b)
print(a<b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b)

#Logical Operations
print(a%2==0 and b%2==0)
print(a%2==0 or b%2==0)
print(not(a+b==29))

#Identity Operations
print(a is b)
print(a is not b)

#Membership Operations
C=['a','b','d','e']
print('j' in C)
print('b' not in C)