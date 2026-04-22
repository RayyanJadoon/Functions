def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("Select operation:")
print("a. add")
print("b.subtract")
print("c. multiply")
print("d. divide")

calc = input("Enter choice:  ")

num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number:  "))

if calc == "a":
    print(num1, "+", num2, "=", add(num1, num2))
elif calc == "b":
  print(num1, "-", num2, "=", subtract(num1, num2))
elif calc == "c":
    print(num1, "x", num2, "=", multiply(num1, num2))
elif calc == "d":
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("invalid input")

