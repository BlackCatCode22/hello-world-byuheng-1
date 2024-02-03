# largestOfThree.py

def find_largest(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        if num2 >= num3:
            return num2
        else:
            return num3


# Get input from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Find and print the largest of the three numbers
largest = find_largest(num1, num2, num3)
print("The largest of the three numbers is:", largest)
