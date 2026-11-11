def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Division by zero is not possible"
    return a / b
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Select an operation:")
print("+ for Addition")
print("- for Subtraction")
print("* for Multiplication")
print("/ for Division")

operation = input("Enter your choice: ")
if operation == "+":
    result = addition(num1, num2)

elif operation == "-":
    result = subtraction(num1, num2)

elif operation == "*":
    result = multiplication(num1, num2)

elif operation == "/":
    result = division(num1, num2)

else:
    result = "Invalid operation"
print("Result:", result)
