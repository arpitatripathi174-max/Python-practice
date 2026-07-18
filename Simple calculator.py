a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator (+,-,*,/,%): ")

if operator == "+":
    print("Addition:", a + b)

elif operator == "-":
    print("Subtraction:", a - b)

elif operator == "*":
    print("Multiplication:", a * b)

elif operator == "/":
    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

elif operator == "%":
    print("Remainder:", a % b)

else:
    print("Invalid operator")
