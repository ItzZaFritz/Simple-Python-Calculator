# Python Projects

def add(x, y):
    """Addition equation of two numbers that leaves a sum"""
    return x + y


def subtract(x, y):
    """Subtraction equation of two numbers that leaves a difference"""
    return x - y


def multiply(x, y):
    """Multiplication equation of two numbers that leaves a product"""
    return x * y


def divide(x, y):
    """Dividition equation of two numbers that leaves a quotient"""
    return x / y


def whole_divide(x, y):
    """Whole division equation of two numbers that leaves a whole quotient"""
    return x // y


def modulus_divide(x, y):
    """Modulus Division equation of two numbers that leaves a remainder"""
    return x % y


def exponent_multiply(x, y):
    """Exponential Multiplication equation of two numbers that leaves a product"""
    return x ** y


print("Calculator starts running")
print("Here are the different options you can choose from, 1/2/3/4/5/6/7")
print("Option 1, +, Addition")
print("Option 2, -, Subtraction")
print("Option 3, *, Multiplication")
print("Option 4, /, Division")
print("Option 5, //, Whole Division")
print("Option 6, %, Modulus Division")
print("Option 7, **, Exponential Multiplication")

num1 = int(input("Choose your first number: "))
choice = input("Choose your equation option: ")
num2 = int(input("Choose your second number: "))

if choice == "+":
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
elif choice == "//":
    print(num1, "//", num2, "=", whole_divide(num1, num2))
elif choice == "%":
    print(num1, "%", num2, "=", modulus_divide(num1, num2))
elif choice == "**":
    print(num1, "**", num2, "=", exponent_multiply(num1, num2))
else:
    print("Invalid Equation Input")
print("Calculation Completed")