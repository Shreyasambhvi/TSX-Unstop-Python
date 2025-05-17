# Task: Checking for leap year

x = int(input("Enter the year: "))       # Taking input

if (x%4==0):
    if (x%100==0):
        if(x%400==0):
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")            # Condition checks
