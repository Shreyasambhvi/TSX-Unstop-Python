# Task: Comparison of two input numbers

x = float(input("Enter first number:"))
y = float(input("Enter second number:")) # Taking inputs

if (x<y):
    print("%f is smaller than %f" %(x,y))
elif (x==y):
    print("%f is equal to %f" %(x,y))
elif (x>y):
    print("%f is greater than %f" %(x,y)) # Checking the three conditions and printing accordingly

