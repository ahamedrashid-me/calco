#!python/main.py   
import time 
import math
print("This is a basic calculator")

time.sleep(3)

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square")
    print("6. Square root")
    print("7. Power")
    print("0. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        time.sleep(3)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("Result: ", result)
    elif choice == 2:
        time.sleep(3)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print("Result: ", result)
    elif choice == 3:
        time.sleep(3)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print("Result: ", result)
    elif choice == 4:
        time.sleep(3)
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print("Result: ", result)   
     
    elif choice == 5:
        time.sleep(3)
        num1 = float(input("Enter number to square: "))
        result = num1 ** 2
        print("Result: ", result)
    elif choice == 6:
        time.sleep(3)
        num1 = float(input("Enter number to find root: "))
        result = num1 ** 0.5
        print("Result: ", result)
    elif choice == 7:
        time.sleep(3)
        num1 = float(input("Enter base number: "))
        num2 = float(input("Enter power: "))
        result = num1 ** num2
        print("Result: ", result)
    
    elif choice == 0:
        break
    else:
        print("Invalid choice. Please try again.") 
    
