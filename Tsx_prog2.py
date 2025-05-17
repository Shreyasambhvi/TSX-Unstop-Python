# Task: Python script to calculate the area and perimeter of rectangle using variables

x = float(input("Enter the length:"))
y = float(input("Enter the breadth:")) # Taking inputs

perimeter = 2 * (x+y)
area = x*y              # Calculating perimeter and area

print("Perimeter of rectangle:",perimeter,"units")
print("Area of rectangle:",area,"sq. units")        # Printing the results
